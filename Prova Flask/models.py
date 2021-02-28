from operator import pos
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Aeroporto(db.Model):
    __tablename__ = 'aeroporto'

    codaeroporto = db.Column(db.String(), primary_key=True)
    nomeaeroporto = db.Column(db.String())
    città = db.Column(db.String())

    def __init__(self, codaeroporto, nomeaeroporto, città):
        self.codaeroporto = codaeroporto
        self.nomeaeroporto = nomeaeroporto
        self.città = città

    def __repr__(self):
        return f"<Aeroporto {self.nomeaeroporto} in {self.città}>"


class Post(db.Model):
    __tablename__ = "post"

    post_id = db.Column(db.String(), primary_key = True)
    contenuto = db.Column(db.String)
    utente_id = db.Column(db.String)
    data_pubblicazione = db.Column(db.TIMESTAMP)

    def __init__(self, post_id, descrizione, utente_id, data_pubblicazione):

        self.post_id = post_id
        self.contenuto = descrizione
        self.utente_id = utente_id
        self.data_pubblicazione = data_pubblicazione

    def __repr__(self):
        return f"post {self.post_id} di {self.utente_id} pubblicato in data {self.data_pubblicazione} che dice:\n {self.contenuto}"