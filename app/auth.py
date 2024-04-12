# from flask import Blueprint, request, jsonify
# from flask_bcrypt import Bcrypt
# import jwt
# import datetime
# from pymongo.errors import DuplicateKeyError  # Import the DuplicateKeyError exception
# from .usermodel import User

# bp = Blueprint('auth', __name__)
# bcrypt = Bcrypt()


# @bp.route('/registers', methods=['POST'])
# def registers():
#     data = request.json
#     role = data.get('role')
#     username = data.get('username')
#     password = data.get('password')
#     email = data.get('email')
#     address = data.get('address')
#     phone = data.get('phone')

#     # Check if all required fields are provided
#     if not all([role, username, password]):
#         return jsonify({'message': 'Missing required fields'}), 400

#     # Hash the password
#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

#     try:
#         # Attempt to create the user
#         user = User(role=role, username=username, email=email, password=hashed_password, address=address, phone=phone)
#         user.save()
#     except DuplicateKeyError:
#         # Handle the case when a duplicate username is detected
#         return jsonify({'message': 'Username already exists'}), 409
#     except Exception as e:
#         # Handle any other exceptions that may occur during user creation
#         return jsonify({'message': f'Error creating user: {str(e)}'}), 500

#     return jsonify({'message': 'User registered successfully'})


# @bp.route('/login', methods=['POST'])
# def login():
#     auth = request.json

#     user = User.objects(username=auth['identifier']).first()

#     if not user or not bcrypt.check_password_hash(user.password, auth['password']):
#         return jsonify({'message': 'Invalid credentials'}), 401

#     token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, bp.config['SECRET_KEY'])

#     return jsonify({'token': token.decode('UTF-8')})

# # @bp.route('/users/<username>', methods=['GET'])
# # def get_user(username):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return jsonify({'message': 'User not found'}), 404

# #     # Return user data
# #     return jsonify({
# #         'username': user.username,
# #         'email': user.email,
# #         'role': user.role,
# #         'address': user.address,
# #         'phone': user.phone
# #     })

# # if __name__ == '__main__':
# #     bp.run(debug=True)

# @bp.route('/users/<username>', methods=['GET'])
# def get_user(username):
#     user = User.objects(username=username).first()
#     if not user:
#         return jsonify({'message': 'User not found'}), 404

#     # Return user data
#     return jsonify({
#         'username': user.username,
#         'email': user.email,
#         'role': user.role,
#         'address': user.address,
#         'phone': user.phone
#     })


import logging
from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from pymongo.errors import DuplicateKeyError
from .usermodel import User

bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@bp.route('/registers', methods=['POST'])
def registers():
    data = request.json
    role = data.get('role')
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    address = data.get('address')
    phone = data.get('phone')

    # Log received data
    logger.debug(f'Received data: {data}')

    # Check if all required fields are provided
    if not all([role, username, password]):
        return jsonify({'message': 'Missing required fields'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        # Attempt to create the user
        user = User(role=role, username=username, email=email, password=hashed_password, address=address, phone=phone)
        user.save()

        # Log successful user registration
        logger.info('User registered successfully')
    except DuplicateKeyError:
        # Handle the case when a duplicate username is detected
        return jsonify({'message': 'Username already exists'}), 409
    except Exception as e:
        # Log error during user creation
        logger.error(f'Error creating user: {str(e)}')

        # Handle any other exceptions that may occur during user creation
        return jsonify({'message': f'Error creating user: {str(e)}'}), 500

    return jsonify({'message': 'User registered successfully'})
