import requests

if __name__ == "__main__":
    print("Running E2E test to check the processes information")
    r = requests.get("http://127.0.0.1:5000/info", headers={'Content-Type': 'application/json'})
    assert r.status_code == 200
    assert "Hostname" in r.text
    print("E2E Tests passed")
