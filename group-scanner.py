# coding=UTF
'''Gets the posting data, price and post-id of a given post in a Facebook selling group containing certain keyword
    e.g. useful to find "bicycle" on your local flea-market group
    writes all the results on a prices.csv comma separated file
'''
import facebook
import requests
import csv
from parse import *

def get_price(post):
    price_out = 0
    strings = [u'\u20ac{:d}', u'{:d}\u20ac', u'{:d} \u20ac', u'\u20ac {:d}', u'{:d} euros',
               u'{:d} Euros']
    for lookfor in strings:
        price = search(lookfor, post)
        if price:
            price_out = price[0]
            break
    return price_out


def find_posts(group_id, access_token, keyword):
    lista = []
    
    graph = facebook.GraphAPI(access_token)
    
    posts = graph.get_connections(group_id, 'feed')
    while 'data' in posts.keys():
        for post in posts['data']:
            if 'message' in post and post['message'].find('fahrrad') != -1:
                lista.append({'id':post['id'],
                              'created_time':post['created_time'],
                              'price':get_price(post['message'])})
        posts = requests.get(posts['paging']['next']).json()
    print("No more posts")
    with open('./prices.csv', 'wb') as f:
        w = csv.DictWriter(f, lista[0].keys())
        w.writeheader()
        w.writerows(lista)
    print('Found ' + str(len(lista)) + ' items')

group_id = '207953839325465'  # get the desired groups group_id from facebook
access_token = '' # get your own Facebook access token in https://developers.facebook.com/tools/explorer
keyword = 'bicycle'

find_posts(group_id, access_token, keyword)