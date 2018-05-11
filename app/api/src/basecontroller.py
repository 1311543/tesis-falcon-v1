## coding: utf-8
# from jinsei.src.decorators import handler_exception

from falcon import errors

class Controller(object):

    def __init__(self, context, **kwargs):
        self.context = context
        for key, value in kwargs.items():
            setattr(self, key, value)