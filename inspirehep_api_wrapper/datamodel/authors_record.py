from typing import Dict, Any, List


class AuthorsRecord:
    """
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self):
        if "metadata" in self.data:
            return self.data["metadata"]
