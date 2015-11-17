# banking-api

## about

- search all German banks for: BIC, BLZ, zipcode and City
- calculate IBAN with BLZ, account number and country code


## datasource

http://www.bundesbank.de/Redaktion/DE/Standardartikel/Aufgaben/Unbarer_Zahlungsverkehr/bankleitzahlen_download.html


## Example API usage:

### blz/bic

```
http://localhost:8000/v1/bank?blz=10000000
http://localhost:8000/v1/bank?bic=MARKDEF1100
http://localhost:8000/v1/bank?city=Berlin
http://localhost:8000/v1/bank?zipcode=10117
```

### iban

```
curl --request POST --url http://localhost:8000/v1/iban/ --header 'Content-Type: application/json' -- data '{"country": "DE", "blz": "64090100", "account_number": "1234567"}'
```

returns

```
{"country":"DE","blz":"64090100","account_number":"1234567","iban":"DE80640901000001234567"}
```
