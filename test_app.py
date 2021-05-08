from app import app


def test_index():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert len(response.data) >= 0


def test_get_count():
    import app
    count = app.update_count()
    assert count >= 0


def test_update_count():
    import app
    old_count = app.get_count()
    new_count = app.update_count()
    assert old_count < new_count
