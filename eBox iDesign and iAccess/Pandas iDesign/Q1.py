# Write a Python program to create a Pandas Data Frame from a List of Lists and print the Data Frame.
# List of Lists is specified as part of the template code.

import pandas as pd

data = [[5.1,3.5,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisVersicolor"],
	[6.4,3.2,4.5,1.5,"IrisVersicolor"],
	[6.3,3.3,6.0,2.5,"IrisVirginica"],
	[5.8,2.7,5.1,1.9,"IrisVirginica"]]

#Fill in the code here
df = pd.DataFrame(data, columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species_type'])

print(df)