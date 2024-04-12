
# from flask import Flask, Blueprint, render_template, redirect, url_for
# from .auth import bp as auth_bp

# # Create a Flask application instance
# app = Flask(__name__)

# # Create a Blueprint for routes
# bp = Blueprint('main', __name__)


# # Register the blueprint from auth.py
# app.register_blueprint(auth_bp)

# @bp.route("/")
# def index():
#     # Redirect to the login page
#     return redirect(url_for('main.login'))

# # Define the route for the login page
# @bp.route("/login")
# def login():
#     return render_template('login.html')
# # Define the route for the register page



# # @bp.route('/register',  methods=['POST'])
# # def register():
# #     return render_template('register.html')
# # # Define the route for the dashboard page
# @bp.route("/dashboard")
# def dashboard():
#     return render_template('dashboard.html')

# # Define the route for the repositories page
# @bp.route("/repositories")
# def repositories():
#     return render_template('repositories.html')


# # Register the Blueprint with the app
# app.register_blueprint(bp)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, Blueprint, render_template, redirect, url_for
from .auth import bp as auth_bp

# Create a Flask application instance
app = Flask(__name__)

# Create a Blueprint for routes
bp = Blueprint('main', __name__)

# Register the blueprint from auth.py
bp.register_blueprint(auth_bp)

@bp.route("/")
def index():
    # Redirect to the login page
    return redirect(url_for('main.login'))

# Define the route for the login page

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')
# Define the route for the dashboard page
@bp.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

# Define the route for the repositories page
@bp.route("/repositories")
def repositories():
    return render_template('repositories.html')

# Register the Blueprint with the app
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
