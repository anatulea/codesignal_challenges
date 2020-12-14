'''
You are creating a new website about HTML parsing. You don't want your page to be too simple, so you would like to estimate the complexity of the main page of your site. In order to measure the complexity of the page, you need to find a set of all tags located on the deepest level of a tree correponsing to HTML document. Given a valid HTML document, find all distinct tags located on the deepest level.

Example

For
document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
the output should be
pageComplexity(document) = ["h1", "p"].
'''
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    
    def __init__(self):
        html.parser.HTMLParser.__init__(self)
        self.level = 0
        self.tags = {}
        self.maxlevel = 0
    
    def handle_starttag(self, tag, attrs):
        self.level += 1
        if self.level>self.maxlevel: self.maxlevel = self.level
        self.tags.setdefault(self.level, set()).add(tag)
    
    def handle_endtag(self, tag):
        self.level -= 1

def pageComplexity(document):
    myparser = MyHTMLParser()
    myparser.feed(document)

    return sorted(myparser.tags[myparser.maxlevel])
