import requests

GET_ADS_BY_SELLERID_URL = "https://qa-internship.avito.com/api/1/"

def test_get_ads_by_sellerid():
    seller_id = 1
    response = requests.get(f"{GET_ADS_BY_SELLERID_URL}{sellerID}/item")
    assert response.status_code == 200
    