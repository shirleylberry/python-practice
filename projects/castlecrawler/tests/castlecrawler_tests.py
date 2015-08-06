from nose.tools import *
from bin.app import app
from tests.tools import assert_response
import castlecrawler

def test_index():
    # check that we get a 200 on the / url
    resp = app.request('/')
    assert_response(resp, status="200")


def test_hello():
    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # test that defaults return correct response
    resp = app.request("/hello", method = "POST")
    print resp
    assert_response(resp, contains = "nobody")

    # test that we get expected values
    data = {'name':'Shirley', 'greet':'vale'}
    resp = app.request("/hello", method = "POST", data = data)
    print resp
    assert_response(resp, contains = "Shirley")
