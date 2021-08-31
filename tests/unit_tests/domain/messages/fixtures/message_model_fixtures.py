import pytest
import uuid
from datetime import datetime
from src.domain.messages.message import Message
from dataclasses import asdict, dataclass

dummy_data = {
    'id': uuid.uuid4,
    'user_id': uuid.uuid4,
    'content': 'dummy_message',
    'created_at': datetime.now()
}
@pytest.fixture
def dummy_message_instance_fixture():
    dummy_message_instance_fixture = Message(id = dummy_data.get('id'), user_id= dummy_data.get('user_id'), content = dummy_data.get('content'), created_at = dummy_data.get('created_at'))
    return dummy_message_instance_fixture