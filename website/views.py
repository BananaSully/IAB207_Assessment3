from flask import Blueprint, render_template, request, redirect,url_for
from .models import Destination 

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
    
@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        destinations = Destination.query.filter(Destination.name.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
    

    
    