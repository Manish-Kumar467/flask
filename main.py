from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000)
