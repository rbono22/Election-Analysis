print("Hello World")


ballots = 3,134
nballots = 8

num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
num_candidates

8 // 5 - 3
8 + 22 * 2 - 4

3 ** 3 % 5

5 + 9 * 3 / 2 - 4

3 ** (3 % 5)

5 + (9 * 3 / 2 - 4)

5 + (9 * 3 / (2 - 4))

counties = ["Arapahoe","Denver","Jefferson"]
  
counties[0]

print(counties[-1])
 
counties_tuple[:-1]

counties_tuple[2]

counties_tuple[:2]

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict

counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
len(counties_dict)
counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
counties_dict.values()
dict_values([422829, 463353, 432438])
counties_dict.get("Denver")

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data
len(voting_data)

voting_data.get('Arapahoe')

voting_data.get('Denver')

voting_data[0]

[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}]
voting_data.append({'county' : 'El Chapo', 'registered_voters': 467789})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Chapo', 'registered_voters': 467789}]
voting_data.insert(4, {'county': 'Sunnyvale', 'registered_voters': 477888})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'El Chapo', 'registered_voters': 467789}, {'county': 'Sunnyvale', 'registered_voters': 477888}]
voting_data.pop(5)

voting_data.pop(4)
{'county': 'Sunnyvale', 'registered_voters': 477888}
voting_data.pop(3)
{'county': 'El Chapo', 'registered_voters': 467789}
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.insert(2, {'county': 'El Paso', 'registered_voters': 461149})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.pop(2)
{'county': 'El Paso', 'registered_voters': 461149}
voting_data.insert(1, {'county': 'El Paso', 'registered_voters': 461149})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.pop(0)
{'county': 'Arapahoe', 'registered_voters': 422829}
  
