from collections import Counter, defaultdict

visits = defaultdict(Counter)


def collect_places():
    """This function takes user inputs and collects them in a list
        in following format [(country, [city]), ...]
    """
    visits.clear()
    while True:

        user_input = input("Tell me where you went: ")
        if user_input == "":
            break
        city_country = user_input.split(",")
        if len(city_country) == 2:
            city, country = [stripped.strip() for stripped in city_country]
            visits[country].update(list((city,)))
            continue
        print("That's not a legal city, country combination")


def display_places():
    sorted_countrys = sorted(visits)
    print(sorted_countrys)
    for country in sorted_countrys:
        print(country)
        sorted_cities = sorted(visits[country])
        for city in sorted_cities:
            count = visits[country][city]
            print(f"  {city} ({count})")


if __name__ == '__main__':
    collect_places()
    print(visits)
    display_places()
