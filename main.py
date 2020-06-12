from flask import request, make_response , redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user



import unittest
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos


app = create_app()

#todos = ['Comprar Cafe 1', 'Enviar solicitud de compra 2', 'Enviar Producto 3']


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello(): 
    
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    #login_form = LoginForm()
    username = current_user.id 

    #return 'HelLo World Platzi , tu ip es {} '.format(user_ip)
    context  = {
            'user_ip':  user_ip,
            'todos' : get_todos(user_id=username),
            #'login_form': login_form,
            'username': username,
    }


    


    return render_template('hello.html', **context)
