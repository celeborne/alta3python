#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=nbaPz941PrncE6gF72Wm4aLr8hbF4Ab6qIYAYWml' ## replace this with our API key

    neourl = neourl + startdate + mykey
    print(neourl)
    neojson = requests.get(neourl).json()

    hazardous_objects = neojson.get("element_count")
    print(hazardous_objects)
    #for i in len(hazardous_objects): 
     #   if (hazardous_objects is True):
    print(str(hazardous_objects))
      #       i+=1
## call main
main()

