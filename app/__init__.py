from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'JWT Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
    'Api Key': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'ApiKey'
    },
}

api = Api(blueprint,
    title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus web service',
    security=['JWT Auth', 'Api Key'],
    authorizations=authorizations
    )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)