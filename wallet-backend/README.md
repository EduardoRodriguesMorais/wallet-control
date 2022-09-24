
## Requirements

 - Python 3 
 - Pip
 - [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)


## How to work

### Clone this repository
```bash
$ git clone https://github.com/EduardoRodriguesMorais/wallet-control.git
```


### Access project directory in terminal
```bash
$ cd wallet-backend
```

### Install all dependencies
```bash
$ pipenv install --dev
```

### Enable environment
```bash
$ pipenv shell
```

### Rename dotenv file
```bash
$ mv dotenv_example .env
```

### Define a db connection string in .env file
```bash
DB_URL=sqlite://boilerplate.db
```

### Run create migrations
```bash
$ make create_migrations
```

### Run migrates
```bash
$ make migrate
```

### Running application in develop mode
```bash
$ python run.py 
```
or
    
```bash
$ make run-app-local
```


### The application is running in port:8000 - 
### acess documentation:  <http://localhost:8000/docs>
### acess Heath Check:  <http://localhost:8000/health-check> 
## Running tests

For run tests, use this commands:

```bash
pytest 
```
or
```bash
make testing 
```

## For create new module, use this commands:
```bash
make create_module 
```

## Reference

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [testdriven.io](https://testdriven.io/courses/tdd-fastapi/)
 - [pytest](https://docs.pytest.org/en/6.2.x/contents.html)
 - [Flake8](https://flake8.pycqa.org/en/latest/)
 - [Clean Arch](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
 
## Author

- [Eduardo Morais](eduardoromorais@gmail.com)




