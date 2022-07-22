# ToDoler is an ToDO API built with FastAPI

This repo contains 3 main folders which is 3 different APIs
- basic
- intermediate
- advanced

These 3 folders are kind of the level of FastAPI included in the APIs.

The basic API has some basic FastAPI features, ... and so on

## To UP the API Server

- export the root directory path of this project to the PYTHONPATH.
- install the required libraries mentioned in the requirements.txt file
- start the Server by changing the directory to basic or intermediate or advanced and execute the below command

```
uvicorn main_file_name:todo_app_name
```

#### To start the basic API Server

```
uvicorn main:todo
```

#### To start the intermediate API Server

```
uvicorn intermediate_api:todo
```

#### To start the advanced API Server

```
uvicorn main:todo
```

Now the API Servers will be up and running.

## To use the swagger docs

```
http://localhost:8000/docs
```

## Advanced API Server oprations

- create user
- login with that user and get the JWT token
- create todo
- list todo
- get todo with id
- get todos with the priority
- get todos with the tag
- get todos with the filer(mention both the tag and priority)
- update todo
- patch todo
- delete todo

## Features

- Authentication
- JWT Token
- FastAPI Routing
- Custom HTTP Exceptions
- Worked with Path variables, Query Parameters, Body, Headers, Form input
- FastAPI exception handler
- BaseModel for the API inputs

## Swagger snaps

#### Todo operations

![Image](https://github.com/LogeshVel/ToDoler-FastAPI/blob/main/advanced/swagger_snaps/todos.png)

#### User and Auth operations

![Image](https://github.com/LogeshVel/ToDoler-FastAPI/blob/main/advanced/swagger_snaps/user_auth.png)

See the swagger documentation for more after running the server.

