from flask import make_response, jsonify
from model import models

def get_user_logic():
    users = models.User.get_user_list()
    user_schema = models.UserSchema(many=True)
    return make_response(jsonify({
        'code': 200,
        'users': user_schema.dump(users)
    }))