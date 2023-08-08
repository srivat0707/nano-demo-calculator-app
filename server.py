from flask import Flask,request
import json

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    a=int((request.get_json().get("first")))
    b=int((request.get_json().get("second")))
    # hold=request.args.get("first")
    # print(hold,type(hold))
    return json.dumps({"result":a+b})
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    a=int((request.get_json().get("first")))
    b=int((request.get_json().get("second")))
    # hold=request.args.get("first")
    # print(hold,type(hold))
    return json.dumps({"result":a-b})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
