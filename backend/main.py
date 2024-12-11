from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from gemini_analysis import askGemini
from local_analysis_model import askLocal

# instance of flask application
app = Flask(__name__)
CORS(app)

@app.route("/analyse/gemini/", methods=["POST"])
def serve():
    print(request.data)
    # result = askGemini(request.data)
    return request.data

if __name__ == '__main__':  
   app.run() 