from typing import Dict
from requests import Response


class ApiResponse:
    """
    Base class for classes handling the API response
    """

    def __init__(self, response: Response):
        self.response = response

    @property
    def data(self) -> Dict:
        """
        Returns data on the response
        """
        return self.response.json()['metadata']