# # CONTINUE stmt
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == 'spam': # If item is spam then it will ignore it and continue
#         print("I am ignoring "+ item)
#         continue # Forces the loop to run through and start from the beginning again
#     print("Buy "+item)
#
# # BREAK stmt
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == 'spam': # If item is spam then it will ignore it and continue
#         break # This will terminate the FOR loop here itself and nothing will be executed after this point
#     print("Buy "+item)

# If you remove SPAM from the list, you'll get an error, just check it out
meal = ["rice", "eggs", "spam", "bacon"]
# Inorder to remove the above error, declare nasty_food_item outside the FOR loop
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else: # As ELSE is also a good place to initialize the nasty_food_item variable
    # nasty_food_item = '' # Not a good choice, all the variables have to be initialized before hand itself
    print("I'll have a plate of that, then, please !!")

if nasty_food_item:
    print("Can I have something without spam in it ?")
