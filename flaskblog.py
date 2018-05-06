from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

posts = [
        {
            'author': 'Slavisa Karalic',
            'title': 'Blog Post 1',
            'content': 'First post content',
            'date_posted': 'April 20, 2018'
            },
        {
            'author': 'Slavisa Karalic',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'April 21, 2018'
            }
        ]
@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)


