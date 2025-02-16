import requests

CREATE_AD_URL = "https://qa-internship.avito.com/api/1/item"

def test_create_ad():
    data = {
    "sellerID": 1,  
    "name": "Иван", 
    "price": 1000  
}
    response = requests.post(CREATE_AD_URL, json=data)
    assert response.status_code == 200
    

