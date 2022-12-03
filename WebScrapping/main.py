import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://dibyaranjangit.github.io/personal/"

# Get the html content
r = requests.get(url)
html_content = r.content

### Differences between parsers
'''
Beautiful Soup presents the same interface to a number of different parsers, but each parser is different. 
Different parsers will create different parse trees from the same document. The biggest differences are between the 
HTML parsers and the XML parsers. Here’s a short document, parsed as HTML using the parser that comes with Python
'''

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())

# HTML Tree traversal
title = soup.title
print(title)


# # One common task is extracting all the URLs found within a page’s <a> tags:
# for link in soup.find_all('a'):
#     print(link.get('href'))


# # Another common task is extracting all the text from a page:
# print(soup.get_text())

# # A Tag object corresponds to an XML or HTML tag in the original document:
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
# print(type(tag))

# A tag has two important features one is name and other is attributes

# Name
print(tag.name)

# Attribute
'''
A tag may have any number of attributes. The tag <b id="boldest"> has an attribute “id” whose value is “boldest”. 
You can access a tag’s attributes by treating the tag like a dictionary
'''
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])


## Multi valued Attributes
'''
The most common multi-valued attribute is class (that is, a tag can have more than one CSS class).
'''
css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
print(css_soup.p['class'])

### Navigating using tag names¶
# print(soup.head)
# <head><title>The Dormouse's story</title></head>

# print(soup.title)
# <title>The Dormouse's story</title>

# print(soup.body.b)
## <b>The Dormouse's story</b>

# print(soup.a)
##<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


### NavigableString
'''
A string corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to contain these 
bits of text:
'''
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
# tag = soup.b
# print(tag.string)

### get_text()
'''
If you only want the human-readable text inside a document or tag, you can use the get_text() method. 
It returns all the text in a document or beneath a tag, as a single Unicode string:
'''
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup, 'html.parser')
print(soup.get_text())