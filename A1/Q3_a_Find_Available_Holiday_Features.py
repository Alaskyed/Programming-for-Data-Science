# This question has a mistake, you should change the 'A1_P4DS_Python_Programming_test.py' file.
# Changing the last item of HOLIDAYS_EG as ["beach", "culture", "hot", "wildlife"]
HOLIDAYS_EG = [ ["Scarborough",  45,  ["beach"]], 
                ["Whitby",       60,  ["beach", "culture"]],
                ["Barcelona",   320,  ["beach", "culture", "hot"]], 
                ["Corfu",       300,  ["beach", "hot"]],
                ["Paris",       250,  ["culture"]],
                ["Rome",        300,  ["culture", "hot"]],
                ["Switzerland", 450,  ["culture", "mountains"]],
                ["California",  750,  ["beach", "hot", "mountains"]],      
             ]   


def available_features(max_cost, holiday_data):
    holiday_data.sort(key=lambda x:x[1])
    destinations_set=set()

    for feature in holiday_data:
        if feature[1] <= max_cost:
            destinations_set = destinations_set | set(feature[2])
    return sorted(list(destinations_set))

result = available_features(5000, HOLIDAYS_EG)
print(result)