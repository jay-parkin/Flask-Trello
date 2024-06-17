from flask import Blueprint, jsonify, request
from main import db
from models.cards import Card

cards = Blueprint('cards',__name__, url_prefix="/cards")

# The GET routes endpoint
@cards.route("/", methods=["GET"])
def get_cards():
    # get all the cards from the database table
    cards_list = Card.query.all()
    # Convert the cards from the database into a JSON format and store them in result
    #result = cards_schema.dump(cards_list)
    # return the data in JSON format
    #return jsonify(result)
    return "List of cards retrieved"