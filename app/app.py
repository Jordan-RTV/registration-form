from flask import Flask, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(
        username=data['username'],
        password=generate_password_hash(data['password']),
        email=data['email'],
        display_name=data['display_name']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
