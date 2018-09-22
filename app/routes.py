from app import app, db
from flask import jsonify, request, redirect
import requests
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


# =============
#     AUTH
# =============
@app.route('/register', methods=['GET', 'POST'])
def register():
    user = User(username=request.form['username'], email=request.form['email'])
    user.set_password(request.form['password'])
    db.session.add(user)
    db.session.commit()

    print(request.form['username'])

    return 'register'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/api/popular')

    user = User.query.filter_by(username=request.form['username']).first()
    if user is None or not user.check_password(request.form['password']):
        return 'invalid'
    login_user(user, remember=request.form['remember_me'])
    return redirect('/api/popular')

@app.route('/logout')
def logout():
    logout_user()
    return 'logged out'


@app.route('/api/popular')
@login_required
def popular():
    res = requests.get(
        'https://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/1.json?api-key={0}'
        .format(app.config['API_KEY']))
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    popularData = jsonify(res.json())
    return popularData


@app.route('/api/best')
@login_required
def best():
    res = requests.get(
        'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json?api-key={0}'
        .format(app.config['API_KEY']))
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    bestData = jsonify(res.json())
    return bestData


@app.route('/api/archives/<month>/<year>')
@login_required
def archives(month, year):
    res = requests.get(
        'https://api.nytimes.com/svc/archive/v1/{0}/{1}.json?api-key={2}'.
        format(month, year, app.config['API_KEY']))
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    archivesData = jsonify(res.json())
    return archivesData
