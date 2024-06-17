from main import db

class Card(db.model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)

    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Date(), nullable=True)
    status = db.Column(db.String, nullable=True)
    priority = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, onupdate="CASCADE", ondelete="CASCADE")



