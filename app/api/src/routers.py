import os
from api.src import __version__
from falcon.routing import CompiledRouter


class CustomRouter(CompiledRouter):

    def add_route(self, uri_template, method_map, resource):
        uri_template = '/api/v%s%s' % (__version__, uri_template)
        return super(CustomRouter, self).add_route(
            uri_template, method_map, resource
        )

    def find(self, uri):
        path, ext = os.path.splitext(uri)
        return super(CustomRouter, self).find(path)
