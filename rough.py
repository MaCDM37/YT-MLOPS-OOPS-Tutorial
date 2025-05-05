#lst = [1,2,3]
#my_str = "mlops playlist"
#my_int = 155
#print(type(lst))
#print(type(str))
#print(type(my_int))
#lst.clear()
#print(lst)
#my_str = my_str.capitalize()
#print(my_str)

from oops_proj import chatbook

#function
lst = [1,2,3]
#a1 = len(lst)
#print(a1)
# this is how we use a function, we are taking up the object first to call a method
# this is how we call a method
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

# getter and setter
#print(user1.get_name())
#user1.set_name("Agent X")
#print(user1.get_name())
# we will want some attributes, which should not be accessed by you
# this additional layer of security is called encapsulation

# getter and setter used to get and set the hidden attribute

