from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)

# 設定資料庫連線字串（從環境變數讀取）
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)


# 建立一個 User 模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


# API 1
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


# API 2
class aaa(Resource):
    def get(self):
        return {'message': 'Hello, World!222'}


# API 3: 新增一個使用者
class AddUser(Resource):
    def get(self):
        user = User(name='TestUser')
        db.session.add(user)
        db.session.commit()
        return {'message': f'User {user.name} added, id: {user.id}'}


# API 4: 查詢所有使用者
class GetUsers(Resource):
    def get(self):
        users = User.query.all()
        return {'users': [u.name for u in users]}


# 註冊 API
api.add_resource(HelloWorld, '/')
api.add_resource(aaa, '/aaa')
api.add_resource(AddUser, '/add_user')
api.add_resource(GetUsers, '/get_users')


# 初始化資料庫（只需執行一次）
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run()
