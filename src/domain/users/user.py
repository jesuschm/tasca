import uuid
from dataclasses import dataclass, asdict, field

@dataclass
class User():
    
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    follows: list = field(default_factory=list)
    
    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        return asdict(self)