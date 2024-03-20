class Profile:

    def __init__(self, status, username, location, age = 0):
        self.status = status
        self.username = username
        self.location = location
        self.age = age

status2 = input("Enter status: ")
username2 = input("Enter username: ")
location2 = input("Enter location: ")
age2 = int(input("Enter age: "))

default_profile = Profile('active', 'sienna-elk', 'New York')
profile2 = Profile(status2, username2, location2, age2)

print(f'Default profile data: {default_profile.status}, user {default_profile.username}, located in {default_profile.location}, {default_profile.age} years old')
print(f'profile2 data: {profile2.status}, user {profile2.username}, located in {profile2.location}, {profile2.age} years old')
