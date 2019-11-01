from requests import Response
from inspirehep_api_wrapper.datamodel.authors_record import AuthorsRecord
from typing import Dict, Any


class AuthorsResponse:
    """
    """

    def __init__(self, api_authors_response: Response):
        self.api_authors_response = api_authors_response

    @property
    def data(self) -> Dict[str, Any]:
        return self.api_authors_response.json()

    def to_record(self):
        return AuthorsRecord(self.data)
