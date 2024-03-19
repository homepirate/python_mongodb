import pymongo
from pymongo import MongoClient

import datetime


# client = MongoClient("localhost", 27017)
client = MongoClient("mongodb://localhost:27017/")
db = client["test"]
collection = db["test"]


def ins_one():
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    print(collection.insert_one(post).inserted_id)


def ins_many():

    data = [{
            "name": "Ivan",
            "birthday": datetime.datetime.now()
        },
        {
            "name": "Nikolay",
            "birthday": datetime.datetime.now()
        },
        {
            "name": "Petr",
            "birthday": datetime.datetime.now(),
            "status": True,
        },
    ]

    collection.insert_many(data)


def ins_custom_id():
    data = {"_id": 1,
            "name": "TestID"
            }
    collection.insert_one(data)


def find_by_status():
    res = collection.find({"status": True})
    print("Method find", res)
    print("Method find", res[0])
    for r in res:
        print(r)

    res2 = collection.find_one({"status": True})
    print("Method findOne", res2)


def find_without_id():
    res = collection.find_one({"status": True}, {"_id": 0})
    print(res)


def find_with_select_field():
    res = collection.find_one({"status": True}, {"_id": 0, "name": 1})
    print(res)


def find_by_first_letter():
    res = collection.find({"name": {"$regex": "Pe*"}})
    for r in res:
        print(r)


def find_sort():
    res = collection.find().sort("name", 1) # -1 убывание
    for r in res:
        print(r)


def find_limit():
    res = collection.find({"name": "Ivan"}).limit(2)
    for r in res:
        print(r)


def count_docs():
    res = collection.count_documents({})
    print(res)
    res = collection.count_documents({"name": "Petr"})
    print(res)


def get_collection_names():
    res = db.list_collection_names()
    print(res)


def drop_coll():
    collection.drop()


def add_meny():
    for i in range(10, 30):
        collection.insert_one({"_id": i, "name": f"test_{i}"})


def update_one():
    current = {"name": "test_12"}
    new = {"$set": {"name": "new_12"}}
    collection.update_one(current, new)


def update_many():
    current = {"name": {"$regex": "test_"}}
    new = {"$set": {"name": "based"}}
    collection.update_many(current, new)


def incr():
    collection.insert_one({"_id": 123, "name": f"test_inc", "balance": 100})
    current = {"_id": 123}
    new = {"$inc": {"balance": +200}}
    collection.update_one(current, new)


def delete_by_id():
    collection.delete_one({"_id": 100})


def del_many():
    collection.delete_many({"name": {"$regex": "base"}})


def index():
    # for i in range(1000, 1500):
    #     user = {
    #         "login": f"name_{i}",
    #         "password": f"passwd_{i}",
    #         "date": datetime.datetime.now(tz=datetime.timezone.utc),
    #     }
    #     collection.insert_one(user)

    # print(collection.index_information())
    collection.create_index([("login", pymongo.DESCENDING)])
    # collection.create_index([("login", pymongo.DESCENDING)], unique=True)  #unique=True чтоб все login`ы бвли уникальными
    # collection.drop_index('login_-1')
    print(collection.index_information())


def main():
    # ins_many()
    # ins_custom_id()
    # find_by_status()
    # find_without_id()
    # find_with_select_field()
    # find_by_first_letter()
    # find_sort()
    # find_limit()
    # count_docs()
    # get_collection_names()
    # add_meny()
    # update_one()
    # update_many()
    # incr()
    # delete_by_id()
    # del_many()
    index()


if __name__ == '__main__':
    main()
