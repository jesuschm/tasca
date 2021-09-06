import pytest
from uuid import uuid4
import mock
from src.application.commands_service import post, read, follow, wall
from src.domain.users.user import User
from src.domain.messages.message import Message

@pytest.fixture
def mocked_mongo_repo():
    mocked_repo = mock.Mock()
    mocked_repo.insert_message.return_value = True
    mocked_repo.get_messages.return_value = [Message(content = 'dummy_message', user_id = uuid4()).to_dict()]
    mocked_repo.get_user.return_value = User(username = 'dummy_user').to_dict()
    return mocked_repo
    
class TestCommandsService(object):
    def test_001_post(self, mocked_mongo_repo):
        rc = post(repo = mocked_mongo_repo, username = 'dummy_user', message = 'dummy_message')
        assert rc
    def test_002_read(self, mocked_mongo_repo):
        rc = read(repo = mocked_mongo_repo, username = 'dummy_user')
        assert rc
    def test_003_follow(self, mocked_mongo_repo):
        rc = follow(repo = mocked_mongo_repo, username = 'dummy_user', follow_username = 'dummy_user_2')
        assert rc
    def test_004_wall(self, mocked_mongo_repo):
        rc = wall(repo = mocked_mongo_repo, username = 'dummy_user')
        assert rc