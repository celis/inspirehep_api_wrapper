import requests
from inspirehep_api_wrapper.datamodel.api_response import ApiResponse, SearchAPIResponse
from os.path import join
from typing import Dict


class InspireAPI:
    """
    Simple wrapper around the INSPIRE API

    https://labs.inspirehep.net

    methods:
       search: search queries at any endpoint
       literature: retrieves particular documents from the literature endpoint
       authors: retrieves particular documents from theauthors endpoint
       jobs: retrieves particular documents from thejobs endpoint
       conferences: retrieves particular documents from the conferences endpoint
    """

    API = "https://labs.inspirehep.net/api"
    LITERATURE = "literature"
    AUTHORS = "authors"
    JOBS = "jobs"
    CONFERENCES = "conferences"

    def __init__(self):
        self.endpoints = [self.LITERATURE, self.AUTHORS, self.JOBS, self.CONFERENCES]

    def search(self, endpoint: str, query: str, params: Dict = None) -> SearchAPIResponse:
        """
        search query

        :param endpoint:
        :param q:
        :return:
        """
        parameters = {"q": query}
        if params:
            parameters.update(params)
        url = join(self.API, endpoint)
        return SearchAPIResponse(requests.get(url, parameters))

    def literature(self, record_id: str) -> ApiResponse:
        """
        Returns api response for a given record_id
        """
        url = join(self.API, self.LITERATURE, record_id)
        return ApiResponse(requests.get(url))

    def authors(self, author_id: str) -> ApiResponse:
        """
        Returns api response for a given author_id
        """
        url = join(self.API, self.AUTHORS, author_id)
        return ApiResponse(requests.get(url))

    def jobs(self, job_id: str) -> ApiResponse:
        """
        Returns api response for a given job_id
        """
        url = join(self.API, self.JOBS, job_id)
        return ApiResponse(requests.get(url))

    def conferences(self, conference_id: str) -> ApiResponse:
        """
        Returns api response for a given conference_id
        """
        url = join(self.API, self.CONFERENCES, conference_id)
        return ApiResponse(requests.get(url))
