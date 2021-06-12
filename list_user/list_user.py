from flask import Flask, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pymongo
import json
import sys
#import database1
import pika
import logging
import warnings
import bcrypt

# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

# setup flask app
app = Flask(__name__)

# setup swagger online document
swagger = Swagger(app)

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning)

@app.route('/listuser',methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def listuser():
    myclient = pymongo.MongoClient("mongodb://192.168.0.45:27018/")
    #db_add = "mongodb://192.168.0.45:27018/"
    mydb = myclient["mydatabase"]
    users = mydb["key"]

    db_list = []
    for x in users.find({},{"Password" : 0, "Own" : 0 , "Debt" : 0 }):
        data = str(x).replace("ObjectId(","")
        data = data.replace(")","")
        data = data.replace("'",'"')
        data = data.replace('"data": "{','')
        data = data.replace('}"','')
        db_list.append(json.loads(data))

    return json.dumps(db_list)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
