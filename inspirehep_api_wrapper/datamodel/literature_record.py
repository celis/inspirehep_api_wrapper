from typing import Dict, Any, List


class LiteratureRecord:
    """
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self):
        if "metadata" in self.data:
            return self.data["metadata"]

    def references(self) -> List[str]:
        if self.metadata and self.metadata.get("references"):
            return [
                element["record"]["$ref"].split("/")[-1]
                for element in self.metadata["references"]
                if element.get("record")
            ]
