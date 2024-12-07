# import flast module
from flask import Flask
from flask import request

# instance of flask application
app = Flask(__name__)

@app.route("/genai/", methods=["POST"])
def hello_world():
    
    return request.args

if __name__ == '__main__':  
   app.run() 