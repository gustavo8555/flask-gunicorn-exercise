from flask import Flask, Response, request
from db.database import initialize_db
from db.models import User 
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://root:example@mongodb:27017/super_users'
        }

initialize_db(app)

@app.route("/users")
def get_users():
    users = User.objects().to_json()
    return Response(users, mimetype="application/json", status=200)

@app.route("/users", methods=['POST'])
def add_user():
    body = request.get_json()
    user = User(**body).save()
    email = user.email
    return {'email': str(email)}, 200

@app.route("/users/<email>", methods=['DELETE'])
def delete_user(email):
    User.objects.get(email=email).delete()
    return '', 200
