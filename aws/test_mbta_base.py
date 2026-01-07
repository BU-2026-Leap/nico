# aws/test_mbta_base.py
from aws import mbta_base


def make_event(path: str, query: dict | None = None) -> dict:
    return {
        "rawPath": path,
        "queryStringParameters": query or {},
    }


def assert_is_html_response(resp: dict, expected_status: int = 200):
    """Loose assertion: checks routing/response shape, not page content."""
    assert isinstance(resp, dict)
    assert resp.get("statusCode") == expected_status

    headers = resp.get("headers")
    assert isinstance(headers, dict)
    assert headers.get("Content-Type") == "text/html"

    body = resp.get("body")
    assert isinstance(body, str)
    assert len(body) > 0


def test_home_page_renders():
    resp = mbta_base.lambda_handler(make_event("/"), None)
    assert_is_html_response(resp, 200)


def test_intro_page_renders():
    resp = mbta_base.lambda_handler(make_event("/intro"), None)
    assert_is_html_response(resp, 200)


def test_cockpit_page_renders():
    resp = mbta_base.lambda_handler(make_event("/cockpit"), None)
    assert_is_html_response(resp, 200)


def test_lunch_route_accepts_query_params_yes():
    resp = mbta_base.lambda_handler(make_event("/lunch", {"choice": "yes"}), None)
    assert_is_html_response(resp, 200)


def test_lunch_route_accepts_query_params_no():
    resp = mbta_base.lambda_handler(make_event("/lunch", {"choice": "no"}), None)
    assert_is_html_response(resp, 200)


def test_lunch_route_missing_query_dict_does_not_crash():
    # Simulate API Gateway sending no queryStringParameters
    resp = mbta_base.lambda_handler({"rawPath": "/lunch"}, None)
    assert_is_html_response(resp, 200)


def test_start_train_renders():
    resp = mbta_base.lambda_handler(make_event("/start_train"), None)
    assert_is_html_response(resp, 200)


def test_dynamic_stop_routes_render():
    for stop in ["B", "BC", "Kenmore", "Anything"]:
        resp = mbta_base.lambda_handler(make_event(f"/stop/{stop}"), None)
        assert_is_html_response(resp, 200)


def test_unknown_route_is_404():
    resp = mbta_base.lambda_handler(make_event("/does-not-exist"), None)
    assert_is_html_response(resp, 404)
