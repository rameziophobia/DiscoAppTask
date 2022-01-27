from shutil import copy
import app
import pytest

@pytest.fixture
def client(tmpdir):
    app.app.config["TESTING"] = True

    with app.app.test_client() as client:
        yield client
