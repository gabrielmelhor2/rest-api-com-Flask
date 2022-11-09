from flask import Flask, jsonify, make_response
from api import blueprint_api

app = Flask(__name__)
app.register_blueprint(blueprint_api)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "URL Nao encontrada!"}))


app.run()
