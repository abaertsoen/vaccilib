# coding: utf-8

# Imports


import requests
import datetime
from datetime import date, datetime


# Config


doctolib_lookup = [
    {
        "url": "https://www.doctolib.fr/centre-de-sante/paris/vaccinodrome-covid-19-porte-de-versailles?highlight%5Bspeciality_ids%5D%5B%5D=5494",
        "agenda_ids": '467153-467165-467177-467186-467189-467150-467151-467188-467190-467187-467152-467154-467162-467163-467164-467166-467174-467175-467176-467178',
        "practice_ids": "185273",
        "visit_motive_ids": "2823401"
    }
]
bot_name = "LaDose"
webhook_url = "https://discord.com/api/webhooks/XXXX/XXXXX"
console_prints = False


# Doctolib API


def check_availabilities(dc_item):
    headers = {
        'authority': 'www.doctolib.fr',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'content-type': 'application/json; charset=utf-8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.doctolib.fr/centre-de-sante/',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('start_date', date.today().strftime("%Y-%m-%d")),
        ('visit_motive_ids', dc_item['visit_motive_ids']),
        ('agenda_ids', dc_item['agenda_ids']),
        ('insurance_sector', 'public'),
        ('practice_ids', dc_item['practice_ids']),
        ('destroy_temporary', 'true'),
        ('limit', '4'),
    )

    response = requests.get('https://www.doctolib.fr/availabilities.json', headers=headers, params=params)

    slots = response.json()
    return slots


# Discord alert


def send_alert(content, e_title, e_desc, e_url):
    data = {
        "content" : content,
        "username" : bot_name
    }

    data["embeds"] = [
        {
            "description" : e_desc,
            "title" : e_title,
            "url" : e_url
        }
    ]

    result = requests.post(webhook_url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if console_prints:
            print(err)
    else:
        if console_prints:
            print("Payload delivered successfully, code {}.".format(result.status_code))


# Main run


for dc_item in doctolib_lookup:
    slots = check_availabilities(dc_item)

    if slots['total'] > 0:
        if console_prints:
            print("Slots available")
        for dates in slots['availabilities']:
            if len(dates['slots']) > 0:
                slot_times = [str(datetime.strptime(stime['start_date'].split('+')[0], '%Y-%m-%dT%H:%M:%S.%f').time()) for stime in dates['slots']]
                send_alert(content='Dose de vaccin disponible', e_title=str(dates['date']), e_desc="\n".join(slot_times), e_url=dc_item.url)
    else:
        if console_prints:
            print("No slots")
