from requests import Response
from .api_response import ApiResponse


class ConferencesResponse(ApiResponse):
    """
    Contains the response from the conferences endpoint
    """

    def __init__(self, response: Response):
        super().__init__(response)