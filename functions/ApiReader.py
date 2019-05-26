#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

def api():
    url = "https://api.dane.gov.pl/resources/17363"

    response = requests.get(url)

    data = response.text
    parsed = json.loads(data)

    url2 = parsed["data"]["attributes"]["link"]
    response2 = requests.get(url2)
    with open('daneApi.csv', 'wb') as f:
        f.write(response2.content)
