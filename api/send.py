import json
import requests


response = requests.post(
            # url='http://localhost:8000/api/v1/users/', 
            url='http://localhost:8001/api/v1/auth/users/', 
            json=({
                    "id": "99ed5bd7-533c-4766-b6cf-6332040a63b9",
                    "email": "crn96ml@gmail.com",
                    "username": "crn96ml@gmail.com",
                    "password": "@Muleya67",
                    # "first_name": "Carrington"
                }),
            headers={"Content-Type":"application/json"}
        )

print(response)