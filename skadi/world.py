import collections as c

from skadi.io import protobuf
from skadi.util.flattener import Flattener

class World(object):
    def __init__(self):
        self.meta = {}
        self.classes = c.OrderedDict()
        self.properties = c.OrderedDict()
        self.string_tables = c.OrderedDict()
        self.send_tables = c.OrderedDict()
        self.recv_tables = c.OrderedDict()

    def __repr__(self):
        lenst = len(self.send_tables)
        lenrt = len(self.recv_tables)
        return '<World ({0} send, {1} recv)>'.format(lenst, lenrt)