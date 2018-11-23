# banking-api

## about

- search all German banks for: BIC, BLZ, zipcode and City
- calculate IBAN with BLZ, account number and country code


## datasource

http://www.bundesbank.de/Redaktion/DE/Standardartikel/Aufgaben/Unbarer_Zahlungsverkehr/bankleitzahlen_download.html


## Example API usage:

### blz/bic

banking.stupig.org is offline atm.

* https://banking.stupig.org/v1/bank?blz=10000000
* https://banking.stupig.org/v1/bank?bic=MARKDEF1100
* https://banking.stupig.org/v1/bank?city=Berlin
* https://banking.stupig.org/v1/bank?zipcode=10117

### iban

```
curl --request POST --url https://banking.stupig.org/v1/iban/ --header 'Content-Type: application/json' --data '{"country": "DE", "blz": "64090100", "account_number": "1234567"}'
```

returns

```
{"country":"DE","blz":"64090100","account_number":"1234567","iban":"DE80640901000001234567"}
```


## docker

```
# database
docker run -d --restart=always -v /home/banking/postgres:/var/lib/postgresql --name banking-db postgres:9.4

# home
docker run -d --name banking-data -v /home/uid1000 -v /home/banking/data:/home/uid1000/banking aexea/aexea-base

# python/nginx
docker build --tag=banking-prod .
docker rm -f banking
docker run -d --volumes-from banking-data --link banking-db:db -v `pwd`/banking/banking/settings/production.py:/opt/code/banking/banking/settings/production.py --restart=always --name banking banking-prod
docker rm -f banking-nginx
docker run --name banking-nginx --net="host" --volumes-from banking-data -p 80:80 -v `pwd`/nginx.conf:/etc/nginx/nginx.conf --restart=always -d nginx
```

initial database setup:

```
docker exec -ti banking python3 ./manage.py reset_db --settings=banking.settings.production
docker exec -ti banking python3 ./manage.py migrate --settings=banking.settings.production
docker exec -ti banking python3 ./manage.py createsuperuser --settings=banking.settings.production
docker exec -ti banking python3 ./manage.py bundesbank_import --settings=banking.settings.production
```
