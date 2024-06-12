import json

JSON_DATA = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
        }
      }
   }
}

echo { "company":{ "employee":{ "name":"emma","payble":{ "salary":7000, "bonus":800}}}} | python -m json.tool


#-------------------------------OR----------------------------------


import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is ", isValid)