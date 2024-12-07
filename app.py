from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path.home() / r"D:\DAB111\GroupProject\database"

db_name = "champions.db"
db_path = base_path / db_name


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    champs = cursor.execute("SELECT * FROM champs").fetchall()
    con.close()

    return render_template("data.html", champs = champs) # template data_table 

@app.route("/link")
def references():
    return render_template("references.html")
  
if __name__=="__main__":
    app.run(debug=True)
