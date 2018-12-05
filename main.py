from flask import Flask,jsonify, request,abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
#db.createAll()

class Player(db.Model):
    """
        "event": "start",
        "country": "FI",
        "player_id": "0a2d12a1a7e145de8bae44c0c6e06629",
        "session_id": "4a0c43c9-c43a-42ff-ba55-67563dfa35d4",
        "ts": "2016-12-02T12:48:05.520022"
        TODO: add date time conversion based on1
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
        self.timestamp = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f')

@app.route("/api/v1/hello")
def print_hello():
    return "hello world"

@app.route('/api/v1/players/20', methods = ['GET'])
def get_completed_sessions(player_id):
    """
    API for fetching last 20 complete sessions for a given player
    :return: JSON result set
    """
    """
    :return: 
    """
    #TODO :  add limit once it starts working , after order by timestamp works
    #Player().filter(something).limit(5).all()

    sessions = db.select([Player]).\
        where(db.and_(Player.columns.player_id == player_id,
                      Player.columns.session_completed != True))
    return jsonify({'Session':sessions})

@app.route('/api/v1/event_batch',methods = ['POST'])
def create_session():
    """
    API for reciving event batches
    :return:
    """
    if not request.json or not 'event' in request.json \
            or not 'country'  in request.json \
            or not 'player_id' in request.json:
        abort(400)
    print(request.json)
    player = Player(request.json['event'],request.json['country'],
                    request.json['player_id'],request.json['session_id'],request.json['ts'])
    db.session.add(player)
    db.session.commit()
    return jsonify({'Player':player})

if __name__== '__main__':
    app.run(debug=True)