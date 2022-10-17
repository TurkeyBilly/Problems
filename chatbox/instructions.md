To get started, you’ll have to pick a local restaurant to build your chatbot for.

Once you have a restaurant in mind, let’s begin by creating a menu.

Rather than add a bunch of print statements to your program to print out the menu, create a list that includes all of the menu items:

```python
menu = ["Pasta", "Soup"]
```
This will come in handy when getting orders from users, and explaining the menu to them.

You should also create a list that stores the possible reservation times that are available to customers. The easiest way to store this information is as String values:

```python
reservation_times = ["7:15"]
```
Lastly, create a function ```print_options```, that provides users with a list of options to choose from. This list should include:

Information on the restaurants menu.
Information on the daily specials.
Make reservations for users.
Take orders for pickup
Users should be able to choose from one of those options. Feel free to include additional options as well!

You should call ```print_options``` to the console so the results come up like so:
```
Welcome to Nino's Pizzeria!
How can I help you?
1. Take a look at the menu.
2. Ask about daily specials.
3. Make a reservation.
4. Order take out.
5. Exit.
```
 

Find the list tutorials here: https://cscircles.cemc.uwaterloo.ca/13-lists/ 

Use this exercise to complete your rule-based chatbot.

For each option that the user can choose from, you should create a separate function that executes when the user chooses that option. For example, if a user wants to see the menu, then a ```print_menu``` function should execute, and provide the menu information to the user. This will make it easy to debug your chatbot and keep things a little more organized.

Each option should also complete a specific task:

Take a look at the menu: Should print the menu to the user.
Ask about daily specials: Should print the daily specials.
Make a reservation: Should show users the available reservation times and allow a user to choose a time. If the user has chosen an appropriate time, take that time out of the available reservations.
Order take out: Should print the menu for the user to see, and allow them to order things on the menu. When the user is done ordering, then their order should be read to them. Consider using a list to store the users order!
Exit: Should exit the program and thank the user for visiting.
Hints:

Successive print statements will print to the console almost automatically. If you want to create a delay in the response time, so that it seems more like a conversation, use the time library to delay when the print statements execute.

You will need to import ```time``` at the top of your program. Then, you can use the function ```time.sleep(seconds)```, which will delay the execution of your program for second amount of seconds. 

If you want your program to be the most realistic, use while loops to make sure users enter the appropriate information into the program. For example, if a user enters a food item that is not on the menu, repeatedly ask for something that’s on the menu using a while loop:

```python
while choice not in menu:
    choice = input("Please enter a valid menu item")
```
