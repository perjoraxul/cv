#create class
class User :
    pass
#create a new object from that class
user_1 = User()
#create an attribute -a variable associated with an object/the things that the object has - for that class
#this below adds the attribute "id" to that class 
user_1.id = "001"

#initialization - he assignment of an initial value for a data object or variable
#constructor -  part of a class which alowes us to specify what should happen when our object is being constructed (when the object is being initialized)

class Car :
    def __init__(self,seats,windows) :
        self.seats = seats
        self.windows = windows
        self.acceleration = 0
    

my_car = Car(5,4)
print(my_car)
#the convention is : the name of the parameter -that is passed to the function - is the same as the name of the attribute; but it can be different if you want

#methods - the things that the object does   

class UserAdvanced : 
    def __init__(self, user_id, username) :
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user) :
        user.followers += 1
        self.following += 1

user_1 = UserAdvanced("1","Rihanna")
user_2 = UserAdvanced("2", "Radu")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)