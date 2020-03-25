######################
# Mail Room Part One #
######################


###########################################################################################
# Data Sturcture for Mail Room
# 1. For the whole records are stored in a list so that we can keep adding now one to it.
# 2. For each record, we use tuple to make sure that a single record only can 
#    contain two items: "name" and "donation amount".
# 3. For donor name, we use string.
# 4. For donation amount, we use a list so that each donor can donate more than time. 
###########################################################################################
donors_db = [('Adan William',[100.75,1200,3200.45]),
             ('Peter Chiykowski',[25.25,4340.25]),
             ('Sara Gogo',[650]),
             ('Jason Zhang',[150.00,35.50,80.75]),
             ('Zooe Bezos',[10,20])]


##################
# prompt the three options for user 
##################
def ori_prompt():
    print("Please choose from the following three options: ")
    input_str = input("1.Send_ThankYouLetter 2.Create_Report,3.Quit : ")
    # remove the leading and tailing whitespace
    input_str.strip() 
    return input_str

##################
# prompt the user to input full name of the donor
##################
def fullname_prompt():
    input_str = input("Please input donor's full name or input 'list' or input 'quit' to quit : ")
    # remove the leading and tailing whitespace
    input_str.strip() 
    if input_str.isdigit():
        print("Input is a number not a name.")
        return -1
    elif input_str == 'quit':
       quit_program() 
    return input_str


##################
# prompt the user to input a donation amount 
##################
def amount_prompt():
    input_str = input("Please input the donation amount  or input 'quit' to quit : ")
    # remove the leading and tailing whitespace
    input_str.strip() 
    if input_str == 'quit':
       quit_program() 
    # Convert the amount into a number
    try:
           input_str = float(input_str)
    except ValueError:
           print("Please input a number for donation amount. Thank you!")
           return -1 

    if  float(input_str)>=0:
        input_amount = float(input_str)
        return input_amount 
    else:# input is not a number we need to ask user to input number again.
        print("Plese input a positive number for donation amount. Thank you! ")
        return -1



##################
# find the name from donors_db 
##################
def found_name(my_name):
    count = 0
    for rowindex, row in enumerate(donors_db):
        if row[0] == my_name:
            return rowindex 
    return -1 

##################
# add the amount to the existing donor on the donors_db 
##################
def add_amount(amount,r_index):
    tmp_amount = [amount]
    donors_db[r_index][1].append(amount)
    print(f"3. Updated donor amount: {donors_db[r_index]}")


##################
# add the new orcorder to the donors_db
##################
def add_newrecord(d_name,amount):
    # use tuple to make sure that a single record only can 
    # contain two items: "name" and "donation amount"
    new_record = (d_name,[amount])
    donors_db.append(new_record) 
    #print(f"1. Updated record {donors_db}")


##################
# print the thank you email 
##################
def thankyou_letter(d_name,amount):
    print(f"Dear {d_name}: ") 
    print(f"     Thank you for your generous donation (${amount}) to us.") 
    print("     You have a wonderful day!") 





#################################
# define send_thankyou() Option #
#################################
def send_thankyou(d_name):
    # if user input 'list' we will list all the donor's name and ask full name again.
    while d_name == 'list':
        print("The donor list: ")
        for i in donors_db:
           print(f"{i[0]}   ",end ="")
        print("\n")

        d_name = fullname_prompt() 
    if d_name == -1 :
        return
    # for existing donor, add the donated amount to the list
    row_index = found_name(d_name)
    if row_index != -1:
        amount = amount_prompt()
        if amount != -1:
            add_amount(amount,row_index)
            # print thankyou_letter()
            thankyou_letter(d_name,amount)
    # for new donor,
    # add the new donor name and donated amount to donors_db.
    else:
        amount = amount_prompt()
        if amount != -1:
            add_newrecord(d_name,amount)
            # print thankyou_letter()
            thankyou_letter(d_name,amount)




#################################
# define reate_report() Option #
#################################
def create_report():
    col_1 = 'Donor Name'
    col_2 = 'Total Amount'
    col_3 = 'Num Gifts'
    col_4 = 'Average Amount'
    formater_title = '{:^20s}|{:^15s}|{:^15s}|{:^20s}'
    # scientific notation output
    #formater_content = '{:<20s} ${:>14,.2e}{:>15d}  ${:>17,.2e}'

    formater_content = '{:<20s} ${:>14,.2f}{:>15d}  ${:>17,.2f}'

    # print the Title of the report
    print(formater_title.format(col_1,col_2,col_3,col_4))
    print('-'*71)

    # print the content of the report
    for i in donors_db:
        tot_amount = 0
        avg_amount = 0
        name = i[0]
        count = len(i[1])
        for j in i[1]:
            tot_amount = tot_amount + j 
        avg_amount = tot_amount / count
        # print out current row data
        print(formater_content.format(name,tot_amount,count,avg_amount))

    print("\n")








#################################
# define Quit_Program()  Option #
#################################
def quit_program():
    print("Bye!")
    exit()






#################################
# define main() function        #
#################################
def main():
    #Forever loop for letting user choose one of three options.
    while True:
        input_str = ori_prompt()
        if input_str == '1':
            d_name = fullname_prompt()
            if d_name != -1:
                send_thankyou(d_name)
        elif input_str == '2':
            create_report()

        elif input_str == '3':
            quit_program()
        else:
            print("Please input a vaild option.")




# put main interaction into the __main__ block 
if __name__ == '__main__':
# calling the main() fuction
    main()
