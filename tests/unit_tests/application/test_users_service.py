import pytest
import mock
from src.application.users_service import create_user, get_user

@pytest.fixture
def mocked_mongo_repo():
    mocked_repo = mock.Mock()
    mocked_repo.create_user.return_value = True
    mocked_repo.get_user.return_value = ['dummy_user']
    return mocked_repo
    
class TestUsersService(object):
    def test_001_create_user(self, mocked_mongo_repo):
        rc = create_user(repo = mocked_mongo_repo, username = 'dummy_user')
        assert rc
    def test_002_get_user(self, mocked_mongo_repo):
        rc = get_user(repo = mocked_mongo_repo, username = 'dummy_user')
        assert rc