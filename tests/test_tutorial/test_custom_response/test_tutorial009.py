from pathlib import Path

from docs_src.custom_response import tutorial009
from docs_src.custom_response.tutorial009 import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get(tmp_path: Path):
    file_path: Path = tmp_path / "large-video-file.mp4"
    tutorial009.some_file_path = str(file_path)
    test_content = b"Fake video bytes"
    file_path.write_bytes(test_content)
    response = client.get("/")
    assert response.content == test_content
