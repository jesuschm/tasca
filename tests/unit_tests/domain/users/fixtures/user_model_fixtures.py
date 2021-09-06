import pytest
import uuid
from src.domain.users.user import User
from dataclasses import asdict, dataclass

dummy_data = {
    'id': uuid.uuid4(),
    'username': 'dummy_name',
    'follows': []
}

@pytest.fixture
def dummy_user_instance_fixture():
    dummy_user_instance_fixture = User(id = dummy_data.get('id'), username= dummy_data.get('username'))
    return dummy_user_instance_fixture