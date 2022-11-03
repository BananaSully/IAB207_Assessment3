from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField,TextAreaField,SubmitField,PasswordField,DateField,SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.validators import (DataRequired,Email,EqualTo,Length,URL)

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#Create new event
class DestinationForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired()])
  venue = StringField('Venue', validators=[InputRequired()])
  genre = SelectField('Music Genre',[DataRequired()],choices=[('Rock'),('Pop'),('Jazz'),('Hip-Pop'),('Metal'),('Classical'),('EDM')])
  #genre = StringField('Music Genre', validators=[InputRequired()])
  ticketPrice = StringField('Ticket Price', validators=[InputRequired()])
  overview = TextAreaField('Overview', 
  validators=[InputRequired()])
  description = TextAreaField('Description', 
  validators=[InputRequired()])
  status = SelectField('Status',[DataRequired()],choices=[('Upcoming'),('Open'),('Sold-out'),('Cancelled'),('Active'),])
  #status = StringField('Status', validators=[InputRequired()])
  image = FileField('Upload Cover Image', validators=[
  FileRequired(message='Image cannot be empty'),
  FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  
  
  
  submit = SubmitField("Create")


class Tickets(FlaskForm):
  number = StringField('Venue', validators=[InputRequired()])
  total = StringField('Music Genre', validators=[InputRequired()])
  ticketPrice = StringField('Ticket Price', validators=[InputRequired()])
  overview = TextAreaField('Overview', 
  validators=[InputRequired()])
  description = TextAreaField('Description', 
  validators=[InputRequired()])
  status = StringField('Status', validators=[InputRequired()])
  image = FileField('Upload Cover Image', validators=[
  FileRequired(message='Image cannot be empty'),
  FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])

submit = SubmitField("Create")
    
#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Submit')