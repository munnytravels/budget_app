from flask import render_template, request, redirect, url_for, flash
from budget_app import app, db, bcrypt
from budget_app.forms import RegistrationForm, LoginForm
from budget_app.models import User, Budget 

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# @app.route('/posts', methods=['GET', 'POST'])
# def posts():

#     if request.method == 'POST': 
#         budget_expense = request.form['expense']
#         budget_type = request.form['type']
#         budget_before = request.form['before']
#         budget_after = request.form['after']

#         new_budget = Budget(expense=budget_expense,budget_type=type, before=budget_before, after=budget_after)
#         db.session.add(new_post) 
#         db.session.commit() 
#         return redirect('/posts')
#     else:
#         all_posts = Budget.query.order_by(Budget.date_posted).all()
#         return render_template('posts.html', posts=all_posts) 


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
