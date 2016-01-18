import json 

foods=['steak', 'cheese']
foods.append({})
foods[-1]['desserts']='cake'
foods[-1]['appetizers']='calamari'

with open("foods_json.json", "w") as f:
 json.dump(foods,f) 

