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
    
@mainbp.route('/edit_or_delete', methods=['POST'])
def edit_or_delete():
    id = request.form['id']
    choice = request.form['choice']
    sock = Destination.query.filter(Destination.id == id).first()
    # two forms in this template
    form1 = AddRecord()
    form2 = DeleteForm()
    return render_template('edit_or_delete.html', sock=sock, form1=form1, form2=form2, choice=choice)

@mainbp.route('/delete_result', methods=['POST'])
def delete_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    sock = Destination.query.filter(Destination.id == id).first()
    if purpose == 'delete':
        db.session.delete(Destination)
        db.session.commit()
        message = f"The sock {Destination.name} has been deleted from the database."
        return render_template('result.html', message=message)
    else:
        abort(405)
    