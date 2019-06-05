from flask import Flask,request
from components import auth

app = Flask(__name__)
authObj = auth.Auth()

@app.route('/auth',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return authObj.auth(request.values['username'],request.values['password'])


@app.route('/register',methods=['POST'])
def register():
    response = app.response_class(
        response = authObj.register(request.values['username'],request.values['password']),
        status = 200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
