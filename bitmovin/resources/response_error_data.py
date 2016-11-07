from typing import List

from bitmovin.errors import InvalidTypeError
from .link import Link
from .response_data import ResponseData
from .response_error_data_detail import ResponseErrorDataDetail


class ResponseErrorData(ResponseData):

    def __init__(self, code, message, developer_message, links, details):
        super().__init__()
        self._links = None
        self._details = None
        self.code = code
        self.message = message
        self.developerMessage = developer_message
        self.links = links  # type: List[Link]
        self.details = details  # type: List[ResponseErrorDataDetail]

    @classmethod
    def parse_from_json_object(cls, json_object):
        code = json_object.get('code')
        message = json_object.get('message')
        developer_message = json_object.get('developerMessage')
        links = json_object.get('links')
        details = json_object.get('details')

        data = ResponseErrorData(
            code=code, message=message, developer_message=developer_message, links=links, details=details)

        return data

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

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, new_details):
        if new_details is None:
            return

        if not isinstance(new_details, list):
            raise InvalidTypeError('details has to be a list of ResponseErrorDataDetail objects')

        if all(isinstance(detail, ResponseErrorDataDetail) for detail in new_details):
            self._details = new_details
        else:
            details = []
            for json_detail in new_details:
                detail = ResponseErrorDataDetail.parse_from_json_object(json_detail)
                details.append(detail)
            self._details = details
