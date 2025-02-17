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

hashable_values = [v for v in sample_dict.values() if isinstance(v, (int, float, str, tuple))]
unique_count = len(set(hashable_values))
print("Unique hashable values:", unique_count)