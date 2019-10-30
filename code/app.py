from flask import Flask
from flask_restful import Api
from flask_jwt import  JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import  Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'#postgresql,mysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

from db import db
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
