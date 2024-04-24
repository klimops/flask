from flask import Flask, request, jsonify, Blueprint, make_response, render_template
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
url = os.getenv('DB_URL')
connection = psycopg2.connect(url)
cursor = connection.cursor()

@app.route("/")
def hello():
    print("Hello")

@app.route("/books", methods=['GET'])
def books():  
    cursor.execute("select * from books")
    result = cursor.fetchall()
    return result
    

@app.route("/create", methods=['POST'])
def insert_books():
    name_autor = 'vini' # request.form.get("name_autor")
    name_book = 'anime' # request.form.get("name_book")
    cursor.execute("insert into books (nome_autor, nome_livro) values (%s, %s)", (name_autor, name_book))
    connection.commit()
    return 'Insert Feito'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
