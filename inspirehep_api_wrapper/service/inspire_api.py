import requests
from inspirehep_api_wrapper.datamodel.api_response import ApiResponse


class InspireAPI:
    """
    Simple wrapper around the INSPIRE API

    https://labs.inspirehep.net

    methods:
       literature: gives access to the literature endpoint
       authors: gives access to the authors endpoint
       jobs: gives access to the jobs endpoint
       conferences: access to conferences endpoint
    """

    LITERATURE = "https://labs.inspirehep.net/api/literature/"
    AUTHORS = "https://labs.inspirehep.net/api/authors/"
    JOBS = "https://labs.inspirehep.net/api/jobs/"
    CONFERENCES = "https://labs.inspirehep.net/api/conferences/"

    def __init__(self):
        pass

    def literature(self, record_id: str) -> ApiResponse:
        """
        Returns api response for a given record_id
        """
        url = self.LITERATURE + record_id
        return ApiResponse(requests.get(url))

    def authors(self, author_id: str) -> ApiResponse:
        """
        Returns api response for a given author_id
        """
        url = self.AUTHORS + author_id
        return ApiResponse(requests.get(url))

    def jobs(self, job_id: str) -> ApiResponse:
        """
        Returns api response for a given job_id
        """
        url = self.JOBS + job_id
        return ApiResponse(requests.get(url))

    def conferences(self, conference_id: str) -> ApiResponse:
        """
        Returns api response for a given conference_id
        """
        url = self.CONFERENCES + conference_id
        return ApiResponse(requests.get(url))
