# -*- coding: utf-8 -*-

import falcon

from api.src.middlewares import JSONTranslator
from api.src.middlewares import RequireJSON
from api.src.middlewares import CrossOriginResourceSharing
#
# Routers
from api.src.routers import CustomRouter

# Controllers
from api.src.controllers import BICollection
from api.src.controllers import BIResource



class App(object):
    """App for Api Rest"""

    def __init__(self, ctx):
        self.ctx = ctx

        # Get Backing Services from config file
        self._get_config_backing_services()

        # Setup database
        db = self._setup_db()

        self.api = falcon.API(
            router=CustomRouter(),
            middleware=[
                CrossOriginResourceSharing(),
                RequireJSON(),
                JSONTranslator()
            ]
        )

        # load routes
        self._load_routes()

    def _load_routes(self):
        self.api.add_route('/bi', BICollection(self.ctx))
        self.api.add_route('/bi/{id}', BIResource(self.ctx))

    def _get_config_backing_services(self):
        try:
            self.ctx.backingServices = self.ctx.config["backingServices"]
        except Exception as e:
            self.ctx.log("No exists configurations for DB Backing Services")

    def _setup_db(self):
        pass