# django Project Instruction

## Project Stack

| Name     | Version  | Name II    | Version |
|----------|----------|------------|---------|
| Python   | 3.11.1   | Nginx      |         |
| Django   | 4.1.6    | Redis      |         |
| Ubuntu   | 20.10.14 | RabbitMQ   |         |
| Docker   | 20.04    | Prometheus |         |
| Git      | 2.33     | ELK        |         |
| Postgres | 14.3     |            |         |

## Development Enviroment Configuration

## Clone Project

The first things to do is to clone the repository.

### Python env Setup

Create a virtual environment to install dependencies inside it and activate it.

### Virtualenv package

Install Virtualenv package

```sh
pip install virtualenv --upgrade
```

Create virtual enviroment command is:
```sh
virtualenv .venv
```

Active Vitual Enviroment in windows

```sh
.\.venv\Scripts\activate.bat
```

To install dependecies you can use below command:
```sh
pip install django
```

To save all dependency always after installation use below command:

```sh
pip freeze > requirements.txt
```

To install all current dependencies on your enviroment:

```sh
pip install -r requirements.txt
```



