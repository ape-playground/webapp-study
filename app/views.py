from flask import jsonify
from app import app


@app.route("/")
def home():
    return "Flask says 'Hello world!'"


@app.route("/phonebook")
def index():
    return app.send_static_file("phonebook.html")


@app.route("/api/data")
def data():
    d = {"Alice": "(708) 727-2377", "Bob": "(305) 734-0429"}
    app.logger.debug(str(len(d)) + " entries in phonebook")
    return jsonify(d)


@app.route("/resume")
def resume():
    return app.send_static_file("resume.html")
