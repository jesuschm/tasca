from src.application.commands_service import post, read, follow, wall
from .fixtures.commands_service_fixtures import mocked_mongo_repo

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