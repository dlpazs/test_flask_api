from app import app, utils
from flask import request, jsonify, abort
from flask_caching import Cache
from flask_restplus import Api, Resource
import logging

cache = Cache(app)
api = Api(app)

logging.basicConfig(filename='app.log', level=logging.DEBUG)

@api.route('/users/london')
class londoners(Resource):
    @cache.cached() # same as memoize() when function has no arguments
    def get(self):
        try:
            data = utils.get_londoners()
            return jsonify(data)
        except Exception as e:
            return {"message": str(e)}


@api.route('/users/london/proximity')
class proximity(Resource):
    @cache.cached()
    def get(self):
        users = utils.get_londonders_proximity()
        return jsonify(users)


@api.route('/users')
class all_london(Resource):
    @cache.cached()
    def get(self):
        ldn_users = utils.get_londoners()
        prox_users = utils.get_londonders_proximity()
        comb_users = ldn_users + prox_users # Used + operator due to anomalies in Swagger calls.
        return jsonify(comb_users)

@app.errorhandler(404)
def not_found(e):
    app.logger.error("Not Found Error: {}".format(str(e)))
    return {"message": "{} Please see {} api documentation for more details.".format(str(e), request.url_root)}


@app.errorhandler(500)
def server_error(e):
    app.logger.error("Server Error: {}".format(str(e)))
    return {"message": str(e)}
