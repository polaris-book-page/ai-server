import os
from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import numpy as np

load_dotenv()

def load_data():
    try:
        # mongoDB 연결
        uri = os.getenv("MONGO_URI")
        client = MongoClient(uri)

        # db 연결
        database = client.test

        collections = database.list_collection_names()

        #print(collections)
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
        #print(res_book)

        df_book = pd.DataFrame(res_book)
        df_review = pd.DataFrame(res_review)
        df_book.to_csv('./data/book.csv', encoding='utf-8-sig')
        df_review.to_csv('./data/review.csv', encoding='utf-8-sig')

        # end example code here
        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

def preprocessing():
    raw_book = pd.read_csv('data/book.csv')
    raw_review = pd.read_csv('data/review.csv')

    df_book = pd.DataFrame(raw_book)
    df_review = pd.DataFrame(raw_review)

    #print("print(df_book): ", df_book)
    #print("print(df_review): ", df_review)

    # book preprocess
    cond_one = len(df_book.isbn) == 13
    cond_tow = df_book.title != np.nan
    cond_three = df_book.category != np.nan
    cond_four = df_book.field != np.nan

    df_book = df_book[cond_one & cond_tow & cond_three & cond_four]
    #print(len(df_book))

    # review preprocess
    df_review = df_review[df_review.evaluation != np.nan] # evaluation이 not null인 것만 추출
    #print(len(df_review))



if __name__ == '__main__':
    # load data
    load_data()

    # preprocessing
    preprocessing()