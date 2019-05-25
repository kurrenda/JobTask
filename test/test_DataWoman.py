from functions import DataWoman

def test_average():
    d = DataWoman.CountWoman('dane.csv')
    temp = 2010
    total = d.average(temp,'Mazowieckie')
    assert total >= 0


def test_percent():
    d = DataWoman.CountWoman('dane.csv')
    temp = 2010
    total = d.percent(temp,'Mazowieckie')
    assert total >= 0 and total <= 101

def test_bestPass():
    d = DataWoman.CountWoman('dane.csv')
    total = d.bestPass(2012)
    assert total >= 0
