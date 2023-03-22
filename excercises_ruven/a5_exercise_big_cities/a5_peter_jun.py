import json
import csv
import requests

gist_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"


def cities_to_csv(url: str, csv_filename: str):
    """
    Takes an url and a filename.
    Writes a csv with wanted cities.
    """
    city_data = requests.get(url)
    des_city_data = json.loads(city_data.text)
    mapped_lst_of_dicts = map(lambda d: {"city": d["city"],
                                         "state": d["state"],
                                         "rank": d["rank"],
                                         "population": d["population"]}, des_city_data)

    with open(csv_filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter="\t")
        for _dict in mapped_lst_of_dicts:
            writer.writerow(_dict.values())




if __name__ == '__main__':
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
