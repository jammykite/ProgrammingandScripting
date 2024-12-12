"""
Install the faker library (pip install faker). Read more about faker library here.
Generate 10 fake user profiles, each with a name, email, and address.
Store the profiles in a list of dictionaries.
"""

from faker import Faker

# Initialize the Faker instance
fake = Faker()

# Create a list to hold the user profiles
user_profiles = []

# Generate 10 fake user profiles
for _ in range(10):
    profile = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    }
    user_profiles.append(profile)

# Print the list of profiles
for i, profile in enumerate(user_profiles, 1):
    print(f"User {i}:")
    print(f"Name: {profile['name']}")
    print(f"Email: {profile['email']}")
    print(f"Address: {profile['address']}")
    print("-" * 40)

# If needed, you can access the list 'user_profiles' for further processing.
