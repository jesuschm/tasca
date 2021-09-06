import pytest
from uuid import uuid4
import mock
from src.domain.users.user import User
from src.domain.messages.message import Message

@pytest.fixture
def mocked_mongo_repo():
    mocked_repo = mock.Mock()
    mocked_repo.insert_message.return_value = True
    mocked_repo.get_messages.return_value = [Message(content = 'dummy_message', user_id = uuid4()).to_dict()]
    mocked_repo.get_user.return_value = User(username = 'dummy_user').to_dict()
    return mocked_repo