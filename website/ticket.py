"""
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Ticket
from .forms import TicketForm
from . import db, app
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('ticket', __name__, url_prefix='/destination')

@bp.route('/<id>', methods = ['GET', 'POST'])
@login_required
def create(id):
  print('Method type: ', request.method)
  form = TicketForm()
  tickets = Ticket.query.filter_by(id=id).first()
  if form.validate_on_submit():
    #call the function that checks and returns image
    ticket=Ticket(id=form.id.data,total=form.total.data,user=current_user)

    #id = request.form['id']
    #total = request.form['total']
    #user = request.form['current']
    # add the object to the db session
    db.session.add(ticket)
    # commit to the database
    db.session.commit()
    print('Successfully created new ticket', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('ticket.show', id=ticket))
  #return render_template('ticket/show.html', form=form, ticket=ticket, tickets=tickets)
"""