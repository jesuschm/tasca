from datetime import datetime
import uuid
from datetime import datetime
from dataclasses import dataclass, asdict, field

@dataclass
class Message():
    
    content: str
    user_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = datetime.now()
    
    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        return asdict(self)