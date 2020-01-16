## Getting Started
These instructions will make you to run some containers in your machine.

### Prerequisites
```
Docker
Docker-composer
Python 3.8.1
```

### Installing

Clone this repository 

```
git clone https://github.com/gustavo8555/flask_test2.git
cd flask_test2
```

Building the containers

```
docker-compose build
```

Runnign the flask server

```
docker-compose up -d
```

Now access the address:
http://localhost/users

## Running the tests

Now you must create a virtual env for the unit_tests

```
python -m venv env;
source env/bin/activate
```

```
pip install -r services/requirements.txt
```

Finally

```
pytest
```


## Built With

* MongoDb
* Gunicorn
* Flask
* NGINX

