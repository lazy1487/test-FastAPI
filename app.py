from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# API 1


class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

# API 2


class aaa(Resource):
    def get(self):
        return {'message': 'Hello, World!222'}


# 註冊兩個 API 路由
api.add_resource(HelloWorld, '/')
api.add_resource(aaa, '/aaa')

if __name__ == '__main__':
    app.run(debug=True)
