try:
    import requests
    import bs4
    import re
except ImportError as e:
    print('MODULES ARE MISSING! ' + e)

website = input('What is your magicseaweed surf spot url: ')

res = requests.get(website)
soup = bs4.BeautifulSoup(res.text, 'lxml')
title = soup.select('title')
current_conditons = soup.select('span.visible-xs.heavy')
size_ft = soup.select('li.rating-text.text-dark')
rating = soup.select('ul.rating.rating-large.clearfix')
ratingcount = 0
wind = soup.select('p.h5.nomargin-top')
swell = soup.select('div.inline-block')
tide = soup.select('table.table.table-sm.table-striped.table-inverse.table-tide')

for word in str(rating).split():
    if word == 'class="active">':
        ratingcount += 1

try:
    print(f'''

{title[0].getText()}
{current_conditons[0].getText()}:


Size:{size_ft[0].getText()}

Rating:  {ratingcount}/5

Wind:   {wind[0].getText()}


Swell:
    Primary Swell: {swell[0].getText()}
    Seconday Swell: {swell[1].getText()}
    Wind Swell: {swell[2].getText()}


Tide:
{tide[0].getText()}


Times:
{tide[1].getText()}

''')
except:
    print("not enough info about surf spot!")