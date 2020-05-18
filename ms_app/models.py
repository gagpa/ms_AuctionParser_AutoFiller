from . import db


class Auction(db.Model):
    """Модель Аукциона"""
    __tablename__ = 'auctions'
    id = db.Column(db.Integer, primary_key=True)  # TODO
    purchase_number = db.Column(db.String)
    notice_id = db.Column(db.String)
    type_name = db.Column(db.String)
