from flask import Flask, request
from flask import jsonify
import json
from flask_cors import CORS
# from gemini_analysis import askGemini
from local_analysis_model import askLocal

# instance of flask application
app = Flask(__name__)
CORS(app)

@app.route("/analyse/gemini/", methods=["POST"])
def serve():
    data = json.loads(request.data)
    print(type(data["data"]))
    print(data["data"])
    result = askLocal(data["data"])
    return jsonify(result)

if __name__ == '__main__':  
   app.run() 