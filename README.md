# GeoJSON API

[![<jvitors23>](https://circleci.com/gh/jvitors23/geojsonapi.svg?style=shield)](https://circleci.com/gh/jvitors23/geojsonapi)


Simple rest API that allows the user to CRUD providers and service areas. This project was deployed to AWS using ECS - Elastic Container Service ([link to deployed app](https://geojson.18.204.47.205.sslip.io/api/swagger/)).


### Technologies

* Python
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Pytest](https://docs.pytest.org/en/7.2.x/)
* [AWS ECS](https://aws.amazon.com/pt/ecs/)
* [AWS ECR](https://aws.amazon.com/pt/ecr/)
* [Docker](https://www.docker.com/)
* [CircleCI](https://circleci.com/)
* [PostGIS](https://postgis.net/)
* [Caddy](https://caddyserver.com/)
* [gunicorn](https://gunicorn.org/)


### About the project

The django project has three apps:

* users: Deals with the user sign up and api token request;
  * POST ```/api/v1/users/signup/```: Sign up of new users;
  * POST ```/api/v1/users/token/```: Endpoint for requesting auth tokens;
  * PUT/PATCH/GET: ```/api/v1/users/me/```: Manage logged user data;
* providers: CRUD of providers. Each provider has an owner user, only this user can edit/delete the provider.
  * POST ```/api/v1/providers/```: Create a new provider;
  * GET ```/api/v1/providers/```: List providers;
  * GET ```/api/v1/providers/{id}```: Retrieve provider;
  * PUT/PATCH ```/api/v1/providers/{id}```: Update provider;
* serviceareas: CRUD of service areas.
  * GET ```/api/v1/serviceareas/?lat=x&lng=y```: Query service areas that contains specific latitude and longitude;
  * POST ```/api/v1/serviceareas/```: Create a new service area;
    * Example payload:
    ```
    {
	    "name": "service area name",
	    "price": 10.50,
	    "provider": 1,
	    "polygon": [
        {"lat": 1, "lng": 1},
        {"lat": 1, "lng": -1},
        {"lat": -1, "lng": -1},
        {"lat": -1, "lng": 1},
        {"lat": 1, "lng": 1}
	    ]
    }
    ```
  * GET ```/api/v1/serviceareas/```: List service areas;
  * GET ```/api/v1/serviceareas/{id}```: Retrieve service area;
  * PUT/PATCH ```/api/v1/serviceareas/{id}```: Update service area.

### About PostGIS

The application database [PostGIS](https://postgis.net/) is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

### Deploy

This application was deployed using AWS ECS ([link to deployed app](https://geojson.18.204.47.205.sslip.io/api/swagger/)). The project docker images were built and pushed to ECR. The ECS task has three containers:
* Django app:  Runs gunicorn server;
* Caddy: Serves the static files, reverse proxy the django application and provides automatic https;
* PostGIS: Application database.

### API docs (swagger)

Available swagger documentation at [https://geojson.18.204.47.205.sslip.io/api/swagger/](https://geojson.18.204.47.205.sslip.io/api/swagger/)

### Running the project

Requirements: Docker and docker-compose.

Most of the project settings comes from environment variables. You need to create a ```.env``` file similar to the ```.env-example``` at the repository root.
Then you can start the local development server using the docker-compose command:

```bash
 docker-compose up --build
```

### Running tests

The tests were written using the pytest framework. They can be run using the following command:

```
docker-compose run app bash -c "pytest geojsonapi/apps --cov . -n 8"
```


![tests](https://i.imgur.com/IpBpZNN.png)
