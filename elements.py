from twisted.web.template import XMLString, Element, renderer

from twisted.python.filepath import FilePath

class Menu(Element):
    def __init__(self):
        self.loader = XMLString(FilePath('templates/elements/menu.xml').getContent())
