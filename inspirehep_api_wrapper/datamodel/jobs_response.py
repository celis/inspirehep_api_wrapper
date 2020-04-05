from requests import Response
from .api_response import ApiResponse


class JobsResponse(ApiResponse):
    """
    Contains the response from the job endpoint
    """

    def __init__(self, response: Response):
        super().__init__(response)