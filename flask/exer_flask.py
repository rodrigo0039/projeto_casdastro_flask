from flask import Flask, redirect, render_template, request, url_for
import psycopg2

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        user = request.form["name"]
        age = request.form["idade"]
        matricula = request.form["matricula"]
        conecta(user, age, matricula)
        return redirect(url_for("success", nome=user))
    return render_template("cadastro.html")


def conecta(user, age, matricula):
    conectar = psycopg2.connect(database="postgres", user="postgres", password="aluno", host="localhost")
    cur = conectar.cursor()
    cur.execute(f"INSERT INTO alunos(nome, idade, matricula) VALUES ('{user}', {age}, '{matricula}')")
    conectar.commit()
    cur.close()
    conectar.close()


@app.route("/success/<nome>")
def success(nome):
    return render_template("success.html", nome=nome)


if __name__ == "__main__":
    app.run()
