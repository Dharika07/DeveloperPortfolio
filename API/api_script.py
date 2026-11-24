
import json

with open("api_response.json", "r") as file:
    data = json.load(file)

print("API Response Data")
print("User ID:", data["userId"])
print("ID:", data["id"])
print("Title:", data["title"])
print("Completed:", data["completed"])
