from docs_src.response_cookies.tutorial001 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_path_operation():
    response = client.post("/cookie/")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Come to the dark side, we have cookies"}
    assert response.cookies["fakesession"] == "fake-cookie-session-value"
