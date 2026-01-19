from flask import Flask, render_template
from data.resume_data import resume

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", resume=resume)

@app.route("/about")
def about():
    return render_template("about.html", resume=resume)

@app.route("/skills")
def skills():
    return render_template("skills.html", resume=resume)

@app.route("/projects")
def projects():
    return render_template("projects.html", resume=resume)

@app.route("/education")
def education():
    return render_template("education.html", resume=resume)

@app.route("/contact")
def contact():
    return render_template("contact.html", resume=resume)

if __name__ == "__main__":
    app.run(debug=True)
