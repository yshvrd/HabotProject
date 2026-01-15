from fastapi import status


def test_get_token_success(client):
    # valid creds
    # outcome - pass 
    response = client.post(
        "/api/auth/token",
        json={"username": "admin", "password": "admin"},
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_get_token_invalid_credentials(client):
    # Invalid credentials
    # outcome - fail/rejected
    response = client.post(
        "/api/auth/token",
        json={"username": "admin", "password": "wrong"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_protected_route_without_token(client):
    # Accessing a protected endpoint without a token
    # outcome - fail

    response = client.get("/api/employees/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
