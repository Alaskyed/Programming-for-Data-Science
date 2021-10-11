HOLIDAYS_EG = [ ["Brighton",            150,  ["beach", "culture"]], 
                  ["Whitby",              100,  ["beach", "culture"]],
                  ["Barcelona",           320,  ["beach", "culture", "hot"]],
                  ["Doncaster",            40,  []],
                  ["Crete",               300,  ["beach", "hot"]],
                  ["London",              250,  ["culture"]],
                  ["Sicily",              300,  ["culture", "hot", "beach"]],
                  ["Barbados",           1250,  ["hot", "beach"]],
                  ["Tanzania",            2500, ["hot", "beach", "wildlife"]],
                  ["Galapagos Islands",  4500,  ["beach", "culture", "hot", "wildlife"]],      
             ]   

def recommend_holidays( max_cost, attributes, holiday_data):
    holiday_data.sort(key=lambda x:x[1])
    destinations_list=[]

    for feature in holiday_data:
        if feature[1] <= max_cost and set(attributes) <= set(feature[2]):
            destinations_list.append(feature[0])
    return sorted(destinations_list)




# Test
print(recommend_holidays(500, ["beach", "culture"], HOLIDAYS_EG))