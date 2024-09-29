from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)

if __name__ == '__main__':
  app.run(port=5000)
