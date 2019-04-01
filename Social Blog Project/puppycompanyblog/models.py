# models.py

from puppycompanyblog import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash #segurança
from flask_login import UserMixin
from datetime import datetime

# importação do __init__.py para verificar se o user existe, está logado etc
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# criando as tabelas do DB
class User(db.Model,UserMixin):

    # criando a tabela users
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    # nomeando a relação user/postagem
    posts = db.relationship('BlogPost', backref='author',lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # encriptando a senha do user
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"


class BlogPost(db.Model):

	# criando a tabela de postagens

	# relacionando a postagem ao user
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    # FK da relação com user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
