from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RoomForm, ItemForm

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
	items = db.relationship('Item', backref='roomname', lazy=True)
	
	def __repr__(self):
		return f"Room('{self.campusname}', '{self.primaryuse}', '{self.roomname}', '{self.id}')"

class Item(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	itemtype = db.Column(db.String(100), nullable=False)
	itemcondition = db.Column(db.Integer, nullable=False)
	itemnote = db.Column(db.String(300),nullable=True)
	roomid = db.Column(db.Integer, db.ForeignKey(Room.id), nullable=False)

	def __repr__(self):
		return f"item('{self.itemtype}', '{self.itemcondition}', '{self.itemnote}','{self.roomid}')"



@app.route("/")
def home():
    return render_template('main.html')

@app.route("/newroom", methods=['GET', 'POST'])
def new_room():
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(campusname=form.campusname.data, roomname=form.roomname.data, primaryuse=form.primaryuse.data)
        db.session.add(room)
        db.session.commit()
        flash('Room added', 'success')
        return redirect(url_for('home'))
    return render_template('newroom.html', title='New Room',
                           form=form, legend='New Room')

@app.route("/newitem", methods=['GET', 'POST'])
def new_item():
    form = ItemForm(roomid=request.args.get('roomid'))
    if form.validate_on_submit():
        item = Item(itemtype=form.itemtype.data, itemcondition=form.itemcondition.data, itemnote=form.itemnote.data, roomid=form.roomid.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added', 'success')
        return redirect(url_for('home'))
    return render_template('newitem.html', title='New Item',
                           form=form, legend='New Item')

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
