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

sorted_by_key = dict(sorted(sample_dict.items(), key=lambda item: item[0]))
print("Dictionary sorted by key:", sorted_by_key)
