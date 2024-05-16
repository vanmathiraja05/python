complex_dict = {
    'personal_info': {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main Street',
            'city': 'Anytown',
            'zipcode': '123458'
        }
    },
    'work_info': {
        'position': 'Software Engineer',
        'company': 'Tech Corp',
        'projects': [
            {'name': 'Project A', 'status': 'Completed'},
            {'name': 'Project B', 'status': 'In Progress'}
        ]
    },
    'contacts': [
        {'name': 'Alice', 'phone': '555-1234'},
        {'name': 'Bob', 'phone': '555-5678'}
    ]
}

# Iterating through personal_info
print("Personal Information:")
for key, value in complex_dict['personal_info'].items():
    if isinstance(value, dict):  # Check if the value is a dictionary
        print(key + ":")
        for inner_key, inner_value in value.items():
            print(f"  {inner_key}: {inner_value}")
    else:
        print(f"{key}: {value}")

# Iterating through work_info
print("\nWork Information:")
for key, value in complex_dict['work_info'].items():
    if isinstance(value, list):  # Check if the value is a list
        print(key + ":")
        for item in value:
            for inner_key, inner_value in item.items():
                print(f"  {inner_key}: {inner_value}")
    elif isinstance(value, dict):  # Check if the value is a dictionary
        print(key + ":")
        for inner_key, inner_value in value.items():
            print(f"  {inner_key}: {inner_value}")
    else:
        print(f"{key}: {value}")

# Iterating through contacts
print("\nContacts:")
for contact in complex_dict['contacts']:
    for key, value in contact.items():
        print(f"{key}: {value}")
