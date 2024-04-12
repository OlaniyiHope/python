# # import os


# # class Config(object):
# #     SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'

# #     # Redis
# #     REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'
# #     REDIS_PORT = os.getenv('REDIS_PORT') or 6379
# #     REDIS_DB = os.getenv('REDIS_DB') or 1
# #     REDIS_URL = 'redis://{}:{}'.format(REDIS_SERVER, REDIS_PORT)

# #     # Celery task queue
# #     CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or REDIS_URL
# #     CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or REDIS_URL
   

# #        # MongoDB
# #     MONGODB_PORT = os.getenv('MONGODB_PORT') or 27017
# #     MONGODB_HOST = os.getenv('MONGODB_HOST') or 'cluster0.fzjtw.mongodb.net'
# #     MONGODB_USERNAME = os.getenv('MONGODB_USERNAME') or 'olaniyihoppee'
# #     MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD') or 'take100'
# #     MONGODB_AUTHENTICATION_DB = os.getenv('MONGODB_AUTHENTICATION_DB') or 'python'
  
# # @staticmethod
# #     def connect_to_mongodb():
# #         try:
# #             client = pymongo.MongoClient(Config.MONGODB_URI)
# #             db = client.get_default_database()
# #             print("Connected to MongoDB:", db)
# #             return db
# #         except Exception as e:
# #             print("Error connecting to MongoDB:", e)
# #             raise e

# #     # database settings
# #     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
# #       'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
# #       'flaskdash.db')
# #     SQLALCHEMY_TRACK_MODIFICATIONS = False


# import os
# import mongoengine

# class Config(object):
#     SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'

#     # Redis
#     REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'
#     REDIS_PORT = os.getenv('REDIS_PORT') or 6379
#     REDIS_DB = os.getenv('REDIS_DB') or 1
#     REDIS_URL = 'redis://{}:{}'.format(REDIS_SERVER, REDIS_PORT)

#     # Celery task queue
#     CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or REDIS_URL
#     CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or REDIS_URL

#     # MongoDB
#     MONGODB_HOST = os.getenv('MONGODB_HOST') or 'cluster0.fzjtw.mongodb.net'
#     MONGODB_USERNAME = os.getenv('MONGODB_USERNAME') or 'olaniyihoppee'
#     MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD') or 'take100'
#     MONGODB_AUTHENTICATION_DB = os.getenv('MONGODB_AUTHENTICATION_DB') or 'python'
#     MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))  # Default port is 27017

  
#     @staticmethod
#     def connect_to_mongodb():
#         try:
#             mongoengine.connect(
#                 db=Config.MONGODB_AUTHENTICATION_DB,
#                 host=Config.MONGODB_HOST,
#                 port=int(os.getenv('MONGODB_PORT', 27017)),  # Convert port to integer
#                 username=Config.MONGODB_USERNAME,
#                 password=Config.MONGODB_PASSWORD
#             )
#             print("Connected to MongoDB")
#         except Exception as e:
#             print("Error connecting to MongoDB:", e)
#             raise e

#     # Database settings
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flaskdash.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'development key'

    # Redis configuration
    REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'
    REDIS_PORT = os.getenv('REDIS_PORT') or 6379
    REDIS_DB = os.getenv('REDIS_DB') or 1
    REDIS_URL = 'redis://{}:{}'.format(REDIS_SERVER, REDIS_PORT)

    # Celery task queue
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or REDIS_URL
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or REDIS_URL

    # MongoDB configuration
    MONGODB_URI = os.getenv('MONGODB_URI') or 'mongodb+srv://olaniyihoppee:take100@cluster0.fzjtw.mongodb.net/newpython?retryWrites=true&w=majority'

    # Database settings
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flaskdash.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
