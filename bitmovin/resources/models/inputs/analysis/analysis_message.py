from bitmovin.resources import Resource, Link
from bitmovin.errors import InvalidTypeError


class AnalysisMessage(Resource):

    def __init__(self, id_, timestamp, type_, text, field, links):
        super().__init__()
        self._links = None
        self.id = id_
        self.timestamp = timestamp
        self.type = type_
        self.text = text
        self.field = field
        self.links = links

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object.get('id')
        timestamp = json_object.get('timestamp')
        type_ = json_object.get('type')
        text = json_object.get('text')
        field = json_object.get('field')
        links = json_object.get('links')

        analysis_message = AnalysisMessage(
            id_=id_, type_=type_, text=text, field=field, links=links, timestamp=timestamp)

        return analysis_message

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

