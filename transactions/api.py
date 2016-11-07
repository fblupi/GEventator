from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
import datetime

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'geventator_transactions'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/geventator_transactions'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /transaction to /transaction/

mongo = PyMongo(app)

@app.route('/event/<event>/transaction', methods=['GET'])
def get_transactions(event):
    transactions = mongo.db.transactions
    output = []
    for t in transactions.find({'event' : event}):
        output.append({'_id' : str(ObjectId(t['_id'])), 'event': t['event'], 'concept' : t['concept'], 'description' : t['description'], 'quantity' : t['quantity'], 'price' : t['price'], 'kind' : t['kind'], 'date' : t['date']})
    return jsonify({'result' : output}), 200

@app.route('/event/<event>/transaction', methods=['POST'])
def add_transaction(event):
    concept = request.json['concept']
    description = request.json['description']
    quantity = request.json['quantity']
    price = request.json['price']
    kind = request.json['kind'] # deposit, expense
    if kind != "deposit" and kind != "expense" and kind != "investment":
        output = "Invalid kind of transaction"
        return jsonify({'result' : output}), 400
    elif quantity < 1:
        output = "Invalid quantity"
        return jsonify({'result' : output}), 400
    else:
        if kind == "deposit":
            price = abs(price)
        else:
            price = abs(price) * -1
        transactions = mongo.db.transactions
        transaction_id = transactions.insert({'event' : event, 'concept' : concept, 'description' : description, 'quantity' : quantity, 'price' : price, 'kind' : kind, 'date' : datetime.datetime.utcnow()})
        new_transaction = transactions.find_one({'_id': transaction_id })
        output = {'_id' : str(ObjectId(new_transaction['_id'])), 'event' : new_transaction['event'], 'concept' : new_transaction['concept'], 'description' : new_transaction['description'], 'quantity' : new_transaction['quantity'], 'price' : new_transaction['price'], 'kind' : new_transaction['kind'], 'date' : new_transaction['date']}
        return jsonify({'result' : output}), 201

@app.route('/event/<event>/transaction/<transaction>', methods=['GET'])
def get_transaction(event, transaction):
    transactions = mongo.db.transactions
    t = transactions.find_one({'_id' : ObjectId(transaction)})
    if t:
        output = {'_id' : str(ObjectId(t['_id'])), 'event': t['event'], 'concept' : t['concept'], 'description' : t['description'], 'quantity' : t['quantity'], 'price' : t['price'], 'kind' : t['kind'], 'date' : t['date']}
        return jsonify({'result' : output}), 200
    else:
        output = "No such transaction"
        return jsonify({'result' : output}), 404

@app.route('/event/<event>/transaction/<transaction>', methods=['DELETE'])
def delete_transaction(event, transaction):
    transactions = mongo.db.transactions
    t = transactions.find_one({'_id' : ObjectId(transaction)})
    if t:
        output = {'_id' : str(ObjectId(t['_id'])), 'event' : t['event'], 'concept' : t['concept'], 'description' : t['description'], 'quantity' : t['quantity'], 'price' : t['price'], 'kind' : t['kind'], 'date' : t['date']}
        transactions.delete_one(t)
        return jsonify({'result' : output}), 200
    else:
        output = "No such transaction"
        return jsonify({'result' : output}), 404

if __name__ == '__main__':
    app.run(debug=True)
