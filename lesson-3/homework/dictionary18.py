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

from collections import defaultdict
default_dict = defaultdict(lambda: "Default Value", sample_dict)
print("Default value for missing key 'unknown':", default_dict["unknown"])
