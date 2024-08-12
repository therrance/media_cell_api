from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_action_by_codeword():
    response = client.get("/action/5001")
    assert response.status_code == 200
    assert response.json() == {"codeword": 5001, "action_id": "alert"}

def test_read_action_by_codeword_not_found():
    response = client.get("/action/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Codeword not found"}

def test_read_action_by_codeword_invalid_input():
    response = client.get("/action/invalid")
    assert response.status_code == 422

def test_read_action_by_codeword_empty_input():
    response = client.get("/action/")
    assert response.status_code == 404

def test_read_codewords_by_action_id():
    response = client.get("/codewords/alert")
    assert response.status_code == 200
    expected_response = {"action_id": "alert", "codewords": [5001, 5003]}
    assert set(response.json()["codewords"]) == {5001, 5003}

def test_read_codewords_by_action_id_not_found():
    response = client.get("/codewords/unknown")
    assert response.status_code == 404
    assert response.json() == {"detail": "Action ID not found"}

def test_read_codewords_by_action_id_multiple_codewords():
    response = client.get("/codewords/alert")
    assert response.status_code == 200
    expected_response = {"action_id": "alert", "codewords": [5001, 5003]}
    assert set(response.json()["codewords"]) == {5001, 5003}

def test_read_codewords_by_action_id_empty_input():
    response = client.get("/codewords/")
    assert response.status_code == 404

def test_read_codewords_by_action_id_case_sensitivity():
    response = client.get("/codewords/ALERT")
    assert response.status_code == 404

def test_read_action_by_codeword_zero():
    response = client.get("/action/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Codeword not found"}