from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RoomForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '57e8728bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#class room(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(20), unique=True, nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #password = db.Column(db.String(60), nullable=False)
    #posts = db.relationship('Post', backref='author', lazy=True)

#    def __repr__(self):
#        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(100), nullable=False)
#    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#    content = db.Column(db.Text, nullable=False)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#    def __repr__(self):
#        return f"Post('{self.title}', '{self.date_posted}')"

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	campusname = db.Column(db.String(10), nullable=False)
	primaryuse = db.Column(db.String(100), nullable=False)
	roomname = db.Column(db.String(100), nullable=False)
	
	def __repr__(self):
		return f"Room('{self.campusname}', '{self.primaryuse}', '{self.roomname}')"

rooms = [
    {
        'campusname': 'khs',
        'primaryuse': 'CTE',
        'roomname': '126'
    },
    {
        'campusname': 'khs',
        'primaryuse': 'CTE',
        'roomname': '129'
    }
]

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/admin")
def admin():
	rooms = Room.query.all()
	return render_template('roomlist.html', rooms=rooms)

@app.route("/khs")
def khs():
	rooms = Room.query.all()
	return render_template('roomlist.html', rooms=rooms)

@app.route("/kms")
def kms():
	rooms= Room.query.all()
	return render_template('roomlist.html', rooms=rooms)

@app.route("/kis")
def kis():
	rooms = Room.query.all()
	return render_template('roomlist.html', rooms=rooms)

@app.route("/kes")
def kes():
	rooms = Room.query.all()
	return render_template('roomlist.html', rooms=rooms)

@app.route("/kps")
def kps():
	rooms = Room.query.all()
	return render_template('roomlist.html', rooms=rooms)
	
if __name__ == '__main__':
    app.run(debug=True)
