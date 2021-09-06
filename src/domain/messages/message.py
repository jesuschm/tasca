from datetime import datetime
import uuid
import timeago
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
    
    @classmethod
    def print_messages(self, messages, usernames):
        
        for m in messages:
            message = Message.from_dict(m) # A way to validate the message 
            ago = timeago.format(message.created_at, datetime.now())
            username = usernames.get(message.user_id, 'Unknown')
            
            print(f"{username} - {message.content} ({ago})")