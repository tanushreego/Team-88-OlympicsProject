from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", 
                           story_url=url_for("story"),
                           insights_url=url_for("insights"),
                           dashboards_url=url_for("dashboards"),
                           about_url=url_for("about"))

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/insights")
def insights():
    return render_template("insights.html")

@app.route("/dashboards")
def dashboards():
    return render_template("dashboards.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=False, port=8000)
