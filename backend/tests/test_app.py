from app import app

def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Hello from Backend!"

def test_database():
    client = app.test_client()

    response = client.get("/db")

    body = response.get_data(as_text=True)
    assert response.status_code == 200, body

    assert response.status_code == 200
    assert "Connected to PostgreSQL" in response.get_data(as_text=True)
