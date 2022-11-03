from flask import Blueprint, render_template, request, redirect,url_for
from .models import Destination 

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
<<<<<<< HEAD
    events = Events.query.all()    
    return render_template('index.html', events=events)
=======
    destinations = Destination.query.all()    
    return render_template('index.html', destinations=destinations)
>>>>>>> 50003a1f6372178de38b3e3ff522702aeba37713

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
<<<<<<< HEAD
        event = Events.query.filter(Events.name.like(dest)).all()
        return render_template('index.html', event=event)
=======
        destinations = Destination.query.filter(Destination.description.like(dest)).all()
        return render_template('index.html', destinations=destinations)
>>>>>>> 50003a1f6372178de38b3e3ff522702aeba37713
    else:
        return redirect(url_for('main.index'))