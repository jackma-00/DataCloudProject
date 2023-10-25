import json
import zipfile
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Loading sample data
zip_file_path = "./src/data/sample.zip"
sample = {"file": ("sample.zip", open(zip_file_path, "rb"))}

# Declaring expected output data
expected_output = {"response": "ok"}


def test_predict_single_data_point():
    response = client.post("/unzip", files=sample, json=pipeline)
    assert response.status_code == 200
    assert response.json() == expected_output
