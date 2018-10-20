from app import app, db
from flask import jsonify, request, redirect
import json
import requests
from flask_login import current_user, login_user, logout_user, login_required
from flask_jwt_extended import create_access_token, jwt_required
from app.models import User


# =============
#     AUTH
# =============
@app.route('/register', methods=['POST'])
def register():
    jsonData = json.loads(request.data.decode('utf-8'))

    user = User(username=jsonData['username'])
    user.set_password(jsonData['password'])
    
    db.session.add(user)
    db.session.commit()

    return 'register'

@app.route('/login', methods=['POST'])
def login():    
    if current_user.is_authenticated:
        return redirect('/api/popular')
        
    jsonData = json.loads(request.data.decode('utf-8'))  
    print(jsonData)       
    user = User.query.filter_by(username=jsonData['username']).first()
    if user is None or not user.check_password(jsonData['password']):
        print('invalid')
        return 'invalid'
    access_token = create_access_token(identity=user.username)
    jwtData = json.dumps({"access_token" :access_token})

    return jwtData

@app.route('/logout')
def logout():
    logout_user()

    return 'logged out'

@app.route('/api/popular')
@jwt_required
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
@jwt_required
def best():
    res = requests.get(
        'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json?api-key={0}'
        .format(app.config['API_KEY']))
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    bestData = jsonify(res.json())
    return bestData


@app.route('/api/archives/<year>/<month>')
@jwt_required
def archives(month, year):
    print(month)
    res = requests.get(
        'https://api.nytimes.com/svc/archive/v1/{0}/{1}.json?api-key={2}'.
        format(year, month, app.config['API_KEY']))
    if res.status_code != 200:
        errData = {'status': res.status_code, 'error': 'There was an error'}
        return jsonify(errData), res.status_code

    archivesData = jsonify(res.json())
    return archivesData
