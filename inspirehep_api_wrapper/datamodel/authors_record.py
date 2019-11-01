from typing import Dict, Any


class AuthorsRecord:
    """
    Datamodel class for handling author data
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self) -> Dict[str, any]:
        if "metadata" in self.data:
            return self.data["metadata"]
