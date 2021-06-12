import pymongo
import json

def db_all(users):
    db_list = []
    for x in users.find():
        data = str(x).replace("ObjectID(","")
        data = data.replace(")","")
        data = data.replace("","")
        data = data.replace('"data":"{','')
        data = data.replace('}"','')
        db_list.append(json.loads(data))
    return db_list

def main(host_ip):
    db_add = "mongodb://192.168.0.45:27018/"
    myclient = pymongo.MongoClient(db_add)
    mydb = myclient["mydatabase"]
    users = mydb["key"]
    return db_all(users)
