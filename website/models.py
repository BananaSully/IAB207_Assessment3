from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


<<<<<<< HEAD
class purchasedTickets(db.Model):  
    __tablename__ = "purchasedTickets"
    user_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    numPurchasedTickets = db.Column(db.Integer)


class Events(db.Model):
    __tablename__ = 'events'
=======

class Destination(db.Model):
    __tablename__ = 'destinations'
>>>>>>> 50003a1f6372178de38b3e3ff522702aeba37713
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    venue = db.Column(db.String(80))
    genre = db.Column(db.String(40))
    ticketPrice = db.Column(db.String(5))
    overview = db.Column(db.String(50))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
<<<<<<< HEAD
    # ... Create the Comments db.relationship
	# relation to call Event.comments and comment.Event
    comments = db.relationship('Comment', backref='events')
=======
>>>>>>> 50003a1f6372178de38b3e3ff522702aeba37713
    
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='destination')

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
<<<<<<< HEAD
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
=======
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
>>>>>>> 50003a1f6372178de38b3e3ff522702aeba37713


    def __repr__(self):
        return "<Comment: {}>".format(self.text)


