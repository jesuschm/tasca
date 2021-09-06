import pytest
from .fixtures.mongo_repo_fixtures import mongo_repo_instance_fixture, bad_data

class TestMongoRepository(object):
    
    @pytest.mark.parametrize(
        'data',
        [pytest.param(bad_data, marks=pytest.mark.xfail)]
    )
    def test001_upsert(self, data, mongo_repo_instance_fixture):
        rc = mongo_repo_instance_fixture.upsert(collection= 'tests_database', data = data, pk_field = 'bad_id')
        assert rc