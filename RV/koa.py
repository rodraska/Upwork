from bs4 import BeautifulSoup
import requests
import pandas as pd
import mechanize

br = mechanize.Browser()
br.set_handle_robots(True)

init_link = 'https://koa.com/states-provinces/'

states_koa = ['alabama', 'alaska', 'arizona', 'arskansas', 'california',
'colorado, connecticut', 'florida', 'georgia',
'idaho', 'illinois', 'indiana', 'iowa', 'kansas',
'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts',
'michigan', 'minnesota', 'mississipi', 'missouri', 'montana',
'nebraska', 'nevada', 'new-hamsphire', 'new-jersey', 'new-mexico',
'new-york', 'north-carolina', 'north-dakota', 'ohio', 'oklahoma',
'oregon', 'pennsylvania', 'south-carolina', 'south-dakota',
'tennessee', 'texas', 'utah', 'vermont', 'virgina',
'washington', 'west-virgina', 'wisconsin', 'wyoming',
'alberta', 'british-columbia', 'manitoba', 'new-brunswick', 'newfoundland-and-labrador',
'nova-scotia', 'ontario', 'prince-edward-island', 'quebec']

headers1 = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

PARAMS = {'query_string':'parameter'}
HEADERS = {'custom_auth_key': 'secret',
 'User-Agent': 'your_bot_name',
 'From' : 'your_email',
 'timeout' : '15'}

html_text = requests.get('https://koa.com/states-provinces/illinois/', headers=headers1).text
soup=BeautifulSoup(html_text, 'lxml')

with open('html_illinois', 'w') as f:
        f.write(soup.prettify())

""" for state in states_koa:
    html_text=requests.get(init_link+state).text
    soup=BeautifulSoup(html_text, 'lxml') """