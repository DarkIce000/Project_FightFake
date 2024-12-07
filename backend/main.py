from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from gemini_analysis import askGemini

# instance of flask application
app = Flask(__name__)
CORS(app)

@app.route("/analyse/gemini/", methods=["POST"])
def serve():
    result = askGemini(request.data)
    return jsonify(result)

if __name__ == '__main__':  
   app.run() 