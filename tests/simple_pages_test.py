"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/page1">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'GIT' in response.data
    assert b'Docker' in response.data
    assert b'Python/Flask' in response.data
    assert b'CI/CD' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to my Website!" in response.data


def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"What is Git" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"What is Docker?" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"What is Pytest" in response.data


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Continuous Integration" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 404
