from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

# @app.route('/')
# def serve_registration_page():
#     return render_template('index.html')

# @app.route('/register_page')
# def register_registration():
#     return render_template('register1.html')


# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']
#     print(f"Received username: {username}, password: {password}")
#     add_user(username, password)
#     return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
    
    

            
