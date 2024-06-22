from datetime import date

from flask import Blueprint
from init import db, bcrypt

from models.user import User
from models.card import Card
from models.comment import Comment

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
            email="admin1@email.com",
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

    cards = [
        Card(
            title = "Title 1",
            description = "Description 1",
            date = date.today(),
            status = "Todo",
            priority = "Urgent",
            user = users[1]
        ),
        Card(
            title = "Title 2",
            description = "Description 2",
            date = date.today(),
            status = "Done",
            priority = "Do whenever",
            user = users[2]
        ),
        Card(
            title = "Title 3",
            description = "Description 3",
            date = date.today(),
            status = "Processing",
            priority = "Eh",
            user= users[1]
        )
    ]

    db.session.add_all(cards)

    db.session.commit()

    print("Tables Seeded..")

