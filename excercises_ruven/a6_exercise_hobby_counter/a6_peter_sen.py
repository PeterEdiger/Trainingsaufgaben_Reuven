import statistics as stat

def average_age_under(people, under=1000):
    ages = [human["age"] for human in people]
    filtered_ages = filter(lambda a: a < under, ages)
    try:
        average_age = stat.mean(filtered_ages)
    except stat.StatisticsError:
        return 0.0
    return average_age

