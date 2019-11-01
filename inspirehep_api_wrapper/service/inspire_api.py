import requests
from inspirehep_api_wrapper.datamodel.literature_response import LiteratureResponse
from inspirehep_api_wrapper.datamodel.authors_response import AuthorsResponse
from inspirehep_api_wrapper.datamodel.jobs_response import JobsResponse


class InspireAPI:
    """
    Wrapper around the inspire api
    """

    LITERATURE = "https://labs.inspirehep.net/api/literature/"
    AUTHORS = "https://labs.inspirehep.net/api/authors/"
    JOBS = "https://labs.inspirehep.net/api/jobs/"

    def __init__(self):
        pass

    def literature(self, record_id: str) -> LiteratureResponse:
        """
        :param record_id:
        :return:
        """
        url = self.LITERATURE + record_id
        return LiteratureResponse(requests.get(url))

    def authors(self, author_id: str) -> AuthorsResponse:
        """
        :return:
        """
        url = self.AUTHORS + author_id
        return AuthorsResponse(requests.get(url))

    def jobs(self, job_id: str) -> JobsResponse:
        """
        :return:
        """
        url = self.JOBS + job_id
        return JobsResponse(requests.get(url))
