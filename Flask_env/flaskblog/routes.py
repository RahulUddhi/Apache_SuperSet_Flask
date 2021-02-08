from flask import flash, redirect, render_template, url_for
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post


posts = [
    {
        'author':'Rahul',
        'title':'Flask Blog post',
        'content': 'First post test content',
        'date_posted': 'Feb, 5th'
    },
    {
        'author':'TestUsername',
        'title':'Flask Blog post',
        'content': 'Second post test content',
        'date_posted': 'Feb, 5th'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account create! Try login now' , 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title='Login', form= form)
