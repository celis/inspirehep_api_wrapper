from typing import Dict, Any, List


class JobsRecord:
    """
    """

    def __init__(self, data: Dict[str, Any]):
        self.data = data

    @property
    def metadata(self):
        if "metadata" in self.data:
            return self.data["metadata"]
