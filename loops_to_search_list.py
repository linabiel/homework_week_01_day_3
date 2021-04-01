# Given a list of users, create a function to find the user with a user_id of 4.

# define a function find user id
# pass two paramaters of list and id_number



users = [
    {"user_id": 1, "first_name": "Margaret", "last_name": "Chicken"},
    {"user_id": 2, "first_name": "Bill", "last_name": "Gates"},
    {"user_id": 3, "first_name": "Steve", "last_name": "Jobs"},
    {"user_id": 4, "first_name": "Guido", "last_name": "van Rossum"},
    {"user_id": 5, "first_name": "Brendan", "last_name": "Eich"},
]

people = [
    {"user_id": 1, "first_name": "Margaret", "last_name": "Chicken"},
    {"user_id": 2, "first_name": "Bill", "last_name": "Gates"},
    {"user_id": 3, "first_name": "Steve", "last_name": "Jobs"},
    {"user_id": 4, "first_name": "Lina", "last_name": "van Rossum"},
    {"user_id": 5, "first_name": "Brendan", "last_name": "Eich"},
]


def find_user_by_id(list_of_users, id_number):
    for user in list_of_users:
        if user['user_id'] == id_number:
            return user

print(find_user_by_id(users, 4))


def find_user(list_of_users, user_id):
    user_im_looking_for = None
    for user in list_of_users:
        if user['user_id'] == user_id:
            user_im_looking_for = user
    return user_im_looking_for


# def find_user(user_id):
#     for user in users:
#         if user['user_id'] == user_id:
#             return user


print(find_user(people, 4))
