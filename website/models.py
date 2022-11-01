from email.policy import default
from msilib import datasizemask
from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


class purchasedTickets(db.Model):  
    user_id = db.Column(db.Integer)
    event_id = db.Column(db.Integer)
    numPurchasedTickets = db.Column(db.Integer)

    
#Might need:
#class Tickets(db.Model):
#   __tablename__ = 'tickets'
    

class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    eventName = db.Column(db.String(80))
    description = db.Column(db.String(200))
    venueLocation = db.Column(db.String(100))
    Genre = db.Column(db.String(50))
    startTime = db.Column(db.Datetime, default=datetime.t())
    endTime = db.Column(db.Datetime, default=datetime())
    startDate = db.Column(db.Datetime, default=datetime())
    endDate = db.Column(db.Datetime, default=datetime())
    ticketPrice = db.Column(db.Integer)
    numTicket = db.Column(db.Integer)
    overview = db.Column(db.String(50))
    coverImage = db.Column(db.String(400))
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
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))


    def __repr__(self):
        return "<Comment: {}>".format(self.text)


