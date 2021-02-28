
test_dict = {1:"Hello", 2:"World", 3:3}
print("This is my test_dict:", test_dict)
#Change code above this line only if the task is asking you to
user_profile={'name':'Mark', 'age':16,'skills':['Python','Java']}
print(user_profile['age'])
print(user_profile.get('name'))

user_profile['age'] = 26
user_profile['address']='Downtown'
user_profile.pop('address')
print(user_profile)
del user_profile['age']
print(user_profile)

user_list=list(user_profile.items())
print(user_list)
user_dict=dict(user_list)
print(user_dict)

friends={
    "Best1":"USA",
    "Best2":"Cameroon",
    "Best3":"Cameroon"
}
for k,v in friends.items():
    print(k+"'s favourite country is:" + v)


