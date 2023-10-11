#API Stuff
import logging

from flask import Flask, abort, jsonify, request
from flask_restx import Api, Resource, reqparse
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

application = Flask(__name__)
application.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
application.config['DEBUG'] = True
application.wsgi_app = ProxyFix(application.wsgi_app)


restxapi = Api(application,version='beta', title='Internal API',description='An API used for my applications.',)
parser = reqparse.RequestParser()

ns1 = restxapi.namespace('demo/', description='Demo API endpoints')

@ns1.route('/test1')
class CryptoPrice(Resource):

    parser.add_argument('demo', type=str, required=True, location='form',help='Temporal customer name.')
    @restxapi.doc(parser=parser)

    def get(self):
        try:
            return jsonify('Successful get')
        except Exception as e:
            logging.error(e)
            abort(400)
    
    def post(self):
        args = parser.parse_args()

        try:
            return jsonify(args)
        except Exception as e:
            logging.error(e)
            abort(400)
        

if __name__ == '__main__':

    #application.run(host='0.0.0.0',port=9000, debug=True,ssl_context='adhoc)
    application.run(host='0.0.0.0',port=9000, debug=True)