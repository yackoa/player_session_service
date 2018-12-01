from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Player(db.Model):
    """
        "event": "start",
        "country": "FI",
        "player_id": "0a2d12a1a7e145de8bae44c0c6e06629",
        "session_id": "4a0c43c9-c43a-42ff-ba55-67563dfa35d4",
        "ts": "2016-12-02T12:48:05.520022"
        TODO: add date time conversion based on
    """
    event = db.Column(db.String(5))
    country = db.Column(db.String(2))
    player_id = db.Column(db.String(50),primary_key=True)
    session_id = db.Column(db.String(50))
    timestamp  = db.Column(db.DateTime)
    session_completed = db.Column(db.BOOLEAN,default=False)

    def __init__(self,event,country,player_id,session_id,timestamp):
        self.event = event
        self.country = country
        self.player_id = player_id
        self.session_id = session_id
        self.timestamp = timestamp

@app.route("/api/v1/hello")
def print_hello():
    return "hello world"

if __name__== '__main__':
    app.run(debug=True)