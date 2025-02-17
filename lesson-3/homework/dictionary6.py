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

sample_dict2 = {
    "country": "USA",
    "married": False,
    "profession": "Data Scientist",
    "experience": 5
}

sample_dict2 = {"country": "USA", "married": False}
merged_dict = {sample_dict, sample_dict2}
print("Merged dictionary:", merged_dict)
