import requests
import create_ad_test

GET_AD_BY_ID__URL = "https://qa-internship.avito.com/api/1/item"

def test_get_ad():
    ad_id = "7b219754-757d-4934-accd-5c364ec6a797"
    response = requests.get(f"{GET_AD_BY_ID__URL}/{ad_id}")
    assert response.status_code == 200



GET_STATS_URL = "https://qa-internship.avito.com/api/1"

def test_get_ad_stats():
    ad_id = "7b219754-757d-4934-accd-5c364ec6a797"
    response = requests.get(f"{GET_STATS_URL}/statistic/{ad_id}")
    assert response.status_code == 200


GET_ADS_BY_SELLERID_URL = "https://qa-internship.avito.com/api/1/"

def test_get_ads_by_sellerid():
    seller_id = 1
    response = requests.get(f"{GET_ADS_BY_SELLERID_URL}{seller_id}/item")
    assert response.status_code == 200

