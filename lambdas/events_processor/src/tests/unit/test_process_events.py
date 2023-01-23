from src.app.handler import lambda_handler


def test_process_put_event(put_event):
    response = lambda_handler(put_event, None)
    assert response["statusCode"] == 200


def test_process_delete_event(delete_event):
    response = lambda_handler(delete_event, None)
    assert response["statusCode"] == 200


def test_process_transition_event(transition_event):
    response = lambda_handler(transition_event, None)
    assert response["statusCode"] == 200


def test_process_expiration_event(expiration_event):
    response = lambda_handler(expiration_event, None)
    assert response["statusCode"] == 200
