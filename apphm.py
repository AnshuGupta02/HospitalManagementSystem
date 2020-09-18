from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hm.db'

db=SQLAlchemy(app)
#bootstrap=Bootstrap(app)

from routeshm import *

if __name__ == '__main__':
    app.run(debug=True)
