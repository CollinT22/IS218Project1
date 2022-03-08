"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/Docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/Git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/Python-Flask">Python-Flask</a>' in response.data
    assert b'<a class="nav-link" href="/CICD">CICD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

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

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/CICD")
    assert response.status_code == 200
    assert b"CICD" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404