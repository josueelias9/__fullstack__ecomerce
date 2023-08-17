
# source
## backend
- load initial data to database, https://docs.djangoproject.com/en/4.2/howto/initial-data/#provide-data-with-fixtures, Django official web page
- database configuration, https://docs.djangoproject.com/en/4.2/ref/settings/#databases, Django official web page
- conector, https://pypi.org/project/mysql-connector-python/, python official page

## mysql
- https://hub.docker.com/_/mysql


# deploy
load db image
```
cd ecomerce
docker compose up -d
```
initialize db
```
cd backend/project
python3 manage.py loaddata sample.json
```
run backend
```
python3 manage.py runserver
```
run frontend
```
npm run dev
```

# on progress...
- move project to repository
- create a simple fetch
- load items from backend