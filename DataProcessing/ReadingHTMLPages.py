# import urllib2
from bs4 import BeautifulSoup
from urllib.request import urlopen

'''Reading the HTML file'''
# Fetch the html file
response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

# Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# Format the parsed html file
strhtm = soup.prettify()

# Print the first few characters
print (strhtm[:225])
print('-----' * 20)
print('*****' * 20)

'''Extracting Tag Value'''
response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

print('-----' * 20)
print('*****' * 20)

'''Extracting All Tags'''
response = urlopen('http://tutorialspoint.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all('b'): print(x.string)

print('-----' * 20)
print('*****' * 20)
