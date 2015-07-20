from nose import *
import castlecrawler


def test_index():
    # check that we get a 404 on the / url
    resp = app.request('/')
    assert_response(resp, status="404")


def test_hello():
    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # test that defaults return correct response
    resp = app.request("/hello", method = "POST")
    assert_response(resp, contains = "nobody")

    # test that we get expected values
    data = {'name':'Shirley', 'greet':'vale'}
    resp = app.request("/hello", method = "POST", data = data)
    assert_response(resp, contains = "Shirley")