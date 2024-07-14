import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

try:
    # mongoDB 연결
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)

    # db 연결
    database = client.test

    collections = database.list_collection_names()

    print(collections)
    coll_review = database["reviews"]
    coll_book = database["books"]

    # start example code here
    proj_review = {
        "content": 1,
        "userId": 1,
        "isbn": 1,
        "evaluation": 1,
        "_id": 0
    }

    proj_book = {
        "title": 1,
        "isbn": 1,
        "writer": 1,
        "category": 1,
        "field": 1,
        "_id": 0
    }

    res_review = list(coll_review.find({}, proj_review))
    #print(res_review)

    res_book = list(coll_book.find({}, proj_book))
    print(res_book)

    # end example code here
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)