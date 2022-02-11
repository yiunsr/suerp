import os
import sys
import json
import unittest 
import pytest
import asynctest
from sqlalchemy import event
from fastapi import FastAPI
from fastapi.testclient import TestClient
try:
    import pathmagic  # noqa
except Exception:
    from . import pathmagic  # noqa

FASTAPI_CONFIG = 'unittest'
os.environ["FASTAPI_CONFIG"] = FASTAPI_CONFIG

@pytest.mark.usefixtures("event_loop", "app", "engine", "db_session")
class TestUser01(asynctest.TestCase):
    fixture_names = ("engine", "db_session")

    @pytest.mark.asyncio
    async def test_singup(self):
        data = dict(
            email="test0100@test.com", name="test0100",
            first_name="first0100", last_name="last0100",
            password="Test0100")
        response = await self.client.post("/users/singup", json=data)
        assert response.status_code == 201

    # def test_read_main(self):
    #     response = self.client.get("/")
    #     assert response.status_code == 200
    #     assert response.json() == {"url": "main.root"}

    # def test_user_list(self):
    #     response = client.get("/")
    #     assert response.status_code == 200
    #     assert response.json() == {"msg": "Hello World"}

if __name__ == "__main__":
    sys.exit(
        pytest.main(
            ["-qq", "--asyncio-mode=strict"], plugins=[TestUser01()]))
