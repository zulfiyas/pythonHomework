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

removed_value = sample_dict.pop("city", None)
print("Removed 'city' with value:", removed_value)
