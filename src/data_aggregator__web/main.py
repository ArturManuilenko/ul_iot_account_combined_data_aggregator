from src.conf.data_aggregator__web import db_config, web_sdk

flask_app = web_sdk.flask_app
db_config.attach_to_flask_app(flask_app)
flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
flask_app.config['SECRET_KEY'] = 'some-long-long-sting-for-csrf-token-for-wtforms'

web_sdk.load_routes()

__all__ = (
    'flask_app',
)
