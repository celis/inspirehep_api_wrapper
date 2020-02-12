from typing import Dict, Any


class ConferencesRecord:
    """
    Datamodel class to handle conferences data
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