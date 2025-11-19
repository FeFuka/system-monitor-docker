import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
	conn = psycopg2.connect(
		host = os.environ['DB_HOST'],
		database = os.environ['DB_NAME'],
		user = os.environ['DB_USER'],
		password = os.environ['DB_PASS']
	)
	return conn

@app.route('/')
def status():
	try:
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute('SELECT version();')
		db_version = cur.fetchone()
		cur.close()
		conn.close()
		return jsonify({"status": "Online", "database": db_version[0]})
	except Exception as e:
		return jsonify({"status": "Erro", "details": str(e)})

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5000)
