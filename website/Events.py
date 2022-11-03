from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment, purchasedTickets
from .forms import EventForm, CommentForm, PurchaseTickets
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('Event', __name__, url_prefix='/Events')

@bp.route('/<id>')
def show(id):
    Event = Events.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('Events/show.html', Event=Event, form=cform)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    Event=Events(name=form.EventName.data,
                description=form.description.data, 
                venue_location=form.venueLocation.data,
                genre=form.musicGenre.data,
                start_time=form.startTime.data,
                end_time=form.endTime.data,
                start_date=form.startDate.data,
                end_date=form.endDate.data,
                ticket_price=form.ticketPrice.data,
                ticket_quantity=form.totalTickets.data,
                overview=form.overview.data,
                image=db_file_path)
    # add the object to the db session
    db.session.add(Event)
    # commit to the database
    db.session.commit()
    print('Successfully created a new Event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('Event.create'))
  return render_template('Events/create.html', form=form)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

@login_required
def Purchase_Tickets(Event):
  print('Method type: ', request.method)
  form = PurchaseTickets()
  if form.validate_on_submit():
    tickets=purchasedTickets(numtickets=form.numofTickets.data,
                             user=current_user)
     # add the object to the db session
    db.session.add(Event)
    # commit to the database
    db.session.commit()
  
    print('Your tickets have be purchased','success')

    return redirect(url_for('Eventpage', id=Event))



@bp.route('/<Event>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(Event):  
    form = CommentForm()  
    #get the Event object associated to the page and the comment
    Event_obj = Events.query.filter_by(id=Event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        Event=Event_obj,
                        user=current_user) 
      #here the back-referencing works - comment.Event is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to event.show
    return redirect(url_for('Event.show', id=Event))
    