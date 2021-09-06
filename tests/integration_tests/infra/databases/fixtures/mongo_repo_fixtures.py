import pytest
from src.infra.databases.mongo import MongoRepository

bad_data = {
    'good_id': 1
}


@pytest.fixture
def mongo_repo_instance_fixture():
    repo = MongoRepository()
    return repo
