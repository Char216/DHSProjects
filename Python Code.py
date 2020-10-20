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
    
    if each_word == "yes":
      feelings_list.append("low")
      encouragement_list.append("that no matter how bad things are, they will get better eventually. You're not alone and there are always people who care for you and whom you can turn to for help.")
      counter += 1
    if each_word == "no":
      feelings_list.append("good")
      encouragement_list.append("that if you ever need encouragement, just ask meow or look for someone who can help you!")
      counter += 1

  if counter == 0:
    
      output = "Sorry, I don't really understand. Perhaps you could use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Please always remember "+ encouragement_list[0] + " Life can be tough but sometimes all you need is a cuddly cat :)"

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + " Life can be tough but sometimes all you need is a cuddly cat :)"

  print()
  print(output)
  print()
