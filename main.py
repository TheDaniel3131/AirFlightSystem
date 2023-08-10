# ............................................PYTHON GROUP PROJECT......................................................
# ............................................AIR MALAYSIA GROUP........................................................

# Daniel Poh Ting Fong # TP056258
# Jackin Fu Yi Qing # TP055908
# Thum Yong Hui # TP053924

# IMPORT
# Class of colours, highlights, and styles
import time

import datetime

e = datetime.datetime.now()


def timenow():
    now_time = time.asctime()
    return now_time


class colour:
    dark_cyan = '\033[36m'
    black = '\033[90m'
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    purple = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'

    # highlights
    hblack = '\033[40m'
    hred = '\033[41m'
    hgreen = '\033[42m'
    hyellow = '\033[43m'
    hblue = '\033[44m'
    hlightpurple = '\033[45m'
    hlightgreen = '\033[46m'
    hwhite = '\033[47m'


class style:
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


def amg_main_page():
    time.sleep(0.6)
    print(style.bold + "-" * 150)
    print("-" * 150 + style.end)
    # print(" ")
    print(colour.blue + style.bold)
    print("\t\t\t\t\t\t\t\t\t\t\t     ", "//""\\""\\", "     ||\\""\\          //||", "   ==========")
    print("\t\t\t\t\t\t\t\t\t\t\t    ", "//  ""\\""\\", "    || \\""\\        // ||", " //          \\\\")
    print("\t\t\t\t\t\t\t\t\t\t\t   ", "//____""\\""\\", "   ||  \\""\\      //  ||", "||       ======")
    print("\t\t\t\t\t\t\t\t\t\t\t  ", "//______""\\""\\", "  ||   \\""\\    //   ||", "||       ======")
    print("\t\t\t\t\t\t\t\t\t\t\t ", "//        ""\\""\\", " ||    \\""\\  //    ||", " \\\\          //")
    print("\t\t\t\t\t\t\t\t\t\t\t", "//          ""\\""\\", "||     \\""\\//     ||", "   ==========")
    print(style.end)
    # print(" ")
    print(style.bold + "-" * 150)
    print("-" * 150 + style.end)
    print(" ")
    print(colour.blue + (e.strftime("%a %b %d %H:%M:%S %Y").center(135) + style.end))
    print("\n\n")

    time.sleep(0.6)
    title = "<<< WELCOME TO AMG >>>"
    amg_title = title.center(135)
    print(colour.white + style.bold + amg_title.upper() + style.end)
    print("\n\n")

    time.sleep(0.6)
    main_page_option = input("\t\t\t\t\t\t\t\t\t\t\tPlease choose the following options to continue.:"
                             '\n\t\t\t\t\t\t\t\t\t\t\t--------------------------------------------------'
                             '\n'
                             '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t[1] Registered as Customer.'
                             '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t[2] Login as Customer.'
                             '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t[3] Login for Admins only.'
                             '\n'
                             '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[4] Exit system'
                             '\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tOption: ')

    if main_page_option == '1':
        time.sleep(1.0)
        flight_title()
        time.sleep(0.3)
        display_option()

    elif main_page_option == '2':
        welcome_message()
        time.sleep(1.25)
        login_title_message()
        time.sleep(0.25)
        login_registered_users()
        time.sleep(0.5)

    elif main_page_option == '3':
        time.sleep(1.0)
        admin_login_title()
        time.sleep(0.4)
        admin_login_access()

    elif main_page_option == '4':
        time.sleep(0.8)
        print("\n")
        print(
            "\t" * 9 + colour.green + style.bold + ">>> Exit Successfully! Thank you for visiting our website <<<" + style.end)

    else:
        time.sleep(0.8)
        print("\n")
        print(
            "\t" * 9 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 4 to proceed. <<<" + style.end)
        amg_main_page()


# 1..............................................Registered as Customer.................................................

# flight title
def flight_title():
    title = "Welcome to Airline Reservations System (ARS)"
    full_title = title.center(150)
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(colour.hyellow + colour.white + style.bold + full_title.upper() + style.end)
    print(" ")
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(" ")


# flight_title()

# 1.1.	Display all airline schedules
def display_flight_schedule():
    f = open("flight_schedule.txt", "r")
    content = f.read()
    # print("WHOLE", content)
    content_list_flight_schedules = content.splitlines()
    # print("BYLINE:", content_list_flight_schedules)
    print("~" * 50)
    for flight_schedule in content_list_flight_schedules:
        detail = flight_schedule.split(";")
        # print("~" * 50)
        time.sleep(0.3)
        print("Airline Number       :", detail[0])
        print("Departure Country    :", detail[1])
        print("Departure Time       :", detail[2])
        print("Departure Date       :", detail[3])
        print("Arrive Country       :", detail[4])
        print("Arrive Time          :", detail[5])
        print("Journey Duration     :", detail[6])
        print("Return Date          :", detail[7])
        print("~" * 50)
    f.close()


# 1.2.	Search airline by from, to, date departure, date return
def search_flight():
    print("-" * 150)
    search = input("\nEnter option below:"
                   "\n"
                   "\n[1]From:"
                   "\n[2]To:"
                   "\n[3]Date Departure:"
                   "\n[4]Date Return:"
                   "\n"
                   "\n[5]Back to the main page."
                   "\n"
                   "\nOption: ")
    print("-" * 150)

    if search == '1':
        with open("flight_schedule.txt", "r") as file:
            word = input("Which of the country did you choose From:")
            flag = 0
            for line in file:
                detail = line.split(";")
                if word == detail[1]:
                    flag = 1
                    if flag == 1:
                        print("~" * 50)
                        print("Airline Number       :", detail[0])
                        print("Departure Country    :", detail[1])
                        print("Departure Time       :", detail[2])
                        print("Departure Date       :", detail[3])
                        print("Arrive Country       :", detail[4])
                        print("Arrive Time          :", detail[5])
                        print("Journey Duration     :", detail[6])
                        print("Return Date          :", detail[7])
                        print("~" * 50)
            if flag == 0:
                print("\n" + colour.red + "-" * 67 + "Invalid option " + "-" * 68 + style.end)
                search_flight()
            search_flight()

    elif search == '2':
        with open("flight_schedule.txt", "r") as file:
            word = input("Which of the country did you choose To:")
            flag = 0
            for line in file:
                detail = line.split(";")
                if word == detail[4]:
                    flag = 1
                    if flag == 1:
                        print("~" * 50)
                        print("Airline Number       :", detail[0])
                        print("Departure Country    :", detail[1])
                        print("Departure Time       :", detail[2])
                        print("Departure Date       :", detail[3])
                        print("Arrive Country       :", detail[4])
                        print("Arrive Time          :", detail[5])
                        print("Journey Duration     :", detail[6])
                        print("Return Date          :", detail[7])
                        print("~" * 50)
            if flag == 0:
                print("\n" + colour.red + "-" * 67 + "Invalid option " + "-" * 68 + style.end)
                search_flight()
            search_flight()

    elif search == '3':
        with open("flight_schedule.txt", "r") as file:
            word = input("Which of the departure date did you choose :")
            flag = 0
            for line in file:
                detail = line.split(";")
                if word == detail[3]:
                    flag = 1
                    if flag == 1:
                        print("~" * 50)
                        print("Airline Number       :", detail[0])
                        print("Departure Country    :", detail[1])
                        print("Departure Time       :", detail[2])
                        print("Departure Date       :", detail[3])
                        print("Arrive Country       :", detail[4])
                        print("Arrive Time          :", detail[5])
                        print("Journey Duration     :", detail[6])
                        print("Return Date          :", detail[7])
                        print("~" * 50)
            if flag == 0:
                print("\n" + colour.red + "-" * 67 + "Invalid option " + "-" * 68 + style.end)
                search_flight()
            search_flight()

    elif search == '4':
        with open("flight_schedule.txt", "r") as file:
            word = input("Which of the  return date did you choose :")
            flag = 0
            for line in file:
                detail = line.split(";")
                if word == detail[7]:
                    flag = 1
                    if flag == 1:
                        print("~" * 50)
                        print("Airline Number       :", detail[0])
                        print("Departure Country    :", detail[1])
                        print("Departure Time       :", detail[2])
                        print("Departure Date       :", detail[3])
                        print("Arrive Country       :", detail[4])
                        print("Arrive Time          :", detail[5])
                        print("Journey Duration     :", detail[6])
                        print("Return Date          :", detail[7])
                        print("~" * 50)
            if flag == 0:
                print("\n" + colour.red + "-" * 67 + "Invalid option " + "-" * 68 + style.end)
                search_flight()
            search_flight()

    elif search == '5':
        flight_title()
        display_option()

    else:
        print(
            colour.red + "-" * 43 + "Invalid input! Please pick the numbers 1 , 2 , 3 , 4 to proceed" + "-" * 44 + style.end)
        search_flight()


# 1.3.	Add new customer register to access other details
def register():
    print("-" * 150)
    print("\n///Please Fill Up Your Details///")
    print("---------------------------------\n")
    username = input("Enter your new Username: ")
    password = input("Enter your new Password: ")
    print("\n>>>")

    flag = 0
    for i in open("user.txt", "r").readlines():
        user_details = i.split(",")
        if username in user_details[0]:
            print(colour.red + "Username repeated!" + style.end)
            flag = flag + 1
    if flag != 0:
        register()
    else:
        full_name = input("Enter your Full Name: ")
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        gender = input("Enter your Gender: ")
        date_of_birth = input("Enter your Date of Birth: ")
        contact_num = input("Enter your Contact Number: ")
        citizenship = input("Enter your Citizenship: ")
        tdd = input("Enter Your TDD: ")
        emergency_contact = input("Enter your Emergency Contact: ")
        save_card = input("Enter your Card Type(Debit/Credit/...): ")
        save_card_num = input("Enter your your Card Number: ")
        valid_date_through = input("Enter your Card Valid Date: ")
        cvv = input("Enter your Card CVV: ")

        user_regiser = []
        user_regiser.append(username)
        user_regiser.append(password)
        user_regiser.append(full_name)
        user_regiser.append(first_name)
        user_regiser.append(last_name)
        user_regiser.append(gender)
        user_regiser.append(date_of_birth)
        user_regiser.append(contact_num)
        user_regiser.append(citizenship)
        user_regiser.append(tdd)
        user_regiser.append(emergency_contact)
        user_regiser.append(save_card)
        user_regiser.append(save_card_num)
        user_regiser.append(valid_date_through)
        user_regiser.append(cvv)

        file = open("user.txt", "a")
        for user in user_regiser:
            file.write(user + ",")
        file.write("\n")
        file.close()
        print(colour.green + "-" * 56 + "You have successfully be our member" + "-" * 57 + style.end)


# display all option
def display_option():
    print("\n\n")
    print(">>>")
    option = input("\nEnter option below:"
                   '\n--------------------'
                   '\n\n【1】Display all airline schedule.'
                   '\n【2】Search airline by from, to, date departure, date return.'
                   '\n【3】Add new customer register to access other details.'
                   '\n【4】Log out.'
                   '\n\nOption: ')

    if option == '1':
        display_flight_schedule()
        display_option()

    elif option == '2':
        search_flight()
        display_option()

    elif option == '3':
        register()
        display_option()

    elif option == '4':
        print("\n")
        print(colour.green + "-" * 64 + "Log Out Successful..." + "-" * 65 + style.end)
        amg_main_page()
    else:
        print("\n")
        print(
            colour.red + "-" * 43 + "Invalid input! Please pick the numbers 1 , 2 , 3 , 4 to proceed" + "-" * 44 + style.end)
        display_option()


# 2...............................................Login as Customer.....................................................

def welcome_message():
    AMG_title = "Welcome to Air Malaysia Group (AMG)"
    AMG_full_title = AMG_title.center(143)
    ARS_title = "Online Airline Reservation System of AMG"
    ARS_full_title = ARS_title.center(0)

    print(colour.black + "-" * 150 + style.end)
    print(colour.black + "-" * 150 + style.end)
    print(" ")
    print(colour.black + "-" * 50 + style.end, colour.yellow + style.bold + ARS_full_title.upper() + style.end,
          colour.black + "-" * 58 + style.end)
    print(" ")
    print(colour.black + ("-" * 75).center(150) + style.end)
    print(" ")
    print(style.bold + colour.cyan + AMG_full_title.upper() + style.end)
    print(" ")
    print(colour.black + "-" * 150 + style.end)
    print(colour.black + "-" * 150 + style.end)
    print(" ")
    print(" ")


"""Login to access system"""


def login_title_message():
    login_outer_title = "U S E R    L O G I N".center(143)
    print(" ")
    print(style.bold + colour.green + login_outer_title.upper() + "       " + style.end)
    print('\n')
    print(colour.black + "-" * 150 + style.end)
    print(" ")
    print(" ")


def import_user_information():
    file = open('user.txt', 'r')
    username = []
    password = []
    for elements in file:
        x = elements.strip()
        n = x.split(',')
        username.append(n[0]), password.append(n[1])
    file.close()
    return username, password


def login_registered_users():
    print(f'{colour.blue + timenow().center(143) + style.end}')
    print(" ")
    print(" ")
    menu_login_title_small = "Log In"
    print(" ")
    print('* ' * 5,
          f'\t\t\t\t\t\t\t\t\t\t\t{"                " + menu_login_title_small + "           "}\t\t\t\t\t\t\t\t\t'
          f'\t\t\t\t   ', ' *' * 5)
    print(" ")
    print(" ")
    print(" ")

    userinformation = import_user_information()  # import user information text file
    retry_time = 3  # time
    username = input("Username: ")

    if username in userinformation[0]:
        user_index = userinformation[0].index(username)
        while retry_time > 0:
            print(" ")
            password = input('Password: ')
            if password == userinformation[1][user_index]:
                print("\n")
                print(
                    f' \t\t\t\t\t\t\t\t\t\t{colour.blue + "> > > > >   // You have successfully login to AMG! //   < < < < <" + style.end}')

                time.sleep(1.55)

                print(" ")
                print(" ")
                print(f'{colour.blue} Greetings and welcome back to AMG! {colour.red + username + style.end}. '
                      f'{style.end}'.center(162))
                print(" ")
                print(" ")

                user_id.append(user_index)
                append_user_information()
                time.sleep(2.25)
                menu_choose_option()

            else:
                retry_time -= 1
                if retry_time > 0:
                    print(" ")
                    print(f'\nYou fail to login, you are now left with {retry_time} time to attempt.')
                    time.sleep(2)

                else:
                    print(" ")
                    print('\nIncorrect password, please login again!\n'), login_registered_users()
                    time.sleep(2)

    else:
        print(" ")

        print('There is no such user found in our database! Please try login or register again.')
        print('\n')
        time.sleep(1.35)

        welcome_message()
        login_title_message()
        login_registered_users()


def append_user_information():
    login_user_detail.clear()
    f = open('user.txt', 'r')
    user = []
    for e in f:
        x = e.strip()
        n = x.split(',')
        user.append(n)
    f.close()
    for t in user[user_id[0]]:
        login_user_detail.append(t)


def show_user_header():
    u = login_user_detail[0]
    print(' ')
    print(f'{colour.blue + timenow() + style.end}')
    print(' ')
    print(colour.black, '-' * 148, style.end)
    print(f'\t\t\t\t\t\t\t\t\t{colour.hblue} {colour.white}Air Malaysia Group (AMG){style.end}\t\t\t\t\t\t\t\t\t\t\t'
          f'{colour.red + style.bold + u + style.end}{" " * (10 - len(u)) + style.end}')
    print(colour.black, '-' * 148, style.end)


def menu_choose_option():
    login_inner_title = "Welcome to your AMG user account! Please surf around!"
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(f"{style.bold + login_inner_title.center(143) + style.end}")
    print(" ")
    print("-" * 150)
    print("-" * 150)
    show_user_header()
    print(" ")
    print(colour.yellow + style.underline + 'Main Menu' + style.end)
    print(" ")

    option = input("Choose one option below to continue:"
                   '\n'
                   '\n*************************************'
                   '\n'
                   '\n[1] Show user profile.'
                   '\n[2] Update user profile.'
                   '\n[3] Add flight bookings.'
                   '\n[4] View flight bookings.'
                   '\n[5] Log out'
                   '\n'
                   '\n*************************************'
                   '\n'
                   '\nOption: ')

    print("")
    if option == '1':
        display_user_information()

    elif option == '2':
        update_user_information()

    elif option == '3':
        add_flight_booking()

    elif option == '4':
        my_booking()

    elif option == '5':
        print("Logging out..")
        print(" ")
        print(" ")
        logout_account()

    elif option == '6':
        print("test")
        # total_ticket_customer()

    else:
        print("Invalid input! Please pick numbers from 1 to 5 to proceed.")
        menu_choose_option()


def display_user_information():
    print(" ")
    show_user_header(), print(colour.yellow + style.underline + "My profile" + style.end)
    print(" ")
    print("*" * 45)

    r = ['Username', 'Password', 'Full Name', 'First Name', 'Last Name', 'Gender', 'Date of Birth', 'Contact No.',
         'Citizenship', 'TDD', 'Emergency Contact', 'Saved Card', 'Saved Card Number', 'Valid Date Through', 'CVV']

    print(" ")
    for e in range(len(r)):
        print(f'{r[e]}: {login_user_detail[e]}')
    print(" ")
    print("*" * 45)
    print(" ")

    x = input('\n[1] Modify my user profile'
              '\n[2] Back to main menu'
              '\n'
              '\nOption: ')

    if x == '1':
        print(" ")
        update_user_information()

    elif x == '2':
        print(" ")
        menu_choose_option()

    else:
        print(" ")
        print(" ")
        print("Your input numbers are invalid for the option, please try again. ")
        print(" ")
        time.sleep(2.5)
        display_user_information()


# START FROM HERE FLOWCHART
def add_flight_booking():
    show_user_header()
    print(" ")
    print(colour.yellow + style.underline + 'Add flight bookings' + style.end)
    print(" ")
    time.sleep(1)
    flight()


def import_booking():
    f = open('user_booking.txt', 'r')

    book_list = []

    for e in f:
        x = e.strip()
        n = x.split(',')
        book_list.append(n)
    f.close()

    return book_list


def my_booking():
    print(" ")
    show_user_header()
    print(" ")
    print(f'{colour.yellow + style.underline}My booking{style.end}')
    print("\n")

    imf = import_flight()
    ib = import_booking()

    for e in range(len(ib)):
        if str(user_id[0]) in ib[e][0]:
            ind = int((ib[e][1]))
            p = imf[ind]
            print('>' * 90)
            print(" ")
            if p[0] == '1':
                print("Ticket type: One Way Ticket")
                print("")
            elif p[0] == '2':
                print("Ticket type: Return Ticket")
                print("")
            else:
                print("Incorrect ticket number for ticket type!")
                print("")
            print(f'{p[4]}\t\t\t\t  {p[7]}  \t\t{p[9]}\tTime Duration\t\t{int(ib[e][2])} Ticket(s)')
            print(f'{p[5] + " " * (11 - len(p[4]))}\t  {p[6]}\t --->  '
                  f'{"  " + p[8]}\t\t {"  "}{p[12] + " " * (7 - len(p[12]))}\t\t\tTotal: RM{int(p[13]) * int(ib[e][2])}'
                  f'\n'
                  f'\nDeparture date: {p[10]}'
                  f'\nReturn date: {p[11]}')

            print(" ")
            print('>' * 90)
            print("\n")
    print(" ")
    print(f"{style.bold}Do you still want to book more flight or exit to the main menu?: {style.end} ")
    print(" ")
    x = input('\n[1] Add new flight booking.'
              '\n'
              '\n[2] Back to main menu.'
              '\n'
              '\nOption: ')

    if x == '1':
        show_user_header()
        flight()

    elif x == '2':
        menu_choose_option()

    else:
        my_booking()


def import_flight():
    f = open('flight.txt', 'r')
    flight_list = []
    for e in f:
        x = e.strip()
        n = x.split(',')
        flight_list.append(n)
    f.close()
    return flight_list


def flight_schedule(f, i, ppl):
    print(" ")
    print(f"{style.bold}Below are the current air flight schedules, please choose one to continue. "
          f"(Press number according to{style.end}"
          f"{style.bold} your chosen flight schedule.) {style.end} ")
    print("\n")
    print(colour.blue + timenow() + style.end)
    print("\n")
    print('\t\t\t\t\t\t\t\t\t\t    |  Departure  |    Arrive   |')
    print(
        'Schedule No. | Flight Company | Flight No. |  From  | Time  |  To  |  Time  |  Departure Date  |  '
        'Return Date  |  Time Duration  |  Price  |')
    print(" ")
    print('/' * 150, end='')
    print(" ")
    temp_no = 1
    for r in i:
        o = f[r]
        print(f'\n \t{temp_no}', end='\t\t\t\t') if temp_no < 15 else print(f'\n\t\t{temp_no}', end='\t\t\t\t')
        print(o[4] + ' ' * (14 - len(o[4])), end='')
        print(o[5] + ' ' * (12 - len(o[5])), end='')
        print(o[6] + ' ' * (8 - len(o[6])), end='')
        print(o[7] + ' ' * (9 - len(o[7])), end='')
        print(o[8] + ' ' * (7 - len(o[8])), end='')
        print(o[9] + ' ' * (11 - len(o[9])), end='')
        print(o[10] + ' ' * (18 - len(o[10])), end='')
        print(o[11] + ' ' * (18 - len(o[11])), end='')
        print(o[12] + ' ' * (15 - len(o[12])), end='')
        print(f'RM{int(o[13]) * ppl}', end='')
        temp_no += 1
    print('\n')
    print('/' * 150)
    return i


def flight():
    fli = import_flight()
    f, t, year, month, day, = '', '', '', '', ''

    ticket = input('\nPlease choose your ticket:'
                   '\n'
                   '\n[1] One Way Ticket'
                   '\n[2] Return Ticket'
                   '\n'
                   '\n[3] Back to main menu.'
                   '\n'
                   '\nOption: ')

    if ticket == '':
        ticket = '1'

    if ticket == '3':
        menu_choose_option()

    ticket_people = input('\nPlease enter the amount of ticket to purchase (how many people)'
                          '\n'
                          '\n[x] Back to main menu.'
                          '\n'
                          '\nHow many?: ')

    print(" ")

    if ticket_people == '':
        ticket_people = 1
    ticket_people = int(ticket_people)
    if ticket_people == 'x':
        menu_choose_option()

    temp_id = []
    for r in range(len(fli)):
        o = fli[r]
        if ticket in o[0]:
            if year in o[1]:
                if month in o[2]:
                    if day in o[3]:
                        if f in o[5]:
                            if t in o[7]:
                                index_order = fli.index(o)
                                temp_id.append(index_order)

    tem_id = flight_schedule(fli, temp_id, ticket_people)
    book(tem_id, fli, ticket_people)


def book(a, b, c):
    bo = input(f'\nPlease enter {style.bold}schedule no.{style.end} that you want to purchase: ')
    if bo == '':
        flight()
    bo = int(bo)
    p = b[a[bo - 1]]

    print('>' * 90)
    if p[0] == '1':
        print("Ticket type: One Way Ticket")
        print("")
    elif p[0] == '2':
        print("Ticket type: Return Ticket")
        print("")
    else:
        print("Incorrect ticket number for ticket type!")
        print("")
    print(f'{p[4]}\t\t\t\t  {p[7]}  \t\t{p[9]}\tTime Duration\t\t{c} Ticket(s)')
    print(f'{p[5] + " " * (11 - len(p[4]))}\t  {p[6]} \t--->  '
          f'{"  " + p[8]}\t\t {"  "}{p[12] + " " * (7 - len(p[12]))}\t\t\tTotal: RM{int(p[13]) * c}'
          f'\n'
          f'\nDeparture date: {p[10]}'
          f'\nReturn date: {p[11]}')
    print('>' * 90)

    ticketconfirmation = input('\nYou sure to buy the tickets based on your selection?(Y/N): '
                               '\n'
                               '\nOption: ')

    inputdetails_temp = []
    im_temp = []

    if ticketconfirmation.lower() == 'y':
        inputdetails_temp.append(str(a[bo - 1])), inputdetails_temp.append(str(c))
        print("\nYour payment has been processing.. Please hold on..")
        im_temp.append(inputdetails_temp), export_to_book_file(im_temp)
        print("\n")

        transfer_process(
            'View flight booking\'s'), my_booking()
        # payment()

    else:
        print("Back to the buy flight ticket menu.")
        flight()


def export_to_book_file(a):
    f = open('user_booking.txt', 'a')
    for e in range(len(a)):
        f.write('')
        f.write(str(user_id[0])), f.write(',')
        for n in range(len(a[e])):
            f.write(a[e][n]), f.write(',')
        f.write('\n')
    f.close()


def export_user_file(a):
    file = open('user.txt', 'w')

    for elements in range(len(a)):
        for n in range(len(a[elements])):
            file.write(a[elements][n])
            file.write(',') \
                if len(a[elements]) > 1 \
                else file.write(a[elements][n])
        file.write('\n')
    file.close()


def import_user_file():
    file = open('user.txt', 'r')

    user = []

    for elements in file:
        x = elements.strip()
        n = x.split(',')
        user.append(n)
    file.close()

    return user


def update_user_information():
    show_user_header()
    print(" ")
    print(colour.yellow + style.underline + 'Edit my user profile' + style.end)
    print(" ")
    print("Please follow the required user details below:")
    print(" ")
    print("*" * 45)
    print(" ")

    importuserfile = import_user_file()

    input_details = []

    details = ['Username', 'Password', 'Full Name', 'First Name', 'Last Name', 'Gender', 'Date of Birth', 'Contact No.',
               'Citizenship', 'TDD', 'Emergency Contact', 'Saved Card', 'Saved Card Number', 'Valid Date Through',
               'CVV']

    for elements in range(len(details)):
        newdetails = input(f'{details[elements]}: ')
        input_details.append(newdetails)

    print('\n')

    confirmation = input('Are you sure to change your user details?: '
                         '\n'
                         '\nYes or no? (Please pick "Y" or "N")'
                         '\n'
                         '\nOption: ')

    if confirmation == 'y' or 'Y':  # confirmation.lower()
        print(" ")
        print("Your user details are now changing..")
        importuserfile[user_id[0]] = input_details
        export_user_file(importuserfile)
        append_user_information()
        modifying_process('your user account\'s')
        menu_choose_option()

    elif confirmation == 'n' or 'N':
        print(" ")
        print("Your user details remain unchanged, please input again to update user details. ")
        display_user_information()
        print(" ")
        time.sleep(2)

    else:
        display_user_information()
        time.sleep(2)

    print(" ")
    print("*" * 45)
    print(" ")


def transfer_process(a):
    ppercentage = 15  # process percentage.
    print(f'\nWaiting for the process...'
          f'\n'
          f'\nTransferring payment now...{ppercentage}%')

    for elements in range(3):
        time.sleep(4) if elements > 3 else time.sleep(0.4)
        # if elements > 1:
        # else:
        #     time.sleep(0.4)
        ppercentage += 17
        print(f'\nYour payment are being transferred at the moment...{ppercentage}%')

    time.sleep(3)

    print('\nYour payment has transferred successfully!!'
          '\n'
          f'\nNow you are returning to \033[1;32m{a}\033[0;0m main menu. ')
    print("\n")

    time.sleep(5)


def modifying_process(a):
    ppercentage = 15  # process percentage.
    print(f'\nWaiting for the process...'
          f'\n'
          f'\nSaving now...{ppercentage}%')

    time.sleep(3)

    print('\nUpdating successfully!!'
          '\n'
          f'\nNow you are returning to \033[1;32m{a}\033[0;0m main menu. ')
    print("\n")

    time.sleep(5)


def logout_account():
    user = login_user_detail[0]
    show_user_header()
    print("\n")
    time.sleep(0.25)
    print(style.bold + f'Thank you for visiting us, please come back again soon! {user}!'
                       '\n'
                       '\nHope you have a pleasant day!! - from Air Malaysia Group' + style.end)
    time.sleep(3.5)
    print('\n' * 10)
    amg_main_page()


login_user_detail = []
user_id = []


# 3............................................Functionalities of Admin.................................................
# 3.1. Login to access system.

# AMG admin login page title

def admin_login_title():
    title = "Welcome to 'AMG' Admin Login Page"
    full_title = title.center(150)
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(colour.hblack + colour.white + style.bold + full_title.upper() + style.end)
    print(" ")
    print("-" * 150)
    print("-" * 150)
    print(colour.blue)
    print(e.strftime("%a, %b %d, %H:%M:%S, %Y"))
    print(style.end)
    print(" ")
    print(" ")


time.sleep(0.25)


# Login to Admin access system

def admin_login(admin_name, password):
    success = False
    read_admin_detail = open("admin_detail.txt", "r")
    print("")
    for e in read_admin_detail:
        a, b = e.split(",")
        b = b.strip()
        if a == admin_name and b == password:
            success = True
            break
    read_admin_detail.close()

    if success:
        print(colour.blue)
        time.sleep(0.25)
        print(style.end)
        print("Logging.")
        time.sleep(0.25)
        print("Logging..")
        time.sleep(0.25)
        print("Logging...")
        time.sleep(0.25)
        print(" ")
        print(
            " " * 45 + colour.white + style.bold + "/// You have successfully login to Your AMG Admin Account! ///" + style.end)
        print(" ")
        print(" " * 68 + colour.white + style.bold + "Hi,", admin_name + style.end)
        print(("-" * 75).center(150))
        time.sleep(0.25)
        admin_option()

    else:
        print("-" * 150)
        print(colour.red + style.bold + "-" * 56 + "Incorrect Your Admin name or password" + "-" * 57 + style.end)
        print("-" * 150)
        print(" ")
        time.sleep(0.25)
        admin_login_access()


# Input the admin name
def admin_login_access():
    admin_name = input(colour.white + "Enter your admin name: ")
    password = input("Enter your password: " + style.end)
    print(" ")
    admin_login(admin_name, password)


# admin_login_access()

# Menu of Admin Page

def admin_option():
    option_of_admin = "Welcome to Admin Menu"
    full_title = option_of_admin.center(150)
    print(" ")
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(colour.hblack + colour.white + style.bold + full_title.upper() + style.end)
    print(" ")
    print(("-" * 75).center(150))
    print("-" * 150)
    print(colour.blue)
    print(e.strftime("%a, %b %d, %H:%M:%S, %Y"))
    print(style.end)
    print(" ")
    time.sleep(0.4)
    print(colour.white)
    option = input("Please select the following option to continue:"
                   '\n------------------------------------------------'
                   '\n[1] Add flight schedules.'
                   '\n[2] Modify flight schedules.'
                   '\n[3] Display all record.'
                   '\n[4] Log out'
                   '\n'
                   '\nOption: ')
    print(style.end)

    if option == '1':
        add_flight_schedules()

    elif option == '2':
        modify_flight_schedules()

    elif option == '3':
        display_all_option()

    elif option == '4':
        time.sleep(0.25)
        print("Exiting.")
        time.sleep(0.25)
        print("Exiting..")
        time.sleep(0.25)
        print("Exiting...")
        print("Successfully Logged Out!")
        print(" ")
        amg_main_page()

    else:
        time.sleep(0.3)
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 4 to proceed. <<<" + style.end)
        admin_option()


# 3.2.	Add flight schedules (flight number, from, to, date & time (departure & return), price, etc...)
# Flight_num, From, To, Departure_time, Arrive_time, Date_departure, Date_return

def add_flight_schedules():
    time.sleep(0.5)
    add_schedules_title = "Add the new flight schedules in the following"
    add_flight_title = add_schedules_title.center(150)
    print(" ")
    print("-" * 150)
    print("-" * 150)
    print(" ")
    print(colour.hblack + colour.white + style.bold + add_flight_title.upper(), style.end)
    print(" ")
    print(("-" * 75).center(150))
    print("-" * 150)
    print(" ")

    # admin input the flight schedules
    time.sleep(0.25)
    print("...")
    print(colour.white)
    airline_num = input("Enter a new Airline number     : ")
    departure = input("Enter a departure country      : ")
    departure_time = input("Enter the departure time       : ")
    departure_date = input("Enter the departure date       : ")
    arrive = input("Enter a arrive country         : ")
    arrive_time = input("Enter the arrive time          : ")
    journey_duration = input("Enter the journey duration     : ")
    return_date = input("Enter the return date          : ")
    price_of_ticket = input("Enter the price of ticket      : ")

    flight = []
    flight.append(airline_num)
    flight.append(departure)
    flight.append(departure_time)
    flight.append(departure_date)
    flight.append(arrive)
    flight.append(arrive_time)
    flight.append(journey_duration)
    flight.append(return_date)
    flight.append(price_of_ticket)

    print(style.end)
    print(" ")
    time.sleep(0.1)
    print("Storing into the Flight Schedule text file...")
    time.sleep(1.0)
    print(" ")
    print(colour.dark_cyan + "*" * 102 + style.end)
    print(colour.white + "Flight Schedule: ", flight, style.end)
    print(colour.dark_cyan + "*" * 102 + style.end)
    # convent list to string
    file = open("flight_schedule.txt", "a")
    for ele in flight:  # all element in flight
        file.write(ele + ";")
    file.write("\n")
    file.close()

    print(" ")
    time.sleep(0.2)
    print(colour.white)
    option = input("Please select the following option to continue:"
                   '\n-----------------------------------------------'
                   '\n[1] Continue to add new flight schedule.'
                   '\n[2] Back to Admin Menu.'
                   '\n'
                   '\n> Option: ')
    print(style.end)

    if option == '1':
        add_flight_schedules()

    elif option == '2':
        admin_option()

    else:
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 2 to proceed. <<<" + style.end)
        add_flight_schedules()


# 3.3. Modify flight schedules

def modify_flight_schedules():
    with open('flight_schedule.txt', 'r') as flight_file:
        data = flight_file.read()
        # print("Raw data:", data)
        schedule = data.splitlines()
        time.sleep(0.3)
        print(" ")
        # display the flight schedules to given admin see
        print("=" * 90)
        print(colour.white, style.bold, "...", "\t\t\t\t\t\t\t", "AMG Flight Schedules", "\t\t\t\t\t\t\t", "...",
              style.end)
        print("=" * 90)
        print(">>>")
        for ele in schedule:
            # schedule = ele.split(";")
            print(colour.white + "ID:", schedule.index(ele) + 1, "\t" + colour.red + "|" + style.end,
                  "\tFlight Schedule:\t", ele + style.end)
            print(colour.blue + "-" * 90 + style.end)
        print(" ")

        # admin input the ID modify the flight schedules
        print("...")
        position = int(input(colour.white + "> Enter the ID to modify the Flight Schedule: " + style.end))

        print(" ")
        time.sleep(0.2)
        print(colour.dark_cyan + "*" * 105 + style.end)
        print(colour.white + "This is the Flight Schedule you will modify: ", schedule[position - 1] + style.end)
        print(colour.dark_cyan + "*" * 105 + style.end)
        # listname[index]

        new_schedule = input(colour.white + "\n> Enter New Flight Schedule to modify: " + style.end)
        # print("-" * 100)
        print(colour.red + "* " + style.end + colour.white + "You will change", schedule[(position - 1)], "to",
              new_schedule, "\n" + style.end)
        print("-" * 150)
        schedule[(position - 1)] = new_schedule
        # schedule[2] = "new item"

        # # Display all Flight Schedules with ID

        # Find in string
        stringvar = schedule[(position - 1)]
        findNreplace = stringvar.replace("Old Flight Schedule", "New Flight Schedule")
        time.sleep(0.2)
        print(colour.white + "Changing Old Flight Schedule to New Flight Schedule:", findNreplace + style.end)
        time.sleep(0.2)
        print("Changing.")
        time.sleep(0.2)
        print("Changing..")
        time.sleep(0.2)
        print("Changing...")
        print(" ")
        print(" ")
        print("=" * 90)
        print(colour.white, style.bold, "...", "\t\t\t\t\t\t", "Updated AMG Flight Schedules", "\t\t\t\t\t\t", "...",
              style.end)
        print("=" * 90)
        print(">>>")

        schedule[(position - 1)] = findNreplace
        for ele in schedule:
            print("ID:", schedule.index(ele) + 1, "\t" + colour.red + "|" + style.end, "\tFlight Schedule:\t", ele)
            print(colour.blue + "-" * 90 + style.end)

        # Update File
        flight_file = open("flight_schedule.txt", "w")
        for item in schedule:
            flight_file.write(item + "\n")
        flight_file.close()

        print(colour.white)
        mod_option = input("Please select the following option to continue:"
                           "\n-----------------------------------------------"
                           "\n[1] Continue to modify flight schedules."
                           "\n[2] Back to Admin Menu."
                           "\n"
                           "\n> Option: ")
        print(style.end)

        if mod_option == '1':
            modify_flight_schedules()

        elif mod_option == '2':
            admin_option()

        else:
            print(
                "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 2 to proceed. <<<" + style.end)
            modify_flight_schedules()


# 3.4.	Display all records of

def display_all_option():
    time.sleep(0.6)
    option_of_record = "Display All Record"
    record_title = option_of_record.center(150)
    print(" ")
    print("-" * 150)
    print(" ")
    print(colour.hblack + colour.white + style.bold + record_title.upper() + style.end)
    print(("-" * 75).center(150))
    print("-" * 150)
    print(" ")
    time.sleep(0.25)
    print(colour.white)
    option = input("Please select the following option to continue:"
                   '\n------------------------------------------------'
                   '\n[1] Flight schedules by flight number.'
                   '\n[2] Flight booked by customer.'
                   '\n[3] Total tickets sold.'
                   '\n[4] Back to Admin Menu.'
                   '\n'
                   '\nOption: ')
    print(style.end)

    if option == '1':
        flight_schedules_by_fligt_number()

    elif option == '2':
        flight_booked_by_customer()

    elif option == '3':
        total_ticket_customer()

    elif option == '4':
        admin_option()

    else:
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 4 to proceed. <<<" + style.end)
        display_all_option()


# Search the flight number to display flight schedules

def flight_schedules_by_fligt_number():
    time.sleep(0.3)
    search_record = "Display flight schedules by searching flight number"
    record_title = search_record.center(150)
    print(" ")
    print("-" * 150)
    print(" ")
    print(colour.hblack + colour.white + style.bold + record_title.upper() + style.end)
    print(("-" * 75).center(150))
    print("-" * 150)
    print(" ")
    print(" ")
    time.sleep(0.5)
    print(">>>")
    print(colour.white)
    search = input("Enter Airline Number to search a Flight Schedule: AM")  # admin input flight number to searching
    print(style.end)
    f = open("flight_schedule.txt", "r")
    content = f.read()
    content_list_schedule = content.splitlines()
    f.close()
    time.sleep(0.25)
    print("Searching...")
    time.sleep(2.5)
    for flight_sched in content_list_schedule:
        detail = flight_sched.split(";")
        if search in detail[0]:
            print(colour.blue + "~" * 46 + style.end)
            print(colour.white)
            print("Airline Number       :", detail[0])  # Display flight schedule in list
            print("Departure Country    :", detail[1])
            print("Departure Time       :", detail[2])
            print("Departure Date       :", detail[3])
            print("Arrive Country       :", detail[4])
            print("Arrive Time          :", detail[5])
            print("Journey Duration     :", detail[6])
            print("Return Date          :", detail[7])
            print("Price of Ticket      :", detail[8])
            print(style.end)
            print(colour.blue + "~" * 46 + style.end)
            print(" ")

            time.sleep(0.25)
            print(colour.white)
    flight_option = input("Please select the following option to continue:"
                          '\n------------------------------------------------'
                          '\n[1] Continue to search flight schedule.'
                          '\n[2] Back to previous menu.'
                          '\n[3] Back to Admin Menu.'
                          '\n'
                          '\n> Option: ')
    print(style.end)

    if flight_option == '1':
        flight_schedules_by_fligt_number()

    elif flight_option == '2':
        display_all_option()

    elif flight_option == '3':
        admin_option()

    else:
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 3 to proceed. <<<" + style.end)
        flight_schedules_by_fligt_number()


# Display all the customer booking

def flight_booked_by_customer():
    print(
        colour.white + style.bold + "\t\t\t\t\t\t\t..." + style.underline + f'Record of Customer Flight Booking' + style.end + "...")
    im = import_user_file()  # import the user detail
    imf = import_flight()  # import the flight detail
    ib = import_booking()  # import the customer booking detail

    for e in range(len(ib)):  # ib is the length so 'e' can see how many flight ticket booked and loop
        ind = int(ib[e][
                      1])  # ib[e]= Line by line of thing  # ib[e][1]= 1 is the middle of each line, and the middle is the ticket id
        p = imf[
            ind]  # imf[?]  ?imf is line by line  # If imf[0] is the first row of the timetable  # imf[1] is the second line
        imt = int(ib[e][0])  # same think, but the plane ticket is exchanged for the user
        m = im[imt][0]  # same think

        time.sleep(0.3)
        print(colour.blue + '>' * 90 + style.end)
        print(colour.white)
        print(f'ID:{imt}\t\t  Name:{m} ')
        print(f'{p[4]}\t\t\t\t  {p[7]}  \t\t{p[9]}\tTime Duration\t\t{int(ib[e][2])} Ticket(s)')
        print(f'{p[5] + " " * (11 - len(p[4]))}\t  {p[6]}\t --->  '
              f'{"  " + p[8]}\t\t {"  "}{p[12] + " " * (7 - len(p[12]))}\t\t\tTotal: RM{int(p[13]) * int(ib[e][2])}'
              f'')
        print(style.end)
        print(" ")
        print(colour.blue + '>' * 90 + style.end)
        print("\n")

        time.sleep(0.25)
        print(colour.white)
    booked_option = input("Please select the following option to continue:"
                          '\n------------------------------------------------'
                          '\n[1] Continue to display the flight booked by customer.'
                          '\n[2] Back to previous menu.'
                          '\n[3] Back to Admin Menu.'
                          '\n'
                          '\n> Option: ')
    print(style.end)

    if booked_option == '1':
        flight_booked_by_customer()

    elif booked_option == '2':
        display_all_option()

    elif booked_option == '3':
        admin_option()

    else:
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 3 to proceed. <<<" + style.end)
        flight_booked_by_customer()


# Display all the calculation

def total_ticket_customer():
    time.sleep(0.3)
    imf = import_flight()
    ib = import_booking()
    x = 0
    y = 0
    for e in range(len(ib)):
        ind = int(ib[e][1])
        p = imf[ind]
        t = int(p[13]) * int(ib[e][2])
        x = x + t
        y = y + int(ib[e][2])
    print(colour.white + style.bold + "\t\t\t\t\t..." + style.underline + "Calculation of Flight" + style.end + "...")
    time.sleep(0.2)
    print("Calculating...")
    time.sleep(1.5)
    print(colour.blue + "/" * 82 + style.end)
    print(colour.white)
    print("Total number of customers who have purchased airline flight tickets  :", len(ib))
    print("Total ticket purchased by customer                                   :", y)
    print(f'Total price of tickets sold                                          : RM{x}')
    print(style.end)
    print(" ")
    print(colour.blue + "/" * 82 + style.end)
    print(" ")

    print(colour.white)
    total_option = input("Please select the following option to continue:"
                         '\n------------------------------------------------'
                         '\n[1] Continue to display the total ticket sold.'
                         '\n[2] Back to previous menu.'
                         '\n[3] Back to Admin Menu.'
                         '\n'
                         '\n> Option: ')
    print(style.end)

    if total_option == '1':
        total_ticket_customer()

    elif total_option == '2':
        display_all_option()

    elif total_option == '3':
        admin_option()

    else:
        print(
            "\t" * 11 + colour.red + style.bold + ">>> Invalid input! Please pick numbers from 1 to 3 to proceed. <<<" + style.end)
        total_ticket_customer()


amg_main_page()
