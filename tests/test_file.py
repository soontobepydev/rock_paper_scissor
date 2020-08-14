## THIS FILE IS JUST FOR TESTING

x = {
  "rock": {
    "defeats" : ["scissors"],
    "defeated_by": ["paper"]
  },"paper": {
    "defeats" : ["rock"],
    "defeated_by": ["scissors"]
  },"scissors": {
    "defeats" : ["paper"],
    "defeated_by": ["rock"]
  }
}
print('dict itself')
print([a for a in x])
print("keys:")
print([b for b in x.keys()])
print('items:')
print([c for c in x.items()])
print('values:')
print([d for d in x.values()])
