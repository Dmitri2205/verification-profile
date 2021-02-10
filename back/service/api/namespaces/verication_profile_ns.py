from flask import request
from flask_restx import Resource, Namespace
from service.api.repo.verification_profile import PROFILES, remove_profile

api = Namespace('verification-profile', description='verification profile users')


@api.route('/get-data')
class GetProfile(Resource):
    @api.doc('get profile')
    def get(self):
        data = PROFILES
        return {"data": data}, 200


@api.route('/verification')
class GetProfile(Resource):
    @api.doc('verification user')
    def post(self):
        param = request.json
        user_id = int(param['user_id'])
        remove_profile(user_id)
        return {"error": 0, "status": "ok"}, 200


@api.route('/cancel-verification')
class GetProfile(Resource):
    @api.doc('verification user')
    def post(self):
        param = request.json
        user_id = int(param['user_id'])
        remove_profile(user_id)
        return {"error": 0, "status": "ok"}, 200


@api.route('/ban-acc')
class GetProfile(Resource):
    @api.doc('ban user')
    def post(self):
        param = request.json
        user_id = int(param['user_id'])
        remove_profile(user_id)
        return {"error": 0, "status": "ok"}, 200


@api.route('/ban-dev')
class GetProfile(Resource):
    @api.doc('ban device')
    def post(self):
        param = request.json
        user_id = int(param['user_id'])
        remove_profile(user_id)
        return {"error": 0, "status": "ok"}, 200
