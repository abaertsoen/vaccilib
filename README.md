# vaccilib
Get a notification on Discord for any Vaccine appointment available near you

## Installation
Put the script wherever you want on your server and create a Python VirtualEnv to run it :
- Go into the deployment folder : 
``cd {my_deployment_folder}``
- Create the virtual env :
``python3 -m venv venv``
- Activate the virtual env :
``source ./venv/bin/activate``
- install the dependency :
``pip install requests``

## Configuration
To configure properly the script, you should edit the config section in Vaccilib.py (with a valid Discord Webhook and some Doctolib's information (see below) and the vaccilib.sh script to add the absolute path to your deployment folder.

### Configure the doctolib_lookup field :
Actually the script need a little bit of help to know where to look on doctolib;
In order to provide the needed information, follow these steps :
- Open a vaccination center's Doctolib page on your browser (ex : https://www.doctolib.fr/centre-de-sante/paris/centre-medical-institut-pasteur-cmip-vaccination-covid-19?highlight%5Bspeciality_ids%5D%5B%5D=5494)
- Open the developer's tools (F12) and go to the "Network" tab
- Flush all data in that tab thanks to the clear button on the top left corner of that tab
- On the page, select the reason for which you want to be alerted for any spot available (for us : Patients de moins de 50 ans éligibles)
- In the "Network tab", a single line should now have appeared, starting with availabilities.json, double click on it
- All the requested data are found in the url you just opened in your browser.

Feel free to add more than a single center in the script as it will run through the whole doctolib_lookup array

## Run the script
sh ./vaccilib.sh

## Automate the script
When everything is in place, you may want to automate this script;

I personnaly just added it to crontab with the following steps :
- Change the chmod of the bash script :
``chmod +rx vaccilib.sh``
- Open the crontab :
``crontab -e``
- and add the following line at the end of the file :
``*/5 * * * * /apps/Vaccilib/vaccilib.sh``

Save it and you're done. with that configuration, the script will run every 5 minutes.
