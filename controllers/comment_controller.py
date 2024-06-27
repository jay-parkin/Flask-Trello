from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.comment import Comment, comment_schema, comments_schema
from models.card import Card

# /cards/<int:card_id>/comments
comments_bp = Blueprint("comments", __name__, url_prefix="/<int:card_id>/comments")

# create comment route
@comments_bp.route("/", methods=["POST"])
@jwt_required()
def create_comment(card_id):
    # get the comment message from body data
    body_data = request.get_json()

    # fetch the cards with that particular id - card_id
    stmt = db.select(Card).filter_by(id = card_id)
    card = db.session.scalar(stmt)

    # if exists
    if card:
        # create an instance of the comment model
        comment = Comment(
            message = body_data.get("message"),
            date = date.today(),
            card = card,
            user_id = get_jwt_identity()
        )

        # add and commit the session
        db.session.add(comment)
        db.session.commit()

        # return the created commit
        return comment_schema.dump(comment), 201

    # else
    else:
        # return an error 'card does not exist'
        return {"error": f"Card with id {card_id} not found"}, 404

# delete comment
@comments_bp.route("/<int:comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(card_id, comment_id):
    # fetch the comment from the db with the id - comment_id
    stmt = db.select(Comment).filter_by(id = comment_id)
    comment = db.session.scalar(stmt)

    # if comment exists
    if comment:
        # delete the comment
        db.session.delete(comment)
        db.session.commit()

        # return some message
        return {"message": f"Comment '{comment.message}' deleted successfully"}
    # else
    else:
        # return an error saying the comment does not exist
        return {"error": f"Comment with id {comment_id} not found"}, 404
    
# editting/updating the comment - /cards/card_id/comments/comment_id
@comments_bp.route("/<int:comment_id>", methods=["PUT", "PATCH"])
@jwt_required()
def edit_comment(card_id, comment_id):
    # get the updated value form the body of the request
    body_data = request.get_json()
    # fetch the comment in the db with the id comment_id
    stmt = db.select(Comment).filter_by(id = comment_id)
    comment = db.session.scalar(stmt)

    # if comment exist
    if comment:
        # update the fields
        comment.message = body_data.get("message") or comment.message

        # commit
        db.session.commit()

        # return some response to the client
        return comment_schema.dump(comment)
    # else
    else:
        # return error saying comment does not exist
        return {"error": f"Comment with id {comment_id} not found"}, 404