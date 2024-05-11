# product_api

API ordering the products 

## Getting Up and Running

1. Install the XCode command line tools for mac

2. Install docker and docker-compose

3. pipx install poetry # if you want to run project outside docker

## Installation

```
cp .env.template .env # fill out missing vars in .env
make up

# for out of docker usage
poetry shell  # it will load variables from .env
poetry install
```

## Usage

```
open http://localhost:8000/
```

## Testing

```
py.test
```

## Deployment

```
# TODO
git push heroku main
```

## Documentation

```
open http://localhost:8000/schema/redoc/
```


## TODO
- prod and dev env split
- refactor code (seprate apps for product and orders)


