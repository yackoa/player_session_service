from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

# TODO : move SQLAlchemy settings to config file
#SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db = SQLAlchemy(app)

class Player(db.Model):
    """
        "event": "start",
        "country": "FI",
        "player_id": "0a2d12a1a7e145de8bae44c0c6e06629",
        "session_id": "4a0c43c9-c43a-42ff-ba55-67563dfa35d4",
        "ts": "2016-12-02T12:48:05.520022"
    """
    #__tablename__ = 'player'
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
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')

    def __repr__(self):
        return '< event: %s country: %s player_id: %s session_id: %s timestamp: %s session_completed: %s>' \
               % (self.event, self.country, self.player_id, self.session_id, self.timestamp, self.session_completed)


