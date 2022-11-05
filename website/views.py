from flask import Blueprint, render_template, request, redirect,url_for, flash
from .models import Destination 
from . import db, app

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = Destination.query.all()    
    return render_template('index.html', destinations=destinations)


@mainbp.route('/Options')
def Options():
    if request.args['Options']:
        print(request.args['Options'])
        dest = "%" + request.args['Options'] + '%'
        destinations = Destination.query.filter(Destination.genre.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
    
    
@mainbp.route('/Status')
def Status():
    if request.args['Status']:
        print(request.args['Status'])
        dest = "%" + request.args['Status'] + '%'
        destinations = Destination.query.filter(Destination.status.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
    
    
@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        destinations = Destination.query.filter(Destination.name.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
    
@mainbp.route('/delete/<int:id>')
def delete_result(id):
    event_to_delete = Destination.query.get(id)
    db.session.delete(event_to_delete)
    db.session.commit()
    return render_template('index.html')
    
    