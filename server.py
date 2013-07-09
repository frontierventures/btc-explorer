from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.python import log
from twisted.web.template import XMLString, Element, renderer, renderElement

from twisted.python.filepath import FilePath
from twisted.web.util import redirectTo
from twisted.web.static import File

import explorer
import sys
import elements


class Main(Resource):
    def __init__(self):
        Resource.__init__(self)

    def render(self, request):
        output = explorer.summary()
        return renderElement(request, Page(output))


class Page(Element):
    def __init__(self, output):
        self.output = output
        self.loader = XMLString(FilePath('templates/pages/summary.xml').getContent())

    @renderer
    def menu(self, request, tag):
        return elements.Menu()

    @renderer
    def summary(self, request, tag):
        print self.output
        slots = {}
        slots['blocks'] = "Current block: %s" % self.output['result']['blocks']
        slots['difficulty'] = "Difficulty: %s" % self.output['result']['difficulty']
        yield tag.clone().fillSlots(**slots) 

log.startLogging(sys.stdout)
root = Main()
root.putChild('', root)

reactor.listenTCP(8888, Site(root))
reactor.run()
