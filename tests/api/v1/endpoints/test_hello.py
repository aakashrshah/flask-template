from app.config import API_V1_STR


def test_root_endpoint(client):
    response = client.get(f'{API_V1_STR}/')
    assert response.status_code == 200
    

def test_root_endpoint_fails(client):
    response = client.get(f'{API_V1_STR}/hello')
    assert response.status_code == 404


def test_items_endpoint(client):
    response = client.get(f'{API_V1_STR}/items/1')
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'item_id': 1, 'q': None}
