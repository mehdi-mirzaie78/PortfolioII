[![iPortfolio](https://github.com/mehdi-mirzaie78/PortfolioII/actions/workflows/main.yml/badge.svg)](https://github.com/mehdi-mirzaie78/PortfolioII/actions/workflows/main.yml)

# iPortfolio

## Technologies
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) 
## Main Source
[iPortfolio](https://bootstrapmade.com/demo/iPortfolio/)

## Demo
https://github.com/mehdi-mirzaie78/iPortfolio/assets/107181484/a4321dad-0611-4e83-a1f9-ba8722d005c5


## How to run?
### Prerequisites
Create a `.env` file inside `src/config` and paste this content and modify it based on your project:
```env
SECRET_KEY=<YOUR_SECRET_KEY>
DEBUG=False
ALLOWED_HOSTS=*
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=<YOUR_DATABASE_NAME>
POSTGRES_USER=<YOUR_DATABASE_USER>
POSTGRES_PASSWORD=<YOUR_DATABASE_PASSWORD>
POSTGRES_HOST=db
POSTGRES_PORT=5432
CORS_ALLOWED_ORIGINS=http://localhost http://0.0.0.0
CSRF_TRUSTED_ORIGINS=<https://*.your_domain.com> http://0.0.0.0
SUPERUSER_USERNAME=<YOUR_SUPERUSER_USERNAME>
SUPERUSER_PASSWORD=<YOUR_SUPERUSER_PASSWORD>
SUPERUSER_EMAIL=<YOUR_SUPERUSER_EMAIL>
```
### 1. Using Docker
1. Install `docker` and `docker compose`
2. In directory that `docker-compose.yml` exists run:
```shell
docker-compose up --build -d
```
3. For stopping server run: 
```shell
docker-compose down
```
### 2. Using Makefile
1. Clone the project.
2. Create `.env` file in `src/config` path.
3. Modifiy `.env` file based on your database information.
4. Create a virtual environment `python -m venv venv`.
5. Activate the environment `source venv/bin/activate`
6. In the root directory of project `cd` to `src` and run:
```shell
make all
```
7. Create a superuser with specified `SUPERUSER_USERNAME` & `SUPERUSER_PASSWORD` info in `.env` file:
```shell
make createsuperuser
```
8. Run server:
```shell
make run
```
## Enter information:
1. Open up your browser in `localhost:80/admin`. 
2. Use your credentials to login and add all of your information.
