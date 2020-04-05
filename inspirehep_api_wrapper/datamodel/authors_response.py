from requests import Response
from .api_response import ApiResponse


class AuthorsResponse(ApiResponse):
    """
    Contains the response from the authors endpoint
    """

    def __init__(self, response: Response):
        super().__init__(response)