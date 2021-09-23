from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    output = []
    drinks = Drink.query.all()
    for drink in drinks:
        drink = {'name': drink.name, 'description': drink.description}
        output.append(drink)
    return {"drinks": output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if not drink:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "deleted successfully"}


'''
from flask_application import db
db.create_all()  # Creates the table

drink = Drink(name="Grape Soda", description="soda like taste")


from flask_application import Drink

# add drink
drink = Drink(name="Grape Soda", description="soda like taste")
db.session.add(drink)
db.session.commit()
Drink.query.all()

# add another drink
db.session.add(Drink(name="Cherry", description="Tastes like cherry"))
Drink.query.all()
db.session.commit()

'''