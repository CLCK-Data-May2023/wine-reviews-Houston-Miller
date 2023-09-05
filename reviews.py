import pandas as pd
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

by_country = reviews.groupby('country').agg({'country': 'count', 'points': 'mean'}).round(1)
by_country_remane = by_country.rename(columns = {'country':'count'})
by_country_sorted = by_country_remane.sort_values('count', ascending = False)

df = pd.DataFrame(by_country_sorted)
df.to_csv('data/reviews-per-country.csv')