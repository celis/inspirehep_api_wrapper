from requests import Response
from inspirehep_api_wrapper.datamodel.jobs_record import JobsRecord
from typing import Dict, Any


class JobsResponse:
    """
    """

    def __init__(self, api_jobs_response: Response):
        self.api_jobs_response = api_jobs_response

    @property
    def data(self) -> Dict[str, Any]:
        return self.api_jobs_response.json()

    def to_record(self):
        return JobsRecord(self.data)
