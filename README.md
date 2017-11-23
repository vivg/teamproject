# Team Api
Simple api to add, modify, delete and list members of a team

## Installation
- Create a new virtualenv and switch to it.
- Clone the repository and install the requirements
```
$ git clone https://github.com/vivg/teamproject
$ cd teamproject
$ pip install -r requirements.txt
```
- Update database credentials in teamproject/settings.py
- Run migrations
```
$ python manage.py migrate
```
- Run the server
```
$ python manage.py runserver
```

## Available APIs
| API endpoints        | Method    | Description                      |
|----------------------|-----------|----------------------------------|
| /members/            | GET       | Returns a list team members      |
| /members/            | POST      | Add a new member to the team     |
| /members/{id}/       | PATCH     | Edit a team member               |
| /members/{id}/       | DELETE    | Delete a team member             |

### Usage Example
**Endpoint:** `GET /members/`
```
$ curl -X GET \
    -H "Content-Type: application/json" \
    http://127.0.0.1:8000/api/members/
```

**Endpoint:** `POST /members/`
```
$ curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"first_name": "Vivek", "last_name": "Gupta", "email": "vivek@fakemail.com", "phone": "+1234567890", "role": "admin"}' \
    http://localhost:8000/api/members/
```

**Endpoint:** `PATCH /team/{id}/`
```
$ curl -X PATCH \
    -H "Content-Type: application/json" \
    -d '{"email": "mail@vivekgupta.com", "phone": "+1234567890", "role": "regular"} ' \
    http://127.0.0.1:8000/api/members/1/
```

**Endpoint:** `DELETE /team/{id}/`
```
$ curl -X DELETE \
    -H "Content-Type: application/json" \
    http://127.0.0.1:8000/api/members/1/
```