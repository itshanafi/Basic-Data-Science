# Create a class named City with the following private_attributes
# __name
# __state (of type State)
# Include a constructor
# __init__(self, name, state)
# Include a method
# __str__(self)
# This method returns a string corresponding to City details in the format specified
# in the sample output.
# Create a class named State with the following private_attributes
# __name
# __city_list (of type City)
# Include a constructor
# __init__(self, name, city_list)
# Include a method
# __str__(self)
# This method returns a string corresponding to State details in the format specified in the sample output.
# Include @property decorator for name
# Include @property decorator for city_list
# Include @setter decorator for city_list
# Create objects of the above classes and test them.
# Note :
# Perform case-sensitive string comparison.
# Initially state_list have the below states.
# Tamilnadu
# Andhra
# Karnataka
# Kerala
# If any new state is added other than the state in the list, it must be added to the state_list. [Refer sample input and output]
# Input and Output Format:
# Refer Sample Input and Output for formatting specifications.
# [All text in bold corresponds to input and the rest corresponds to output]
# Sample Input and Output 1:
# Enter City Details
# Enter city name
# Coimbatore
# Enter state name
# Tamilnadu
# Do you want to add another city? Type Yes / No
# Yes
# Enter city name
# Chennai
# Enter state name
# Tamilnadu
# Do you want to add another city? Type Yes / No
# Yes
# Enter city name
# Bangalore
# Enter state name
# Karnataka
# Do you want to add another city? Type Yes / No
# Yes
# Enter city name
# Vijayawada
# Enter state name
# Andhra
# Do you want to add another city? Type Yes / No
# Yes
# Enter city name
# Cochin
# Enter state name
# Kerala
# Do you want to add another city? Type Yes / No
# Yes
# Enter city name
# Bhopal
# Enter state name
# Madhya Pradesh
# Do you want to add another city? Type Yes / No
# No
# City Details
# Coimbatore is in state Tamilnadu
# Chennai is in state Tamilnadu
# Bangalore is in state Karnataka
# Vijayawada is in state Andhra
# Cochin is in state Kerala
# Bhopal is in state Madhya Pradesh
# State Details
# Tamilnadu has 2 cities
# Andhra has 1 cities
# Karnataka has 1 cities
# Kerala has 1 cities
# Madhya Pradesh has 1 cities

# Main.py
from City import City
from State import State

state_list = []
state_list.append(State("Tamilnadu",[]))
state_list.append(State("Andhra",[]))
state_list.append(State("Karnataka",[]))
state_list.append(State("Kerala",[]))

print("Enter City Details")
city_created_list = []
choice = "Yes"
while choice == "Yes" :
	city_name = input("Enter city name\n")
	state_name = input("Enter state name\n")
	state_found_flag = 0
	for state in state_list :
		if state_name == state.name :
			city = City(city_name, state)
			state.city_list.append(city)
			city_created_list.append(city)
			state_found_flag = 1
	if state_found_flag == 0 :
		state = State(state_name,[])
		state_list.append(state)
		city = City(city_name, state)
		city_created_list.append(city)
		state.city_list.append(city)
	choice = input("Do you want to add another city? Type Yes / No\n")

print("\nCity Details\n")
for city in city_created_list :
	print(city)

print("\nState Details\n")	
for state in state_list :
	print(state)

# City.py
class City:
    def __init__(self, name, state):
        self.__name = name
        self.__state = state
    
    @property
    def name(self):
        return self.__name
    
    @property
    def state(self):
        return self.__state
    
    def __str__(self):
        return f"{self.__name} is in state {self.__state.name}"

	
# State.py
class State:
    def __init__(self, name, city_list=None):
        self.__name = name
        if city_list is None:
            city_list = []
        self.__city_list = city_list
    
    @property
    def name(self):
        return self.__name
    
    @property
    def city_list(self):
        return self.__city_list
    
    @city_list.setter
    def city_list(self, city_list):
        self.__city_list = city_list
    
    def __str__(self):
        return f"{self.__name} has {len([city.name for city in self.__city_list])} cities"
