"""
Pull data from Zillow for multiple data dimensions.
Pulled from zillowstatic.com
Data includes:
  - 

Parameters:
  - 
"""

import requests as r
import os

BASEURL = "http://files.zillowstatic.com/research/public"
city_url = os.path.join(BASEURL, "City")
neigh_url = os.path.join(BASEURL, "Neighborhood/Neightborhood_")

# Build url lists to pull from
rental_opts = ["duplextriplex.csv", "studio.csv", "1bedroom.csv"]
rental_urls = ["_".join([neigh_url, "medianrentalpricepersqft", x]) for x in rental_opts]

def run():
    
