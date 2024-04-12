from mongoengine import Document, StringField

class User(Document):
    role = StringField(required=True, choices=["admin", "teacher", "parent", "student"])
    username = StringField(required=True, unique=True)
    email = StringField()
    password = StringField(required=True)
    address = StringField()
    phone = StringField()


