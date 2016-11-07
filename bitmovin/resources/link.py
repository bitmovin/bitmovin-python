from .resource import Resource


class Link(Resource):

    def __init__(self, href, title):
        super().__init__()
        self.href = href
        self.title = title

    @classmethod
    def parse_from_json_object(cls, json_object):
        href = json_object.get('href')
        title = json_object.get('title')
        link = Link(href=href, title=title)
        return link

