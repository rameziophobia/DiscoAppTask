
def test_search_wrong_query_param(client):
    response = client.get("/search?name=the godfather")
    assert response.status_code == 400


def test_search_by_title(client):
    response = client.get("/search?title=the godfather")
    assert len(response.get_json()) == 3
    assert response.status_code == 200


def test_search_by_title_exact(client):
    response = client.get("/search?title_exact=the godfather")
    assert len(response.get_json()) == 1
    assert response.get_json()[0]['id'] == '238'
    assert response.status_code == 200


def test_search_by_vote_average_at_least_x(client):
    response = client.get("/search?title_exact=the godfather")
    assert len(response.get_json()) == 1
    assert response.get_json()[0]['id'] == '238'
    assert response.status_code == 200


def test_search_by_vote_average_at_least_x(client):
    TEST_NUM = 8.5
    response = client.get(f"/search?vote_average_at_least={TEST_NUM}")
    assert len(response.get_json()) == 31
    assert all([float(row['vote_average']) >=
               TEST_NUM for row in response.get_json()])
    assert response.status_code == 200
