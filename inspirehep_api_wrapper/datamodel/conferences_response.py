from requests import Response
from inspirehep_api_wrapper.datamodel.conferences_record import ConferencesRecord
from typing import Dict, Any


class ConferencesResponse:
    """
    Contains the response from the conferences endpoint
    """

    def __init__(self, api_conferences_response: Response):
        self.api_conferences_response = api_conferences_response

    @property
    def data(self) -> Dict[str, Any]:
        """
        Raw data obtained from INSPIRE
        """
        return self.api_conferences_response.json()

    def to_record(self) -> ConferencesRecord:
        """
        Return a ConferencesRecord object
        """
        return ConferencesRecord(self.data)