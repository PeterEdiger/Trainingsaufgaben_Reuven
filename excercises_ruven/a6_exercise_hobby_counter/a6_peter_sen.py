import statistics as stat

def average_age_under(people, under=1000):
    try:
        ages = [human["age"] for human in people]
        filtered_ages = filter(lambda a: a < under, ages)
        average_age = stat.mean(filtered_ages)
        return average_age
    except: return 0.0

