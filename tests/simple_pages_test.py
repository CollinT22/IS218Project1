"""This test the homepage"""




def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/Docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/Git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/Python-Flask")
    assert response.status_code == 200
    assert b"Python-Flask" in response.data



def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404