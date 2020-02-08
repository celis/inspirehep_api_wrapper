from typing import Any, List, Dict


class LiteratureRecord:
    """
    Datamodel class for handling literature record data,
    implementing basic methods to access the properties
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self) -> Dict[str, Any]:
        """
        Returns raw metadata provided by INSPIRE as a Dict
        """
        if "metadata" in self.data:
            return self.data["metadata"]

    @property
    def references(self) -> List[str]:
        """
        Returns reference list of the article as a List of INSPIRE article ids,
        ordered in the order of appearance.
        """
        if self.metadata and self.metadata.get("references"):
            return [
                element["record"]["$ref"].split("/")[-1]
                for element in self.metadata["references"]
                if element.get("record")
            ]

    @property
    def preprint_date(self) -> str:
        """
        Returns date of the preprint
        """
        if "preprint_date" in self.metadata:
            return f"({self.metadata['preprint_date']})"

    @property
    def authors(self) -> List[str]:
        """
        Returns the article authors.
        """
        if "authors" in self.metadata:
            return [author.get("full_name") for author in self.metadata["authors"]]

    @property
    def doi(self) -> str:
        """
        Returns the article DOI code
        """
        if "dois" in self.metadata:
            return self.metadata["dois"][0].get("value")

    @property
    def arxiv(self) -> Dict[str, str]:
        """
        Returns the article arXiv data (eprint number and url)
        """
        if "arxiv_eprints" in self.metadata:
            return {
                "eprint": self.metadata["arxiv_eprints"][0].get("value"),
                "url": "https://arxiv.org/abs/"
                + self.metadata["arxiv_eprints"][0].get("value"),
            }

    @property
    def title(self) -> str:
        """
        Returns title as it appears on INSPIRE
        (some articles title differ when published on a journal compared to the preprint)
        """
        if "titles" in self.metadata:
            return self.metadata["titles"][0].get("title")

    @property
    def journal(self) -> Dict[str, Any]:
        """
        Returns journal information about the article
        """
        if "publication_info" in self.metadata:
            return {
                "title": self.metadata["publication_info"][0].get("journal_title"),
                "volume": self.metadata["publication_info"][0].get("journal_volume"),
                "page_start": self.metadata["publication_info"][0].get("page_start"),
                "year": self.metadata["publication_info"][0].get("year"),
            }
