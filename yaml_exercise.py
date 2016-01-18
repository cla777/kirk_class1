import yaml

foods=['steak', 'cheese']
foods.append({})
foods[-1]['desserts']='cake'
foods[-1]['appetizers']='calamari'

with open("foods_yaml.yml", "w") as f:
 f.write(yaml.dump(foods, default_flow_style=False)

