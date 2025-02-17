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

inverted_dict = {v: k for k, v in sample_dict.items() if not isinstance(v, (list, dict))}
print("Inverted dictionary:", inverted_dict)
