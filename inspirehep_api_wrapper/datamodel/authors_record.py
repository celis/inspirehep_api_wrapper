from typing import Dict, Any


class AuthorsRecord:
    """
    Datamodel class for handling author data
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self) -> Dict[str, any]:
        """
        Returns raw metadata provided by INSPIRE as a Dict
        """
        if "metadata" in self.data:
            return self.data["metadata"]
