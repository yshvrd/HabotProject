from fastapi import status

def get_auth_headers(client):
    #Helper function, gets Authorization header for protected endpoints.
    response = client.post(
        "/api/auth/token",
        json={"username": "admin", "password": "admin"},
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# test employee creation 
# outcome - pass
def test_create_employee(client):
    headers = get_auth_headers(client)

    response = client.post(
        "/api/employees/",
        json={
            "name": "Alice",
            "email": "alice@test.com",
            "department": "Engineering",
            "role": "Developer",
        },
        headers=headers,
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Alice"
    assert data["email"] == "alice@test.com"
    assert "id" in data



# test duplicate email 
# outcome - fail
def test_duplicate_email(client):
    headers = get_auth_headers(client)

    # First creation
    client.post(
        "/api/employees/",
        json={
            "name": "Bob",
            "email": "bob@test.com",
        },
        headers=headers,
    )
    # Duplicate email
    response = client.post(
        "/api/employees/",
        json={
            "name": "Bob 2",
            "email": "bob@test.com",
        },
        headers=headers,
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# test list employee endpoint 
def test_list_employees(client):
    headers = get_auth_headers(client)

    response = client.get(
        "/api/employees/",
        headers=headers,
    )
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


# test get employee by id endpoint
def test_get_employee_by_id(client):
    headers = get_auth_headers(client)

    create_resp = client.post(
        "/api/employees/",
        json={"name": "Charlie", "email": "charlie@test.com"},
        headers=headers,
    )
    emp_id = create_resp.json()["id"]

    response = client.get(
        f"/api/employees/{emp_id}",
        headers=headers,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == emp_id



# test update employee endpoint 
def test_update_employee(client):
    headers = get_auth_headers(client)

    create_resp = client.post(
        "/api/employees/",
        json={"name": "Dave", "email": "dave@test.com"},
        headers=headers,
    )
    emp_id = create_resp.json()["id"]

    response = client.put(
        f"/api/employees/{emp_id}",
        json={"role": "Manager"},
        headers=headers,
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["role"] == "Manager"



# test delete employee endpoint 
def test_delete_employee(client):
    headers = get_auth_headers(client)

    create_resp = client.post(
        "/api/employees/",
        json={"name": "Eve", "email": "eve@test.com"},
        headers=headers,
    )
    emp_id = create_resp.json()["id"]

    response = client.delete(
        f"/api/employees/{emp_id}",
        headers=headers,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

