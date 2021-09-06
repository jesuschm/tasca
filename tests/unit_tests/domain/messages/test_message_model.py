import pytest
from .fixtures.message_model_fixtures import dummy_message_instance_fixture, dummy_data

class TestMessageModel(object):
    def test_001_from_dict(self, dummy_message_instance_fixture):
        msg = dummy_message_instance_fixture.from_dict(dummy_data)
        assert msg.to_dict() == dummy_data