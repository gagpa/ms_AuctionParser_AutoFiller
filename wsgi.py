import os

from dotenv import load_dotenv
from flask_migrate import Migrate


env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

from app import app, db

migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
