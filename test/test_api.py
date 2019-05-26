#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import ApiReader
from os.path import exists

def test_api():
    ApiReader.api()
    d = exists("daneApi.csv")
    assert d == True
