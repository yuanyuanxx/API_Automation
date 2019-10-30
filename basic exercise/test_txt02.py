import json
# class Die():
    # username=input('What is your name?')
    # filename='username.json'
    # with open(filename,'w') as f_obj:
    #     json.dump(username,f_obj)
    #     print("We'll remember you when you came back!")

    # def roll_die(self):
    #     i = 1
    #     while i < 11:
    #         x = random.randint(1, 6)
    #         print(x)
    #         i += 1
        #



# def test_demo1():
#     username = input('What is your name?')
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you came back!")

def get_username():
     filename='username.json'
     try:
         with open(filename) as f_obj:
             username=json.load(f_obj)
     except FileNotFoundError:
         return None
     else:
         return username

def get_new_username():
    username = input('What is your name?')
    filename='username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username=get_username()
    if username:
        print('Welcome back,'+username+"!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
