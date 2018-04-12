
# coding: utf-8

# In[ ]:

def num_evaluate(num):
    d = num % 10
    c = ((num-d) % 100)/10
    b = ((num - d - 10*c) % 1000) / 100
    a = (num - d - 10*c - 100*b) / 1000
    if (a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        return 1
    else: 
        return 0


# In[ ]:

def num_parse(num):
    d = num % 10
    c = ((num-d) % 100)/10
    b = ((num - d - 10*c) % 1000) / 100
    a = (num - d - 10*c - 100*b) / 1000
    result =[a,b,c,d]
    return result


# In[ ]:

def num_match(num1,num2):
    output=[]
    num1_parse=num_parse(num1)
    num2_parse=num_parse(num2)
    for i in range(len(num1_parse)):
        if num1_parse[i]==num2_parse[i]:
            output.append('A')
        elif(num1_parse[i] in num2_parse):
            output.append('B')
    num_A=output.count("A")
    num_B=output.count("B")
    message=`num_A`+" A "+`num_B`+" B"
    return message

