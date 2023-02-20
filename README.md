# Todo Application

<p>
    This Application made with Django and Rest Framework.
    If you have idea, add yours and then send pull request to have better project.
</p>

## Endpoints:

- ***/api/tasks/***
  <p>

This EndPoint will be able to get list of Tasks and
create one.

For getting list of Tasks, use `GET` HTTP Method:

##### because of Authentication, you're able to `get` your own tasks!

```commandline
curl -X GET http://127.0.0.1:8000/api/tasks/  
```

Response:

```json
  [
  {
    "id": 1,
    "title": "first task",
    "body": "Amir",
    "completed": false,
    "created": "2023-02-15T20:11:45.210471Z",
    "updated": "2023-02-15T20:11:45.210548Z"
  }
]
 ```

For create new Task, use `POST` HTTP Method:

##### because of Authentication, you're able to `create` your own task!

```
  curl -X POST -H "Content-Type: application/json" \
  -d '{"title": "title", "body": "Your Data", "completed": false}' \
  http://127.0.0.1:8000/api/tasks/
```

Response:

  ```json
{
  "id": 4,
  "title": "title",
  "body": "Your Data",
  "completed": false,
  "created": "2023-02-18T11:42:02.673197Z",
  "updated": "2023-02-18T11:42:02.673287Z"
}
  ```

</p>

- ***/api/tasks/&lt;pk&gt;/***

<p>
This EndPoint will be able to Retrieve Task, Delete or update that!


For getting Task, use `GET` HTTP Method:

##### because of Authentication, you're able to `get` your own task!

```
  curl -X GET http://127.0.0.1:8000/api/tasks/1/  
```

Response:

```json
  {
  "id": 1,
  "title": "first task",
  "body": "Amir",
  "completed": false,
  "created": "2023-02-15T20:11:45.210471Z",
  "updated": "2023-02-15T20:11:45.210548Z"
}
```

For Update Task, use `PUT` HTTP Method:

##### because of Authentication, you're able to `update` your own task!

```
  curl -X PUT -H "Content-Type: application/json" \
  -d '{"title": "title", "body": "Your Data", "completed": true}' \
  http://127.0.0.1:8000/api/tasks/1/  
```

Response:

```json
{
  "id": 1,
  "title": "title",
  "body": "Your Data",
  "completed": true,
  "created": "2023-02-17T13:25:34.615685Z",
  "updated": "2023-02-18T11:43:54.343544Z"
}
```

For Partial Update Task, use `PATCH` HTTP Method:

##### because of Authentication, you're able to `update` your own task!

```
  curl -X PATCH -H "Content-Type: application/json" \
  -d '{"title": "title updated with partial update"}' \
  http://127.0.0.1:8000/api/tasks/1/
  ```

Response:

```json
{
  "id": 1,
  "title": "title updated with partial update",
  "body": "Your Data",
  "completed": true,
  "created": "2023-02-17T13:25:34.615685Z",
  "updated": "2023-02-18T11:45:57.212193Z"
}
```

For Delete Task, use `DELETE` HTTP Method:

##### because of Authentication, you're able to `delete` your own task!

```
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/  
```

Response:

```
204 Response
```

- ***/accounts/api/register/***

EndPoint to create new user instance with `POST` Http Method:

```
curl -X POST -H "Content-Type: application/json" \
 -d '{"email": "email@example.com", "password1": "your password", "password2": "your password"}' \
 http://127.0.0.1:8000/accounts/api/register/
```

Response:

```json
{
  "email": "email@example.com",
  "first_name": null,
  "last_name": null,
  "birthday": null
}
```

Data that you want wo send to this endpoint should be like following:

```json
{
  "email": {
    "type": "email",
    "required": true,
    "read_only": false,
    "max_length": 250
  },
  "password1": {
    "type": "string",
    "required": true,
    "read_only": false,
    "max_length": 100
  },
  "password2": {
    "type": "string",
    "required": true,
    "read_only": false,
    "max_length": 100
  },
  "first_name": {
    "type": "string",
    "required": false,
    "read_only": false,
    "max_length": 100
  },
  "last_name": {
    "type": "string",
    "required": false,
    "read_only": false,
    "max_length": 100
  },
  "birthday": {
    "type": "date",
    "required": false,
    "read_only": false
  }
}
```

- ***/accounts/api/token/***

EndPoint to get refresh, access and user instance with `POST` HTTP method.

```
curl -X POST \
 -H "Content-Type: application/json" \
 -d'{"email": "amir@gmail.com", "password": "password"}' \
 http://127.0.0.1:8000/accounts/api/token/
```

Response:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NjgwNzM2MiwiaWF0IjoxNjc2NzIwOTYyLCJqdGkiOiI4MmU5YzI3NmM2ZmI0NzdmYWVjMjZjNGYzNDFjY2I0YSIsInVzZXJfaWQiOjF9.mmVudtHIOub_okskM-0FbWOPyXwXgnDQc_YYRijHTlA",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2NzIxNTYyLCJpYXQiOjE2NzY3MjA5NjIsImp0aSI6ImY4ZmY1YjRkOWY1NzQ1NmQ4ZjJhZmUwNTkwMGY1YTE2IiwidXNlcl9pZCI6MX0.14lyypcYv0tm-HeeyeGOfr9OrNHBhp7QWVmBSq4S3Hw",
  "user": {
    "email": "amir@gmail.com",
    "first_name": null,
    "last_name": null
  }
}
```

- ***/accounts/api/token/refresh/***

Endpoint to get new access token by HTTP `POST` Method:

```
curl -X POST \
 -H "Content-Type: application/json" \
 -d '{"refresh": "your refresh token"}' \
 http://127.0.0.1:8000/accounts/api/token/refresh/
```

Response:

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2NzIxNzYxLCJpYXQiOjE2NzY3MjA5NjIsImp0aSI6IjZmNWNhNjllYmU0ZDQzYTg4OTkyNmE0ZmRjNjNkNjNlIiwidXNlcl9pZCI6MX0.uPNp27IrDJYgoYVTD2Xe_HmcjgX-KnBp5V5hY_j1Qco"
}
```

- ***/accounts/api/token/verify/***

Send your access or refresh token to this Endpoint with `token` Key and if token is valid, you get
`HTTP 200 OK` Response and if not, you get `HTTP 401 Unauthorized`

```
curl -X POST \
 -H "Content-Type: application/json" \
 -d '{"token": "your token"}' \
 http://127.0.0.1:8000/accounts/api/token/verify/
```

  </p>

## Have Todo:

- [x] Configure Model layer
- [x] Make Endpoints for making new tasks
- [x] Create Custom User Model
- [x] Add JWT Authentication
- [ ] Email confirmation Stage
- [ ] Password Forget section and work with sending email in django
- [ ] Make Profile for users
- [ ] Make Front-End View With React and Bootstrap
- [ ] Publish project into server
- [ ] Work with Redis in server
- [ ] Work With Docker

## Usage:

- clone the Project:

```commandline
git clone https://github.com/Amirmahdikahdouii/Todo-App-DRF.git
```

- Go to the Directory created:

```commandline
cd Todo-App-DRF
```

- make virtual Environment:

``` commandline
python -m venv .venv 
```

- (Linux) Active your venv:

```commandline
source ./venv/bin/activate
```

- install requirements:

```
pip install requirements.txt
```

##### if you have problem with installation use command below:

```
pip install -r requirements.txt
```

- migrate all the changes:

```commandline
python manage.py migrate
```

- run & enjoy:

```
python manage.py runserver 
```

## Support me

Please give Star to this Repo and make sure you have followed my account for more.
Thanks :heart:
