sample_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "hobbies": ["reading", "cycling", "cooking"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

if "name" in sample_dict:
    pair = ("name", sample_dict["name"])
    print("Key-value pair for 'name':", pair)
else:
    print("Key 'name' not found")
