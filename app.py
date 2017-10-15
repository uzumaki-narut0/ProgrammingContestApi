from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.cache import Cache
import os
import make_api

app = Flask(__name__)
api = Api(app)
cache = Cache(config={'CACHE_TYPE': 'simple'})

resultSet = {"present_contests":[],"upcoming_contests":[]}

class ContestTracker(Resource):
    @cache.cached(timeout=900)  #caching for 15 minutes
    def get(self):
        make_api.make_api(resultSet);
        return {"result": resultSet}

class ContestTrackerWithQueryLimit(Resource):
    @cache.cached(timeout=900)  #caching for 15 minutes
    def get(self, querylimit):
        assert (str(type(querylimit)) == "<type 'int'>"),type(querylimit)
        make_api.make_api(resultSet);
        if(querylimit <= len(resultSet["present_contests"])):
            resultSet["present_contests"] = resultSet["present_contests"][:querylimit]
        if(querylimit <= len(resultSet["upcoming_contests"])):
            resultSet["upcoming_contests"] = resultSet["upcoming_contests"][:querylimit]
        return {"result": resultSet}

class UpcomingContestTracker(Resource):
    @cache.cached(timeout=900)  #caching for 15 minutes
    def get(self, querylimit):
        assert (str(type(querylimit)) == "<type 'int'>"),type(querylimit)
        make_api.make_api(resultSet);
        if(querylimit <= len(resultSet["upcoming_contests"])):
            return {"result": resultSet["upcoming_contests"][:querylimit]}
        else:
            return {"result":resultSet}

class PresentContestTracker(Resource):
    @cache.cached(timeout=900)  #caching for 15 minutes
    def get(self, querylimit):
        assert (str(type(querylimit)) == "<type 'int'>"),type(querylimit)
        make_api.make_api(resultSet);
        if(querylimit <= len(resultSet["present_contests"])):
            return {"result": resultSet["present_contests"][:querylimit]}
        else:
            return {"result": resultSet }

    
api.add_resource(ContestTracker, '/')
api.add_resource(ContestTrackerWithQueryLimit, '/<int:querylimit>')
api.add_resource(UpcomingContestTracker, '/upcoming/<int:querylimit>')
api.add_resource(PresentContestTracker, '/present/<int:querylimit>')


port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
