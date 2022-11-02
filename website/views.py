from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events 

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    events = Events.query.all()    
    return render_template('index.html', events=events)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        event = Events.query.filter(Events.description.like(dest)).all()
        return render_template('index.html', event=event)
    else:
        return redirect(url_for('main.index'))