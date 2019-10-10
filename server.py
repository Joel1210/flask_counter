from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'this is a secret'

@app.route('/')
def index():
    if 'counter' in session: 
        session['counter'] += 1
    else:
       session['counter'] = 1
    return render_template("index.html")


@app.route('/destroy_session', methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

@app.route('/addtwo', methods=['POST'])
def addtwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/addamount', methods=['POST'])
def addamount():
    session['counter'] += int(request.form['addby']) - 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)