from flask import Flask, render_template, request, session

app = Flask(__name__)
app.debug = True

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/", methods=['GET', 'POST'])
def tally_demo():
    # print(tally)

    if 'tally' not in session:
        session['tally'] = 0

    # print(session['tally'])
    if 'addx' in request.form:
        session['tally'] += 1

    if 'subx' in request.form and session['tally'] > 0:
        session['tally'] -= 1

    print(session['tally'])
    return render_template("base.html", tally=session['tally'])

