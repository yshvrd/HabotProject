# Habot - hiring project (Python Backend Developer)

A FastAPI-based backend implementing employee management with JWT authentication and PostgreSQL.


## Run locally - 

1. Clone the repository 
```bash
git clone https://github.com/yshvrd/HabotProject
cd HabotProject
```

2. Create and a run a virtual environment 
```bash
python3 -m venv .venv 
source .venv/bin/activate  #mac
```

3. install dependencies 
```bash
pip install -r requirements.txt
```

4. Run the DB and create table

```bash
docker run -d \
  --name habot-db \
  -e POSTGRES_USER=habot \
  -e POSTGRES_PASSWORD=habot \
  -e POSTGRES_DB=habot-db \
  -p 5432:5432 \
  postgres:16
```
```bash
cd Backend 
python -m db.create_table 
```

5. Run the server 
```bash
uvicorn app:app --reload
```


See [Tests Documentation](backend/tests/README.md) for details on running and understanding the test suite.


## Test Endpoints

1. generate auth token 
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin"}'
```

- Returns a JWT access token
- Required for accessing protected endpoints

![](assets/01.png)


2. employees endpoint(without auth)

```bash
curl -X POST http://127.0.0.1:8000/api/employees/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Me","email":"me@test.com"}'
```

- Does not work 
- Returns 401 Unauthorized

![](assets/02.png)


3. Create Employee
```bash
curl -X POST http://127.0.0.1:8000/api/employees/ \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@test.com"}'
```

- Creates a new employee
- Returns 201 Created
- Duplicate email returns 400 Bad Request

![](assets/03.png)

4. List Employees
```bash
# get all
curl http://127.0.0.1:8000/api/employees/ \
  -H "Authorization: Bearer <TOKEN>"
```
```bash
# get employee by ID
curl http://127.0.0.1:8000/api/employees/<EMPLOYEE_ID> \
  -H "Authorization: Bearer <TOKEN>"
```
```bash
# list employees (pagination)
curl http://127.0.0.1:8000/api/employees/?page=2 \
  -H "Authorization: Bearer <TOKEN>"
```
```bash
# list employees (filter by)
curl http://127.0.0.1:8000/api/employees/?department=Engineering \
  -H "Authorization: Bearer <TOKEN>"

```

5. Update Employee
```bash
curl -X PUT http://127.0.0.1:8000/api/employees/<EMPLOYEE_ID> \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"role":"Manager"}'
```
- Updates provided fields only
- Returns updated employee data

6. Delete Employee
```bash
curl -X DELETE http://127.0.0.1:8000/api/employees/<EMPLOYEE_ID> \
  -H "Authorization: Bearer <TOKEN>"
```
- Deletes the employee
- Returns 204 No Content




