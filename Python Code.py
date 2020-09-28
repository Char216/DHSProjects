print("Title of program: Meow Encouragement")
print()
print("Hi there! With this project, you can get some advice from a cat and hopefully feel better ฅ^•ﻌ•^ฅ")
print()
while True:
  description = input("Do you need some encouragement, meow?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "Yes" or "yes":
      feelings_list.append("yes")
      encouragement_list.append("Are things just not going your way, meow?")
      counter += 1
    if each_word == "No" or "no":
      feelings_list.append("no")
      encouragement_list.append("That's good, it means you're feeling alright! If you ever need encouragement, just ask meow!")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = encouragement_list[0] 

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
