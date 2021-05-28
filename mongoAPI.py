from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from db import CLIENTE

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Kinvo'
app.config['MONGO_URI'] = CLIENTE

mongo = PyMongo(app)

@app.route('/data', methods=['GET'])
def get_last_data():
  debentures = mongo.db.AnbimaSeries
  output = []
  
  for d in debentures.find().sort([('datetime', -1)]).limit(1):
    output.append({'datetime' : d['datetime'], 'value' : d['value']})

  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)