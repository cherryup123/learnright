from sys import argv
script,user_name,age_s=argv
prompt='enter :'
print("Hi%s,I'm the %s script"%(user_name,script))
print("I'd like to ask you a few question.")
print("Do you like me %s?"%user_name)
likes=raw_input(prompt)
print("I'm %s?"%age_s)
age_s=raw_input(prompt)
print("What kind of computer do you have?")
computer=raw_input(prompt)
print(""""
Alright, so you said %r about liking me.
You live in %r I'm %r."""%(likes,computer,age_s))
#python ex14.py zed 18
