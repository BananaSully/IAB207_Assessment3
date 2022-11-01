from flask import Blueprint, render_template, request, redirect,url_for
from .models import Events 

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = Events.query.all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        destinations = Events.query.filter(Events.description.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))