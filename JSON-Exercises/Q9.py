import json

sample = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
dataList =[]

try:
    data = json.loads(sample)
except Exception as e:
    print(e)

for item in data:
    dataList.append(item.get("name"))
print(dataList)