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

### paste your Token with "your_token_here" in commands above!

For getting list of Tasks, use `GET` HTTP Method:

##### because of Authentication, you're able to `get` your own tasks!

```
curl -X GET -H "Authorization: Token your_token_here" http://127.0.0.1:8000/tasks/api-tasks/
```

Response:

```json
[
  {
    "id": 7,
    "title": "title",
    "body": "body",
    "completed": false,
    "created": "2023-02-18T19:51:05.819786Z",
    "updated": "2023-02-18T19:51:05.819869Z",
    "user": {
      "email": "amir@gmail.com",
      "first_name": null,
      "last_name": null
    }
  }
]
 ```

For create new Task, use `POST` HTTP Method:

##### because of Authentication, you're able to `create` your own task!

```
  curl -X POST -H "Content-Type: application/json" \
  -H "Authorization: Token your_token_here" \
  -d '{"title": "title", "body": "Your Data", "completed": false}' \
  http://127.0.0.1:8000/tasks/api-tasks/
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
  curl -X GET -H "Authorization: Token your_token_here" http://127.0.0.1:8000/tasks/api-tasks/1/
```

Response:

```json
{
  "id": 1,
  "title": "title",
  "body": "Your Data",
  "completed": false,
  "created": "2023-02-24T20:50:11.277838Z",
  "updated": "2023-02-24T20:50:11.277922Z",
  "user": {
    "email": "amir@gmail.com",
    "first_name": null,
    "last_name": null
  }
}
```

For Update Task, use `PUT` HTTP Method:

##### because of Authentication, you're able to `update` your own task!

```
  curl -X PUT -H "Content-Type: application/json" \
  -H "Authorization: Token your_token_here" \
  -d '{"title": "title Updated", "body": "Your Data Updated", "completed": false}' \
  http://127.0.0.1:8000/tasks/api-tasks/1/ 
```

Response:

```json
{
  "id": 1,
  "title": "title Updated",
  "body": "Your Data Updated",
  "completed": false,
  "created": "2023-02-24T20:50:11.277838Z",
  "updated": "2023-02-24T21:22:05.206567Z",
  "user": {
    "email": "amir@gmail.com",
    "first_name": null,
    "last_name": null
  }
}
```

For Partial Update Task, use `PATCH` HTTP Method:

##### because of Authentication, you're able to `update` your own task!

```
  curl -X PATCH -H "Content-Type: application/json" \
  -H "Authorization: Token your_token_here" \
  -d '{"completed": true}' \
  http://127.0.0.1:8000/tasks/api-tasks/1/ 
  ```

Response:

```json
{
  "id": 1,
  "title": "title Updated",
  "body": "Your Data Updated",
  "completed": true,
  "created": "2023-02-24T20:50:11.277838Z",
  "updated": "2023-02-24T21:23:30.710451Z",
  "user": {
    "email": "amir@gmail.com",
    "first_name": null,
    "last_name": null
  }
}
```

For Delete Task, use `DELETE` HTTP Method:

##### because of Authentication, you're able to `delete` your own task!

```
curl -X DELETE \
 -H "Authorization: Token your_token_here" \
 http://127.0.0.1:8000/tasks/api-tasks/1/  
```

Response:

```
204 Response
```

- ***/accounts/api/email-verify/send-verification-key/***

This EndPoint is build to send verification email to users,
allowed method is HTTP `post` method and send email to this endpoint,
to send verification code to user email!

Request data:

```json
{
  "email": "user@email.com"
}
```

Fetch Example:

```
curl -X POST -H "Content-Type: application/json" \
 -d '{"email": "user@gmail.com"}' \
 http:/127.0.0.1:8000/accounts/api/email-verify/send-verification-key/  
```

- ***/accounts/api/email-verify/send-verification-key/***

This EndPoint is build to confirm verification email by users,
allowed method is HTTP `put` method and send email and verify_key to this endpoint,
to verify user email!

Request Data:

```json
{
  "email": "user@email.com",
  "verify_key": "verify_key like: 123456"
}
```

Fetch Example:

```
curl -X PUT -H "Content-Type: application/json" \
 -d '{"email": "user@gmail.com", "verify_key": "801730"}' \
 http:/127.0.0.1:8000/accounts/api/email-verify/confirm-verification-key/  
```

- ***/accounts/api/register/***

EndPoint to create new user instance with `POST` Http Method:

### user should verify email first, to register his account!

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
- [x] Email Verification Stage
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
