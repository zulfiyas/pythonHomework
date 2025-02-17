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

keys_with_value = [k for k, v in sample_dict.items() if v == "Engineer"]
print("Keys with value 'Engineer':", keys_with_value)
