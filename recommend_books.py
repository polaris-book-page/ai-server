from flask_restx import Resource, Namespace
from flask import request, jsonify, Response


RecommendBooks = Namespace('RecommendBooks')


@RecommendBooks.route('/')
class RecommendBook(Resource):
    def post(self):

        result = "test!";
        return jsonify({"result" : result})