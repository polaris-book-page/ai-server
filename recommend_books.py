from flask_restx import Resource, Namespace
from flask import request, jsonify, Response
from mongoDB import recommend

RecommendBooks = Namespace('RecommendBooks')


@RecommendBooks.route('/')
class RecommendBook(Resource):
    def post(self):
        userId = request.json.get('userId')
        recommend_arr = recommend(userId)

        print(recommend_arr)

        return jsonify({"result": recommend_arr})
