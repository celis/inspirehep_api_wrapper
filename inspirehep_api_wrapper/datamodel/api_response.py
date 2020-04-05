from typing import Dict, List
from requests import Response


class ApiResponse:
    """
    Class handling the API response
    """

    def __init__(self, response: Response):
        self.response = response

    @property
    def data(self) -> Dict:
        """
        Returns data on the response
        """
        data = self.response.json()
        if data.get("metadata"):
            return data["metadata"]


class SearchAPIResponse:
    """
    Class handling search responses
    """

    def __init__(self, response: Response):
        self.response = response

    @property
    def data(self) -> List:
        """
        Returns data on the response
        """
        data = self.response.json()
        if data.get("hits"):
            return data["hits"]["hits"]
