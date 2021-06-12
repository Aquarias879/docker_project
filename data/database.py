import pymongo

def insert_db(message, db_ip):
    myclient = pymongo.MongoClient("mongodb://"+db_ip+":27017/")
    mydb = myclient["mydatabase"]
    users = mydb["key"]

    my_dict = {"data":message}
    x = users.insert_one(my_dict)
    return x.inserted_id
