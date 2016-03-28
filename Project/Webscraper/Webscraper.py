from lxml import html
import requests

#Next we will use requests.get to retrieve the web page with our data,
#  parse it using the html module and save the results in tree:

buyers = []
prices = []
for i in xrange(1,6):
    page = requests.get('http://econpy.pythonanywhere.com/ex/00%d.html' % (i))
    tree = html.fromstring(page.content)
    #This will create a list of buyers:
    buyers.append(tree.xpath('//div[@title="buyer-name"]/text()'))
    #This will create a list of prices
    prices.append(tree.xpath('//span[@class="item-price"]/text()'))

#Lets see what we got exactly:
buyerlist = []
pricelist = []
for row in buyers:
    for item in row:
        buyerlist.append(item)

for row in prices:
    for item in row:
        pricelist.append(item)

# print 'Buyers: ', buyers
# print 'Prices: ', prices
for i in xrange(0, len(buyerlist) - 1):
    print '{0: >25}'.format(buyerlist[i]), " ", pricelist[i]


