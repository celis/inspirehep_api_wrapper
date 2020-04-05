from requests import Response
from .api_response import ApiResponse


class LiteratureResponse(ApiResponse):
    """
    Contains the response from the literature endpoint
    """

    def __init__(self, response: Response):
        super().__init__(response)
