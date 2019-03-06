from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#DB setup
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine



@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for i in items:
        output += '<p>'
        output += ('{} </br>').format(i.name)
        output += ('{} </br>').format(i.price)
        output += ('{} </br>').format(i.description)
        output += '</p>'
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)