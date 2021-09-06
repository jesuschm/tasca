import pytest
from .fixtures.user_model_fixtures import dummy_user_instance_fixture, dummy_data

class TestUserModel(object):
    def test_001_from_dict(self, dummy_user_instance_fixture):
        user = dummy_user_instance_fixture.from_dict(dummy_data)
        assert user.to_dict() == dummy_data