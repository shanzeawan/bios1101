import pandas as pd

filnavn = "abalone_measurements.csv"
data = pd.read_csv(filnavn, skiprows = 7)
print(data.head())