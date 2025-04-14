import requests

def test_nso_is_alive():
    response = requests.get("http://localhost:8081/", auth=("admin", "admin"))
    assert response.status_code == 200
