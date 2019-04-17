import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from flask_sqlalchemy import SQLAlchemy
from config.config import DevelopmentConfig

app = create_app()

    # set config
app_settings = os.getenv(
    "APP_SETTINGS", "config.config.DevelopmentConfig"
)
app.config.from_object(DevelopmentConfig)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()