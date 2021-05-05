# vaccilib
Get a notification on Discord for any Vaccine appointment available near you

## Configure the doctolib_lookup field :
Actually the script need a little bit of help to know where to look on doctolib;
In order to provide the needed information, follow these steps :
- Open a vaccination center's Doctolib page on your browser (ex : https://www.doctolib.fr/centre-de-sante/paris/centre-medical-institut-pasteur-cmip-vaccination-covid-19?highlight%5Bspeciality_ids%5D%5B%5D=5494)
- Open the developer's tools (F12) and go to the "Network" tab
- Flush all data in that tab thanks to the clear button on the top left corner of that tab
- On the page, select the reason for which you want to be alerted for any spot available (for us : Patients de moins de 50 ans éligibles)
- In the "Network tab", a single line should now have appeared, starting with availabilities.json, double click on it
- All the requested data are found in the url you just opened in your browser.

Feel free to add more than a single center in the script as it will run through the whole doctolib_lookup array
