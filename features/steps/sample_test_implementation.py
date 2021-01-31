import requests
from behave import *

api_endpoints = {}
request_headers = {}
response_codes = {}
response_texts = {}
request_bodies = {}
api_url = None


@given(u'the REST API url is set')
def step_impl(context):
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'


# Post scenario

@given(u'POST post api endpoint is set')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url + '/posts'
    print('url :' + api_endpoints['POST_URL'])


@when(u'The HEADER param request content type is set as "{header_content_type}"')
def step_impl(context, header_content_type):
    request_headers['Content-Type'] = header_content_type


@when(u'body request is set')
def step_impl(context):
    request_bodies['POST'] = {"title": "turtle", "body": "fish", "userId": "1"}


@when(u'POST HTTP request is sent')
def step_impl(context):
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    response_texts['POST'] = response.text
    print("POST RESPONSE:" + response.text)
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then(u'a valid HTTP response with code 201 for "POST" is recieved')
def step_impl(context):
    print('Post rep code: '+str(response_codes['POST']))
    assert response_codes['POST'] == 201

#END POST
