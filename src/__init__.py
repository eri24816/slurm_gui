from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask import session,redirect,render_template,url_for

socketio = SocketIO()
login_manager = LoginManager()
def create_app():
    app = Flask(__name__.split('.')[0])

    
    login_manager.init_app(app)

    from . import auth, posts, slurm
    for module in [auth,posts,slurm]:
        app.register_blueprint(module.bp)
    
    @app.route('/', methods=["GET", "POST"])
    def index():
        if not session.get('logged_in', False):
            return redirect(url_for('auth.login'))
        return render_template('index.html')

    

    return app



