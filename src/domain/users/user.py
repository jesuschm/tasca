import uuid
from dataclasses import dataclass, asdict, field

@dataclass
class User():
    
    username: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    follows: list = field(default_factory=list)
    
    @classmethod
    def from_dict(self, d):
        return self(**d) if isinstance(d, dict) else None
    
    def to_dict(self):
        return asdict(self)
    
    def add_follow(self, follow_user_id):
        self.follows.append(follow_user_id)