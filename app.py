from flask import Flask, request, jsonify, render_template
import psycopg2
from main import add_user
from config import host, user as db_user, password, db_name

app = Flask(__name__)

@app.route('/')
def serve_registration_page():
    return render_template('index.html')

@app.route('/register_page')
def register_registration():
    return render_template('register1.html')


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(f"Received username: {username}, password: {password}")
    add_user(username, password)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
    
    

            
