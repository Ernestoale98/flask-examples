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


@pytest.mark.usefixtures('db')
def test_query_operators_with_pymongo(client,db):
    companies = db.companies.count_documents({
        "number_of_employees":{
            "$gte":50
        }
    })
    assert companies == 904

    companies = db.companies.count_documents({
        "category_code":{"$not":{"$eq":"web"}}
    })
    assert companies == 7553

    companies = db.companies.count_documents({
        "acquisitions":{"$size":10}
    })
    assert companies == 4

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


@pytest.mark.usefixtures('connection')
def test_query_operators_with_mongoengine(client,connection):
    companies = Company.objects(number_of_employees__gte=50).count()
    assert companies == 904

    companies = Company.objects(category_code__not__exact='web').count()
    assert companies == 7553

    companies = Company.objects(acquisitions__size=10).count()
    assert companies == 4
