from flask import Flask
from routes.auth import auth
from models.user import db


app = Flask(__name__)

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
app.register_blueprint(auth)

@app.route('/')
def home():
    return render_template('templates/login.html')  # redirige vers la page de connexion

if __name__ == "__main__":
    app.run()
