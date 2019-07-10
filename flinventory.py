from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RoomForm, ItemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '57e8728bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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
	itemquantity = db.Column(db.Integer,nullable=True)
	roomid = db.Column(db.Integer, db.ForeignKey(Room.id), nullable=False)

	def __repr__(self):
		return f"item('{self.itemtype}', '{self.itemcondition}', '{self.itemnote}','{self.roomid}, {self.itemquantity}')"



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
        item = Item(itemtype=form.itemtype.data, itemcondition=form.itemcondition.data, itemnote=form.itemnote.data, roomid=form.roomid.data, itemquantity=form.itemquantity.data)
        db.session.add(item)
        db.session.commit()
        flash('Item added', 'success')
        return redirect(url_for('home'))
    return render_template('newitem.html', title='New Item',
                           form=form, legend='New Item')

@app.route("/admin")
def admin():
	rooms = Room.query.filter(Room.campusname == "admin")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)

@app.route("/khs")
def khs():
	rooms = Room.query.filter(Room.campusname == "khs")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)

@app.route("/kms")
def kms():
	rooms = Room.query.filter(Room.campusname == "kms")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)

@app.route("/kis")
def kis():
	rooms = Room.query.filter(Room.campusname == "kis")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)

@app.route("/kes")
def kes():
	rooms = Room.query.filter(Room.campusname == "kes")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)

@app.route("/kps")
def kps():
	rooms = Room.query.filter(Room.campusname == "kps")
	items = Item.query.all()
	return render_template('roomlist.html', rooms=rooms, items=items)
	
if __name__ == '__main__':
    app.run(debug=True)
