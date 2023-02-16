# Todo Application

<p>
    This Application made with Django and Rest Framework.
    If you have idea, add yours and then send pull request to have better project.
</p>

## Endpoints:

- /api/tasks/ <br>
  <p>
  This EndPoint will be able to get list of Tasks and
  create one.
  For getting list of Tasks, use GET HTTP Method:
  <br>
  <code>
  $ curl -X GET http://127.0.0.1:8000/api/tasks/  
  </code>
  <br>
  Response:
  <code>
  [ <br>
  {"id":1,"title":"first task","body":"Amir","completed":false,"created":"2023-02-15T20:11:45.210471Z","updated":"2023-02-15T20:11:45.210548Z"}
  <br> ]
  </code>
  <br>
  For create new Task, use POST HTTP Method:
  <br>
  <code>
  $ curl -X POST -d '{"title": "title", "body": "Your Data", "completed": false}' http://127.0.0.1:8000/api/tasks  
  </code>
  <br>
  Response:
  <code>
  {"title": "title", "body": "Your Data", "completed": false}
  </code>
  </p>
- /api/tasks/&lt;pk&gt;
<p>
  This EndPoint will be able to Retrieve Task, Delete or update that!
  For getting Task, use GET HTTP Method:
  <br>
  <code>
  $ curl -X GET http://127.0.0.1:8000/api/tasks/1  
  </code>
  <br>
  Response:
  <code>
  {"id":1,"title":"first task","body":"Amir","completed":false,"created":"2023-02-15T20:11:45.210471Z","updated":"2023-02-15T20:11:45.210548Z"}
  </code>
  <br>
  For Update Task, use PUT HTTP Method:
  <br>
  <code>
  $ curl -X PUT -d '{"title": "title", "body": "Your Data", "completed": false}' http://127.0.0.1:8000/api/tasks/1  
  </code>
  <br>
  Response:
  <code>
  {"title": "title", "body": "Your Data", "completed": false}
  </code>
  <br>
  For Partial Update Task, use PATCH HTTP Method:
  <br>
  <code>
  $ curl -X PATCH -d '{"completed": true}' http://127.0.0.1:8000/api/tasks/1  
  </code>
  <br>
  Response:
  <code>
  {"title": "title", "body": "Your Data", "completed": false}
  </code>
  <br>
  For Delete Task, use DELETE HTTP Method:
  <br>
  <code>
  $ curl -X DELETE http://127.0.0.1:8000/api/tasks/1  
  </code>
  <br>
  Response:
  <code>
  204 Response
  </code>
  </p>

## Have Todo:

- [x] Configure Model layer
- [x] Make Endpoints for making new tasks
- [ ] Add JWT Authentication
- [ ] Make Profile for users
- [ ] Make Front-End View With React and Bootstrap
- [ ] Publish project into server
- [ ] Work with Redis in server
- [ ] Work With Docker

## Usage:

- make new Directory: <code>mkdir Todo-App </code>
- Go to the Directory you created: <code> cd Todo-App </code>
- make virtual Environment: <code> python -m venv .venv </code>
- (Linux) Active your venv: <code> source ./venv/bin/activate </code>
- clone the Project: <code> git clone https://github.com/Amirmahdikahdouii/Todo-App-DRF.git </code>
- install requirements: <code> pip install requirements.txt </code>
- migrate all the changes: <code> python manage.py migrate </code>
- run & enjoy: <code> python manage.py runserver </code>

## Support me

Please give Star to this Repo and make sure you have followed my account for more.
Thanks!
