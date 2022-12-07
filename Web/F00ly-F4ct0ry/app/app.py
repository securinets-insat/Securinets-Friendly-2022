
from flask import Flask, render_template, redirect, session, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = app.config['SECRET_KEY']

# Getting configuration variables from config.py
app.config.from_pyfile('config.py')

# Getting db instance
db = SQLAlchemy(app)

users = dict()

# Defining a list of mechas
mechas = [
    {'name': 'Atomsk',
     'power': app.config['FLAG'],
     'image':'Atomsk.gif'
     },
    {
        'name': 'Canti',
        'power': 'Extreme physical strength, can fuse with Naota to transform into a powerful cannon apparently powered by his N.O., can fuse with other robots, levitation and flight, communication device',
        'image': 'Canti.webp',
    },
    {
        'name': 'Detective Rifle Mecha',
        'image': 'DetectiveRifleMecha.gif',
        'power': 'This robot is a large tower-like robot wearing a button-up coat and hat. It has rifles and revolvers, shooting many bullets at a time. After the cape is removed, it resembles a gargantuan hand. '
    },
    {
        'name': 'Defective Hand Mecha',
        'power': 'his robot is a hand-shaped robot. It can use its fingers to crawl around and has teeth to bite. Red and blue wires stick out of its body. ',
        'image': 'DefectiveHandMecha.gif',
    },
]


# Defining our model
class Mecha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    power = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f"Mecha('{self.name}', '{self.power}')"


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/mecha", methods=['GET'])
def all_mechas():
    mechas = Mecha.query.all()[1:]
    print(mechas)
    return render_template('mechas.html', mechas=mechas)


@app.route("/mecha/<int:mechaId>", methods=['GET'])
def find_mecha(mechaId):
    if session.get('username', None) != None:
        print('here')
        mecha = Mecha.query.get_or_404(mechaId)
        return render_template('mecha.html', mecha=mecha)
    else:
        return redirect('/login')


@app.route("/ping", methods=['GET'])
def ping():
    return "pong, up and running"


@app.route("/login", methods=['GET', 'POST'])
def login():
    method = request.method
    error = ''

    if method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if users.get(username, None) == None:
            users[username] = password
            print('here')
        if users.get(username) == password:
            session['username'] = username

            return redirect('/mecha')
        else:
            error = "Username or password is incorrect, please try again"

    if session.get('username', None) != None:
        return redirect('/mecha')

    return render_template('login.html', error=error)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect('/')


def init_db():
    db.drop_all()
    db.session.commit()
    db.create_all()
    for mecha in mechas:
        new_mecha = Mecha(name=mecha['name'],
                          power=mecha['power'],
                          image=mecha['image'])
        db.session.add(new_mecha)
    # Commiting changes to db
    db.session.commit()
    print('added all')


init_db()
