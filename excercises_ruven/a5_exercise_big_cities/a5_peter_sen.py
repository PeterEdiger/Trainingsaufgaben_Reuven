import pandas as pd
my_url = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json"


def cities_to_csv(url: str, file_name: str) -> None:
    '''
    Function to get cities and write to csv
    '''

    df = pd.read_json(url)
    df = df[['city', 'state', 'rank', 'population']]
    df = df[['city']]
    print(df)
    df.to_csv(file_name, sep='\t', header=None, index=False)


cities_to_csv(my_url, "citi.csv")