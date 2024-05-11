# product_api

API ordering the products

I built a quick app in less than 2 + 2 hours. There are comments where improvments are needed e.g. spliting the app into modules.

The most imporat logic is in create_order

## Getting Up and Running

1. Install the XCode command line tools for mac

2. Install docker and docker-compose

3. pipx install poetry # if you want to run project outside docker

## Installation

```
cp .env.template .env # fill out missing vars in .env
make up
make migrate
make loaddata
make superuser # optionally
```

## Usage

```
open http://localhost:8000/ # to see if docker built correctly

# here we get the token, see the stock, create the order and list the stock afterwards
curl -X POST -d "username=testme&password=ubwLut7Lv" http://localhost:8000/api-token-auth/
# replace token value with a real one
curl 'http://localhost:8000/products/' -H 'Authorization: Token 08a6a90f82e0c55f5ee20ff2d870604a15873967'

curl 'http://localhost:8000/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token 08a6a90f82e0c55f5ee20ff2d870604a15873967' \
  -d '{
  "product_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "quantity": 2
}'

# stock go down to 8
curl 'http://localhost:8000/products/' -H 'Authorization: Token 08a6a90f82e0c55f5ee20ff2d870604a15873967'
curl 'http://localhost:8000/orders/' -H 'Authorization: Token 08a6a90f82e0c55f5ee20ff2d870604a15873967'
```

## Testing

```
make test
```

## Deployment

```
# TODO add Procifle, gunicorn, runtime.txt
git push heroku main
```

## Documentation

```
open http://localhost:8000/schema/redoc/
```


## TODO
- prod, dev, test env split
- more validation for input
- refactor code (seprate apps for product and orders, move classes to separate files, better naming user -> buyer etc.)
- a lot of other things to consider like rate-limiting


