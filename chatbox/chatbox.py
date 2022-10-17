menu = ["Pasta", "Soup", "Rice"]
daily_specials = ["John Deng", "Max Li", "Tomato Egg soup", "Noodle"]
reservation_times = ["7:15", "8:00"]

user_order = []
reserved_time = []

def print_options():
    print(
        '''Welcome to Nino's Pizzeria!
        How can I help you?
        1. Take a look at the menu.
        2. Ask about daily specials.
        3. Make a reservation.
        4. Order take out.
        5. Exit.
        '''
    )

def f_print(subject: list[str]):
    print(*["\n" + "\t" +f"{i + 1}. {subject[i]}"for i in range(len(subject))])
    # for i in range(len(subject)):
    #   print()
    #   print("\t" + str(i + 1) + str(subject[i]), end="")

def print_menu():
    print()
    print("Menus: ")
    print(*["\n" + "\t" +f"{i + 1}. {menu[i]}"for i in range(len(menu))])

def print_daily_special():
    print()
    print("Daily Special: ")
    print(*["\n" + "\t" +f"{i + 1}. {daily_specials[i]}"for i in range(len(daily_specials))])

def make_reservation():
    print()
    print("Avaliable Slots: ")
    print(*["\n" + "\t" +f"{i + 1}. {reservation_times[i]}"for i in range(len(reservation_times))])
    c = input(
        f"Plz make your order, type numbers from 1 to {len(reservation_times)}, and seperate using space "
    )
    l = c.split()
    try:
        [reserved_time.append(reservation_times[int(i) - 1]) for i in l]
    except IndexError as e:
        print(e)
        print(f"Plz input again! Only numbers from 1 to {len(reservation_times)} are allowed!")
        reserved_time.clear()
        make_reservation()

    print("Reserved time: ")
    f_print(reserved_time)

def make_order():
    print()
    print_menu()
    print()
    c = input(
        f"Plz make your order, type numbers from 1 to {len(menu)}, and seperate using space "
    )
    l = c.split()
    try:
        [user_order.append(menu[int(i) - 1]) for i in l]
    except IndexError as e:
        print(e)
        print(f"Plz input again! Only numbers from 1 to {len(menu)} are allowed!")
        user_order.clear()
        make_order()

    print("Checked out orders: ")
    f_print(user_order)

operations: dict[int, callable] = {
    1: print_menu,
    2: print_daily_special,
    3: make_reservation,
    4: make_order,
    5: exit
}

if __name__ == "__main__":
    while True:
        print_options()
        operations[int(input("Enter Your Choice: "))]()
