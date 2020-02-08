from typing import Dict, Any


class JobsRecord:
    """
    Datamodel class to handle job data
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
