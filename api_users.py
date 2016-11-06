from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import hashlib

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'geventator_users'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/geventator_users'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /user to /user/

mongo = PyMongo(app)

@app.route('/user', methods=['GET'])
def get_all_users():
    users = mongo.db.users
    output = []
    for u in users.find():
        output.append({'username' : u['username'], 'email' : u['email'], 'name' : u['name']})
    return jsonify({'result' : output})

@app.route('/user/<username>', methods=['GET'])
def get_one_user(username):
    users = mongo.db.users
    u = users.find_one({'username' : username})
    if u:
        output = {'username' : u['username'], 'email' : u['email'], 'name' : u['name']}
    else:
        output = "No such username"
    return jsonify({'result' : output})

@app.route('/user/<username>', methods=['POST'])
def edit_one_user(username):
    users = mongo.db.users
    u = users.find_one({'username' : username})
    if u:
        username = request.json['username']
        email = request.json['email']
        name = request.json['name']
        password = hashlib.md5(request.json['password'].encode('utf-8')).hexdigest()
        u1 = users.find_one({'username' : username})
        u2 = users.find_one({'email' : email})
        if u1 and u1 != u:
            output = "Already a user with that username"
        elif u2 and u2 != u:
            output = "Already a user with that email"
        else:
            u['username'] = username
            u['email'] = email
            u['name'] = name
            u['password'] = password
            users.save(u)
            output = {'username' : u['username'], 'email' : u['email'], 'name' : u['name']}
    else:
        output = "No such username"
    return jsonify({'result' : output})

@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    name = request.json['name']
    password = hashlib.md5(request.json['password'].encode('utf-8')).hexdigest()
    users = mongo.db.users
    u1 = users.find_one({'username' : username})
    u2 = users.find_one({'email' : email})
    if u1:
        output = "Already a user with that username"
    elif u2:
        output = "Already a user with that email"
    else:
        user_id = users.insert({'username' : username, 'email' : email, 'name' : name, 'password' : password})
        new_user = users.find_one({'_id': user_id })
        output = {'username' : new_user['username'], 'email' : new_user['email'], 'name' : new_user['name']}
    return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
