all_people = [{'name': 'Reuven', 'age': 50, 'hobbies': ['Python', 'cooking', 'reading']},
              {'name': 'Atara', 'age': 20, 'hobbies': ['horses', 'cooking', 'art', 'reading']},
              {'name': 'Shikma', 'age': 18, 'hobbies': ['Python', 'piano', 'cooking', 'reading']},
              {'name': 'Amotz', 'age': 15, 'hobbies': ['boxing', 'cooking']}]


def average_age_under(people, under=1000):
    sum_humans = 0
    sum_age = 0
    for human in people:
        if human["age"] < under:
            sum_age += human["age"]
            sum_humans += 1
    avg_age = sum_age / sum_humans if sum_humans > 0 else 0
    return avg_age



