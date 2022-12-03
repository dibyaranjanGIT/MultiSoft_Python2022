'''
HTTP Methods
REST APIs listen for HTTP methods like GET, POST, and DELETE to know which operations to perform on the web service’s
resources. A resource is any data available in the web service that can be accessed and manipulated with HTTP requests
to the REST API. The HTTP method tells the API which action to perform on the resource.

While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:

HTTP method	Description
GET	Retrieve an existing resource.
POST	Create a new resource.
PUT	Update an existing resource.
PATCH	Partially update an existing resource.
DELETE	Delete a resource.
'''


## Status Codes
# Once a REST API receives and processes an HTTP request,
# it will return an HTTP response. Included in this response is an HTTP status code

'''
Code	Meaning	Description
200	OK	The requested action was successful.
201	Created	A new resource was created.
202	Accepted	The request was received, but no modification has been made yet.
204	No Content	The request was successful, but the response has no content.
400	Bad Request	The request was malformed.
401	Unauthorized	The client is not authorized to perform the requested action.
404	Not Found	The requested resource was not found.
415	Unsupported Media Type	The request data format is not supported by the server.
422	Unprocessable Entity	The request data was properly formatted but contained invalid or missing data.
500	Internal Server Error	The server threw an error when processing the request.


Code range	Category
2xx	Successful operation
3xx	Redirection
4xx	Client error
5xx	Server error
'''

## GET ##
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# response.json()

## POST ##
'''POST create a new resource '''
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# response = requests.post(api_url, json=todo)
# response.json()

## PUT ##
'''PUT request is to update an existing request'''

# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.get(api_url)
# response.json()
# #{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}
#
# todo = {"userId": 1, "title": "Wash car", "completed": True}
# response = requests.put(api_url, json=todo)
# response.json()

## PATCH ##
'''PATCH is to modify the value of a specific field on an existing resource'''
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# todo = {"title": "Mow lawn"}
# response = requests.patch(api_url, json=todo)
# response.json()

## DELETE ##
''' if you want to completely remove a resource '''
# import requests
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# response = requests.delete(api_url)
# response.json()