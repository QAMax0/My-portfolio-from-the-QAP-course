##  Get
import requests

status = 'pending'
res_get_status = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                              headers={'accept': 'application/json'})
print(res_get_status.json())


##  Post
data = {"id": 9223372036854742132,
        "category": {
          "id": 0,
          "name": "Dog"
        },
        "name": "Boris",
        "photoUrls": [
          "string"
        ],
        "tags": [
          {
            "id": 0,
            "name": "RUSSIAN"
          }
        ],
        "status": "available"}

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

res_post_new_pet = requests.post(f"https://petstore.swagger.io/v2/pet", headers=headers, json=data)

print(res_post_new_pet.json())

##  Put

data_put = {"id": 9223372036854742132,
            "category": {
                "id": 0,
                "name": "Dog"
            },
            "name": "BUBL",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "Big baby"
                }
            ],
            "status": "available"}

headers_put = {'accept': 'application/json', 'Content-Type': 'application/json'}

res_put = requests.put(f"https://petstore.swagger.io/v2/pet", headers=headers_put, json=data_put)

print(res_put.json())

##  Delete

res_delete = requests.delete(f"https://petstore.swagger.io/v2/pet/9223372036854742132",
                             headers={'accept': 'application/json'})

print(res_delete.json())
