from . import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class Customer(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)



    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')
    

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password=password)

    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)
    

    def __str__(self):
        return '<Customer %r' % Customer.id
    


class Products(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    product_name = db.Column(db.string(100),nullable=False)
    current_price = db.Column(db.string(100),nullable=False)
    previous_price = db.Column(db.string(100),nullable=False)
    in_stock = db.Column(db.string(100),nullable=False)
    product_picture = db.Column(db.string(100),nullable=False)
    flash_sale = db.Column(db.Boolean, default=True)

