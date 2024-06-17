from main import db

class Comments(db.model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String, nullable=False)
    date = db.Column(db.Date(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, onupdate="CASCADE", ondelete="CASCADE")
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False, onupdate="CASCADE", ondelete="CASCADE")