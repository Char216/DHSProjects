print("Title of program: Meow Encouragement")
print()
print("Hi there! With this project, you can look at some cute cats and hopefully feel better ฅ^•ﻌ•^ฅ")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

kitten1 = input("I like kittens more than grown cats.")

ginger1 = input("I like ginger-coloured cats.")

calico1 = input("I like Calico cats.")

black1 = input("I like black cats.")

2 = input("I'm good with tying knots and ropes.")

music2 = input("I play a musical instrument well.")


tech_final = int(tech1) + int(tech2)
outdoor_final = int(outdoor1) + int(outdoor2)
music_final = int(music1)+ int(music2)

print()

if tech_final > outdoor_final and tech_final > music_final:
  print("You might be suitable for Infocomm club!")
elif outdoor_final > music_final:
  print("You might be stuiable for ODAC!")
else:
  print("You might be suitable for Band!")
