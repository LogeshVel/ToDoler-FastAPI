# ToDoler is an ToDO API built with FastAPI

This repo contains 3 main folders which is 3 different APIs
- Basic
- Intermediate
- Advanced

These 3 folders are kind of the level of FastAPI included in the APIs.

The basic API has some basic FastAPI features, ... and so on

## To UP the API Server

- export the root directory path of this project to the PYTHONPATH.
- install the required libraries
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

Now the API Servers will be and running.

## To use the swagger docs

```
url/docs
```

