from flask import Flask, flash
from flask import redirect, render_template
from flask import url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee299c6e45dff93b72946c1f4f501de2'

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
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',
               'success')
        return redirect(url_for('home'))

    return render_template("register.html",
                            title='Register',
                            form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You habe been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
        return redirect(url_for('home'))
    return render_template("login.html",
                            title='Login',
                            form=form)


if __name__ == '__main__':
    app.run(debug=True)


