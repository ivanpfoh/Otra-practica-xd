import pandas as pd 
# Let's create a dictionary
dataset = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
        'year': [2017, 2016, 2017, 2019, 2016],
        'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol']}

# Write your code here
audi_cars = pd.DataFrame(dataset)
# Adding a new column
audi_cars.insert(2, "price", [12500, 16500, 16800, 17300, 13900])
# Let`s print it
print(audi_cars)