import requests
from inspirehep_api_wrapper.datamodel.literature_response import LiteratureResponse
from inspirehep_api_wrapper.datamodel.authors_response import AuthorsResponse
from inspirehep_api_wrapper.datamodel.jobs_response import JobsResponse


class InspireAPI:
    """
    Simple wrapper around the INSPIRE API

    https://labs.inspirehep.net

    methods:
       literature: gives access to the literature endpoint
       authors: gives access to the authors endpoint
       jobs: gives access to the jobs endpoint
    """

    LITERATURE = "https://labs.inspirehep.net/api/literature/"
    AUTHORS = "https://labs.inspirehep.net/api/authors/"
    JOBS = "https://labs.inspirehep.net/api/jobs/"

    def __init__(self):
        pass

    def literature(self, record_id: str) -> LiteratureResponse:
        """
        Returns api response for a given record_id
        """
        url = self.LITERATURE + record_id
        return LiteratureResponse(requests.get(url))

    def authors(self, author_id: str) -> AuthorsResponse:
        """
        Returns api response for a given author_id
        """
        url = self.AUTHORS + author_id
        return AuthorsResponse(requests.get(url))

    def jobs(self, job_id: str) -> JobsResponse:
        """
        Returns api response for a given job_id
        """
        url = self.JOBS + job_id
        return JobsResponse(requests.get(url))
