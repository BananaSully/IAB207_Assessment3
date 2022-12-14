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
    destination = db.relationship('Destination', backref='user')
    



class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    venue = db.Column(db.String(80))
    genre = db.Column(db.String(40))
    ticketPrice = db.Column(db.String(5))
    overview = db.Column(db.String(50))
    description = db.Column(db.String(200))
    status = db.Column(db.String(20))
    image = db.Column(db.String(400))
    user_id = db.Column(db.String(3), db.ForeignKey('users.id'))
    
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='destination')
    #ticket = db.relationship('Ticket', backref='destination')
    

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer)
    user_id = db.Column(db.String(3), db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer)

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.String, default=datetime.now().strftime('%d %B %Y'))
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)


