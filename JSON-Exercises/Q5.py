import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

salary = json.loads(sampleJson)

print(salary["company"]["employee"]["payble"]["salary"])