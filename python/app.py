from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# postgresql://user:pass@localhost:5432/my_db
app.config['SQLALCHEMY_DATABASE_URI'] = ( 
  f"postgresql://{os.environ['PG_USER']}"   
  f":{os.environ['PG_PASSWORD']}"
  f"@{os.environ['PG_HOST']}"
  f":{os.environ['PG_PORT']}"
  f"/{os.environ['PG_DATABASE']}"
)

db = SQLAlchemy(app)

# Model
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), unique=True, nullable=False)
  content = db.Column(db.String(255), nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content

db.create_all()

@app.route('/', methods=['GET'])
def get():
  return "ok"

# Create Item
@app.route('/items', methods=['POST'])
def itemadd():
  request_data = request.get_json()

  title = request_data['title']
  content = request_data['content']

  db.session.add(Item(title, content))
  db.session.commit()

  return "item created"