from init import db, ma
from marshmallow import fields

class User(db.Model):
    # define the table name
    __tablename__ = "users"

    #define the primary key
    id = db.Column(db.Integer, primary_key=True)

    # more attributes (columns)
    name = db.Column(db.String(100))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cards = db.relationship("Card", back_populates="user")
    comments = db.relationship("Comment", back_populates = "user")

class UserSchema(ma.Schema):
    # a List of nested fields.
    # a user can have multiple cards and comments
    cards = fields.List(fields.Nested("CardSchema", exclude=["user"]))
    comments = fields.List(fields.Nested('CommentSchema', exclude=["user"]))

    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "cards", "comments")

# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
users_schema = UserSchema(many=True, exclude=["password"])

