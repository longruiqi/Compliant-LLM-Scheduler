import re
from re import Pattern
from dataclasses import dataclass

_rid_pattern: Pattern = re.compile(
    "ri"
    "\\.(?P<service>[a-z][a-z0-9\\-]*)"
    "\\.(?P<instance>[a-z0-9][a-z0-9\\-]*)?"
    "\\.(?P<type>[a-z][a-z0-9\\-]*)"
)

@dataclass(frozen=True)
class ResourceIdentifier:
    service: str
    instance: str
    type: str

    def __str__(self) -> str:
        return f"ri.{self.service}.{self.instance}.{self.type}"
    
    def __repr__(self) -> str:
        return str(self)
    
    @classmethod
    def from_string(cls, value: str) -> "ResourceIdentifier":
        """
        Return a ResourceIdentifier object if the value can be parsed as a resource identifier
        or raise an error
        """

        match = _rid_pattern.match(value)
        if match:
            return ResourceIdentifier(
                service=match.group("service"),
                instance=match.group("instance"),
                type=match.group("type"))
        else:
            raise ValueError("value can not be parsed as a ResourceIdentifier")
        
    
    