from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events 

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    Events = Events.query.all()    
    return render_template('index.html', Events=Events)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        Event = Events.query.filter(Events.name.like(dest)).all()
        return render_template('index.html', Event=Event)
    else:
        return redirect(url_for('main.index'))