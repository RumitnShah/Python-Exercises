sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

minimum = min(sample_dict)

print(minimum)


#-----------------------OR-------------------------

mini = min(sample_dict, key=sample_dict.get)

print(mini)