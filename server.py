from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "The schnozberries taste like schnozberries!"


@app.route('/')
def index():

    return render_template("index.html")


@app.route('/users', methods=["POST"])
def create_user():
    print(request.form)
    if request.form['form'] == "login":
        pass
    elif request.form['form'] == "register":
        pass
    session['name'] = request.form["name"]
    session['email'] = request.form["email"]
    return redirect("/success")


@app.route('/success')
def success():
    return render_template("index.html", name=session['name'], email=session['email'])


if __name__ == "__main__":
    app.run(debug=True)
