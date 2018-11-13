from bs4 import BeautifulSoup

# html_doc = '/home/django/data/bs4/examplepage.html'

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
 </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# Some of the navigational methods
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.title.parent.name)

#finds the first 'p' tag
print(soup.p)
print(soup.find('p'))

#returns the class attribute of the first 'p' tag
print(soup.p['class'])
#Returns the list of all the 'p' tags
print(soup.find_all('p'))

#finds and returns t

print(soup.a['id'])