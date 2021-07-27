# Pytest
import pytest

#PyMongo
from pymongo import ASCENDING, DESCENDING

# App
from app.models.company import Company
"""PyMongo"""


@pytest.mark.usefixtures('db')
def test_get_company_with_pymongo(client,db):
    company = db.companies.find_one({
        "name":"Facebook"
    })
    assert company['name'] == 'Facebook'

@pytest.mark.usefixtures('db')
def test_sort_companies_with_pymongo(client,db):
    companies = list(db.companies.find().sort("name", ASCENDING).limit(10))
    assert len(companies) == 10
    assert companies[0]['name'] == '(fluff)Friends'

    companies = list(db.companies.find().sort("name", DESCENDING).limit(5))
    assert len(companies) == 5
    assert companies[0]['name'] == 'zyntroPICS'


"""MongoEngine"""


@pytest.mark.usefixtures('connection')
def test_get_company_with_mongoengine(client,connection):
    company = Company.objects(name='Facebook').first()
    assert company['name'] == 'Facebook'


@pytest.mark.usefixtures('connection')
def test_sort_companoes_with_mongoengine(client,connection):
    companies = list(Company.objects().order_by('+name').limit(10))
    assert len(companies) == 10
    assert companies[0]['name'] == '(fluff)Friends'

    companies = list(Company.objects().order_by('-name').limit(5))
    assert len(companies) == 5
    assert companies[0]['name'] == 'zyntroPICS'
