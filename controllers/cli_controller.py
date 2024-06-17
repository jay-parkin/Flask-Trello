from flask import Blueprint
from init import db, bcrypt

from models.user import User

db_commands = Blueprint("db", __name__)

# cli command used - flask db create
@db_commands.cli.command("create")
def create_tables():
    db.create_all()

    print("Tables Created...")

# cli command used - flask db drop
@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

# cli command used - flask db seed
@db_commands.cli.command("seed")
def seed_tables():

    # list of user instances
    users = [
        User(
            name="Admin",
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8")
        ),
        User(
            name="User 2",
            email="user2@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8")
        ),
        User(
            name="User 3",
            email="user3@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    print("Tables Seeded..")