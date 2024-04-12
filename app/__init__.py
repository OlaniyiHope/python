
# # import redis
# # from flask import Flask
# # from app.utils import make_celery
# # from config import Config
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_migrate import Migrate

# # app = Flask(__name__, static_url_path='/static')
# # app.config.from_object(Config)
# # db = SQLAlchemy(app)
# # migrate = Migrate(app, db)

# # # connect to Redis instance
# # redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
# #                              port=app.config['REDIS_PORT'],
# #                              db=app.config['REDIS_DB'])
# # celery = make_celery(app)

# # # Import and register the Blueprint
# # from app.routes import bp as main_bp
# # app.register_blueprint(main_bp)
# # app/__init__.py



# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_migrate import Migrate
# # import redis
# # import mongoengine
# # from config import Config  # Import the Config class from your config module


# # app = Flask(__name__, static_url_path='/static')
# # app.config.from_object(Config)  # Assuming Config is imported properly

# # # Initialize SQLAlchemy for database operations
# # db = SQLAlchemy(app)
# # migrate = Migrate(app, db)

# # # Connect to Redis instance
# # redis_db = redis.StrictRedis(host=app.config['REDIS_SERVER'],
# #                              port=app.config['REDIS_PORT'],
# #                              db=app.config['REDIS_DB'])

# # # Define default MongoDB connection
# # mongoengine.connect(host=app.config['MONGODB_HOST'],
# #                      port=app.config['MONGODB_PORT'],
# #                      username=app.config['MONGODB_USERNAME'],
# #                      password=app.config['MONGODB_PASSWORD'],
# #                      authentication_source=app.config['MONGODB_AUTHENTICATION_DB'])

# # # Import and register the main blueprint
# # from .routes import bp as main_bp
# # app.register_blueprint(main_bp)

# # # Import models for database
# # from . import models
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from config import Config
# import redis
# import mongoengine

# app = Flask(__name__, static_url_path='/static')
# app.config.from_object(Config)




# # Initialize SQLAlchemy for database operations
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # Connect to Redis instance
# redis_db = redis.StrictRedis(
#     host=app.config['REDIS_SERVER'],
#     port=app.config['REDIS_PORT'],
#     db=app.config['REDIS_DB']
# )

# # # Connect to MongoDB using mongoengine
# # mongoengine.connect(
# #     db=app.config['MONGODB_AUTHENTICATION_DB'],
# #     host=app.config['MONGODB_HOST'],
# #     port=app.config['MONGODB_PORT'],
# #     username=app.config['MONGODB_USERNAME'],
# #     password=app.config['MONGODB_PASSWORD']
# # )
# # Connect to MongoDB using mongoengine
# mongoengine.connect(host=app.config['MONGODB_URI'])

# # Import and register the main blueprint
# from .routes import bp as main_bp
# app.register_blueprint(main_bp)

# # Import models for database
# from . import models



from flask import Flask
from flask_mongoengine import MongoEngine
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import redis
import mongoengine
import pymongo
import ssl


app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)



# Initialize MongoEngine
db = MongoEngine(app)

# # Initialize SQLAlchemy for database operations
# db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Connect to Redis instance
redis_db = redis.StrictRedis(
    host=app.config['REDIS_SERVER'],
    port=app.config['REDIS_PORT'],
    db=app.config['REDIS_DB']
)

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


# Connect to MongoDB using pymongo with SSL enabled
client = pymongo.MongoClient(app.config['MONGODB_URI'], ssl=True)

print(app.config['MONGODB_URI'])


# Import and register the main blueprint
from .routes import bp as main_bp
app.register_blueprint(main_bp)

