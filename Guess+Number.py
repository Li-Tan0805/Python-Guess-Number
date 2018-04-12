
# coding: utf-8

# In[20]:

from random import randint
import functions

print "Guessing Numbers!"
print "Rule: You are given 8 chances, in each chance, type in a four digit number, the system will then return the result as A and B - A means correct number in the correct position; B means correct number in the wrong position."
raw_input("Press Enter to start:")

chance = 8
a = randint(1, 9)
b = randint(0, 9)
c = randint(0, 9)
d = randint(0, 9)
while not (a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
    a = randint(1, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
correct_number=a*1000+b*100+c*10+d
#print correct_number

while chance>0:
    guess_number=input("please type in four-digit number:")
    while ((type(guess_number)!=type(1234)) or (guess_number<1000) or (guess_number>9999)):
        guess_number=input("Not qualified, please re-enter:")
    while num_evaluate(guess_number)==0:
        guess_number=input("Not qualified, please re-enter:")
    if guess_number==correct_number:
        print "You get it! The correct number is "+`correct_number`+" !"
        break     
    chance -= 1
    print num_match(guess_number,correct_number)+" - You have "+`chance`+" chances left!"

if (chance==0):
    print "You lose! The correct number is "+`correct_number`
print "End!"


# In[ ]:



