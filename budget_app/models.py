from datetime import datetime
from budget_app import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #budgets = db.relationship('Budget', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', {self.email}"

# class Expense(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     vendor = db.Column(db.String(100), nullable=False)
#     expense_type = db.Column(db.String(50), nullable=False)
#     cost = db.Column(db.Integer, nullable=False)
#     balance_before = db.Column(db.Integer, nullable=False)
#     balance_after = db.Column(db.Integer, nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     def __repr__(self):
#         return f"User('{self.username}', {self.email}"


# class Budget(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String(100), nullable=False)
#     budget_id = db.Column(db.Text, nullable=False)
#     amount = 
#     category = 
#     description = 
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) 

#     def __repr__(self):
#         return f"User('{self.username}', {self.email}"
