from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# charger les données
df = pd.read_csv("movies_clean.csv")

movies = df.to_dict(orient="records")

@app.route("/")
def home():
    return render_template("index.html", movies=movies)

@app.route("/movie/<int:id>")
def movie_detail(id):
    movie = movies[id]
    return render_template("movie.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)