from src.application.commands_service import post, read, follow, wall

class TestCommandsService(object):
    def test_001_post(self):
        rc = post(user = 'dummy_user', message = 'dummy_message')
        assert rc
    def test_002_post(self):
        rc = read(user = 'dummy_user')
        assert rc
    def test_003_follow(self):
        rc = follow(user = 'dummy_user', follow = 'dummy_user_2')
        assert rc
    def test_004_wall(self):
        rc = wall(user = 'dummy_user')
        assert rc