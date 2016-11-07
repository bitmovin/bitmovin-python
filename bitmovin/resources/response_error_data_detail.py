from bitmovin.errors import InvalidTypeError
from .resource import Resource
from .link import Link


class ResponseErrorDataDetail(Resource):

    def __init__(self, timestamp, type_, text, field, links):
        super().__init__()
        self._links = None  # to suppress variable declared outside of __init__ warning
        self.timestamp = timestamp
        self.type = type_
        self.text = text
        self.field = field
        self.links = links

    @classmethod
    def parse_from_json_object(cls, json_object):
        timestamp = json_object.get('timestamp')
        type_ = json_object.get('type')
        text = json_object.get('text')
        field = json_object.get('field')
        links = json_object.get('links')
        detail = ResponseErrorDataDetail(timestamp=timestamp, type_=type_, text=text, field=field, links=links)
        return detail

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, new_links):
        if new_links is None:
            return

        if not isinstance(new_links, list):
            raise InvalidTypeError('links has to be a list of Link objects')

        if all(isinstance(link, Link) for link in new_links):
            self._links = new_links
        else:
            links = []
            for json_link in new_links:
                link = Link.parse_from_json_object(json_link)
                links.append(link)
            self._links = links
