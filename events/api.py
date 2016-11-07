from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'geventator_event'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/geventator_events'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /event to /event/

mongo = PyMongo(app)

@app.route('/event', methods=['GET'])
def get_events():
    events = mongo.db.events
    output = []
    for e in events.find():
        output.append({'_id' : str(ObjectId(e['_id'])), 'name' : e['name'], 'description' : e['description'], 'location' : e['location'], 'start_date' : e['start_date'], 'finish_date' : e['finish_date']})
    return jsonify({'result' : output}), 200

@app.route('/event', methods=['POST'])
def add_event():
    user = '58208f5dcec8de0e27f0ce0e'
    name = request.json['name']
    description = request.json['description']
    location = request.json['location']
    start_date = request.json['start_date']
    finish_date = request.json['finish_date']
    events = mongo.db.events
    event_id = events.insert({'name' : name, 'description' : description, 'location' : location, 'start_date' : start_date, 'finish_date' : finish_date})
    new_event = events.find_one({'_id': event_id })
    organizers = mongo.db.organizers
    organizer_id = organizers.insert({'event' : str(ObjectId(new_event['_id'])), 'user' : user})
    output = {'_id' : str(ObjectId(new_event['_id'])), 'name' : new_event['name'], 'description' : new_event['description'], 'location' : new_event['location'], 'start_date' : new_event['start_date'], 'finish_date' : new_event['finish_date']}
    return jsonify({'result' : output}), 201

@app.route('/event/<event>', methods=['GET'])
def get_event(event):
    events = mongo.db.events
    e = events.find_one({'_id' : ObjectId(event)})
    if e:
        output = {'_id' : str(ObjectId(e['_id'])), 'name' : e['name'], 'description' : e['description'], 'location' : e['location'], 'start_date' : e['start_date'], 'finish_date' : e['finish_date']}
        return jsonify({'result' : output}), 200
    else:
        output = "No such event"
        return jsonify({'result' : output}), 404

@app.route('/event/<event>', methods=['PUT'])
def edit_event(event):
    events = mongo.db.events
    e = events.find_one({'_id' : ObjectId(event)})
    if e:
        name = request.json['name']
        description = request.json['description']
        location = request.json['location']
        start_date = request.json['start_date']
        finish_date = request.json['finish_date']
        e['name'] = name
        e['description'] = description
        e['location'] = location
        e['start_date'] = start_date
        e['finish_date'] = finish_date
        events.save(e)
        output = {'_id' : str(ObjectId(e['_id'])), 'name' : e['name'], 'description' : e['description'], 'location' : e['location'], 'start_date' : e['start_date'], 'finish_date' : e['finish_date']}
        return jsonify({'result' : output}), 200
    else:
        output = "No such event"
        return jsonify({'result' : output}), 404

@app.route('/event/<event>/organizer', methods=['GET'])
def get_organizers(event):
    organizers = mongo.db.organizers
    output = []
    for o in organizers.find({'event' : event}):
        output.append({'event' : o['event'], 'user' : o['user']})
    return jsonify({'result' : output}), 200

@app.route('/event/<event>/organizer/<user>', methods=['POST'])
def add_organizer(event, user):
    organizers = mongo.db.organizers
    organizer_id = organizers.insert({'event' : event, 'user' : user})
    new_organizer = organizers.find_one({'event' : event, 'user' : user})
    output = {'event' : new_organizer['event'], 'user' : new_organizer['user']}
    return jsonify({'result' : output}), 201

@app.route('/event/<event>/organizer/<user>', methods=['DELETE'])
def delete_organizer(event, user):
    organizers = mongo.db.organizers
    o = organizers.find_one({'event' : event, 'user' : user})
    if o:
        output = {'event' : o['event'], 'user' : o['user']}
        organizers.delete_one(o)
        return jsonify({'result' : output}), 200
    else:
        output = "No such event"
        return jsonify({'result' : output}), 404

@app.route('/user/<user>/event', methods=['GET'])
def get_user_events(user):
    organizers = mongo.db.organizers
    output = []
    for o in organizers.find({'user' : user}):
        output.append({'event' : o['event'], 'user' : o['user']})
    return jsonify({'result' : output}), 200

if __name__ == '__main__':
    app.run(debug=True)
