import json
import csv
import requests

gist_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"


def cities_to_csv(url, cities):
    city_data = requests.get(url)
    des_city_data = json.loads(city_data.text)
    new_lst1 = map(lambda d: {"city": d["city"],
                              "state": d["state"],
                              "population": d["population"],
                              "rank": d["rank"]}, des_city_data)
    cities = open("cities", 'w')
    writer = csv.writer(cities, delimiter="\t")
    writer.writerow(['city', 'state', 'population', 'rank'])
    for dictionary in new_lst1:
        writer.writerow(dictionary.values())
    cities.close()
    cities = open("cities", 'r')
    print(cities.read())

    # map filter reduce syntax in live templates.
    # print(des_city_data[:2])
    # print(new_lst[:3])
    # print(list(new_lst1)[:3])


cities_to_csv(gist_url, "cities.csv")

"""
City name
State name
City population
City size rank
"""

"""Wir haben ein riesiges list mit dicts. Wir brauchen nur einige key_value pairs aus einem dict. 
Diese pairs sollen dann in einem CSV Format dargestellt werden, wobei der delimiter ein Tab sein soll. 
"""
