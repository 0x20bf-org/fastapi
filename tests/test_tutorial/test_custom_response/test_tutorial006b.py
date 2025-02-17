from docs_src.custom_response.tutorial006b import app
from fastapi.testclient import TestClient

client = TestClient(app)


openapi_schema = {
    "openapi": "3.0.2",
    "info": {"title": "FastAPI", "version": "0.1.0"},
    "paths": {
        "/fastapi": {
            "get": {
                "summary": "Redirect Fastapi",
                "operationId": "redirect_fastapi_fastapi_get",
                "responses": {"307": {"description": "Successful Response"}},
            }
        }
    },
}


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == openapi_schema


def test_redirect_response_class():
    response = client.get("/fastapi", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://fastapi.tiangolo.com"
