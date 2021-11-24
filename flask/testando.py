from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def cadastro():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("success", nome=user))
    return render_template("cadastro.html")

@app.route("/success/<nome>")
def success(nome):
    return render_template("teste.html", nome=nome)


if __name__ == "__main__":
    app.run()
