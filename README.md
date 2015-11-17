# banking-api

## about

- search all German banks for: BIC, BLZ, zipcode and City
- [TODO] calculate IBAN out of BLZ and account number


## datasource

http://www.bundesbank.de/Redaktion/DE/Standardartikel/Aufgaben/Unbarer_Zahlungsverkehr/bankleitzahlen_download.html


## Example API usage:

```
/v1/bank?blz=10000000
/v1/bank?bic=MARKDEF1100
/v1/bank?city=Berlin
/v1/bank?zipcode=10117
```
