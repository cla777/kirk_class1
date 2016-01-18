import yaml
import json
from pprint import pprint as pp

with open("foods_yaml.yml") as f:
 new_y=yaml.load(f)

pp(new_y)

with open("foods_json.json) as f:
 new_j=json.load(f)

pp(new_j)
