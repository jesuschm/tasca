import pytest
import mock
from src.application.commands_service import post, read, follow, wall

@pytest.fixture
def mocked_mongo_repo():
    mocked_repo = mock.Mock()
    mocked_repo.insert_message.return_value = True
    mocked_repo.get_messages.return_value = ['dummy_message']
    return mocked_repo
    
class TestCommandsService(object):
    def test_001_post(self, mocked_mongo_repo):
        rc = post(repo = mocked_mongo_repo, user = 'dummy_user', message = 'dummy_message')
        assert rc
    def test_002_post(self, mocked_mongo_repo):
        rc = read(repo = mocked_mongo_repo, user = 'dummy_user')
        assert rc
    def test_003_follow(self, mocked_mongo_repo):
        rc = follow(repo = mocked_mongo_repo, user = 'dummy_user', follow = 'dummy_user_2')
        assert rc
    def test_004_wall(self, mocked_mongo_repo):
        rc = wall(repo = mocked_mongo_repo, user = 'dummy_user')
        assert rc