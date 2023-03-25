import statistics as stat
from collections import Counter


def average_age_under(people, under=1000):
    ages = [human["age"] for human in people]
    filtered_ages = list(filter(lambda a: a < under, ages))
    try:
        average_age = stat.mean(filtered_ages)
    except stat.StatisticsError:
        return 0.0
    return average_age

def hobby_counter(people: list) -> Counter:
    """
    Counts how many times a hobby is present.
    """
    counter=Counter()
    for human in people:
       counter.update(human["hobbies"])
    return counter

def n_most_common(people: list, n: int) -> list:
    return [i[0] for i in sorted(hobby_counter(people).items(),key=lambda x:x[1],reverse=True)[:n]]

