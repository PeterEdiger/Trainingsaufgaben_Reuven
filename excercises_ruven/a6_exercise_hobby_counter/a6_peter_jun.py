from collections import Counter
from functools import reduce


def average_age_under(people, under=1000):
    """
    Sums up ages of people and calculates the average.
    """
    sum_humans = 0
    sum_age = 0
    for human in people:
        if human["age"] < under:
            sum_age += human["age"]
            sum_humans += 1
    avg_age = sum_age / sum_humans if sum_humans > 0 else 0
    return avg_age


def all_hobbies(people: list) -> set:
    """
    Looks for unique hobbies of all people.
    """

    def union_hobbies(s1, s2):
        return s1.union(s2)
    if not people:
        return set()
    list_of_hobbies_sets = [set(human["hobbies"]) for human in people]
    return reduce(union_hobbies, list_of_hobbies_sets)


def hobby_counter(people: list) -> Counter:
    """
    Counts how many times a hobby is present.
    """
    hobby_list = []
    for human in people:
        for hobbies in human["hobbies"]:
            hobby_list.append(hobbies)
    hobby_count = Counter(hobby_list)
    return hobby_count


def n_most_common(people: list, n: int) -> list:
    """
    Counts which hobbies are most common
    """
    hobby_count = hobby_counter(people)
    hobby_list = []
    sorted_hobbies = sorted(hobby_count.items(), key=lambda x: x[1])
    for hobby_tuple in sorted_hobbies[-n:]:
        hobby_list.append(hobby_tuple[0])
    return hobby_list
