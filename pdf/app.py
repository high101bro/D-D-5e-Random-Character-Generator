#! /usr/bin/env python3

from flask import Flask, render_template, jsonify, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/character-data')
def character_data():
    with open('sheet.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
