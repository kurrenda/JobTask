#!/usr/bin/env python
# -*- coding: utf-8 -*-


from functions import DataMan

def test_average():
    d = DataMan.CountMan('dane.csv')
    temp = 2010
    total = d.average(temp,'Mazowieckie')
    assert total >= 0


def test_percent():
    d = DataMan.CountMan('dane.csv')
    temp = 2010
    total = d.percent(temp,'Mazowieckie')
    assert total >= 0 and total <= 101

def test_bestPass():
    d = DataMan.CountMan('dane.csv')
    total = d.bestPass(2012)
    assert total >= 0
