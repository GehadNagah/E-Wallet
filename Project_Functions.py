from datetime import datetime , date
def sign_up(username, password):
    username_counter=0
    password_counter=0
    if len(username)>=6 and len(username) <= 15:
        username_counter=username_counter+1
    if username[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        username_counter=username_counter+1
    for j in range(0,len(username)):
        if username[j] in '0123456789':
            username_counter=username_counter+1
        elif username[j]in'@#$%^&*!':
            username_counter=username_counter+1
        elif username[j] in 'abcdefghijklmnopqurtuvwxyz':
            username_counter=username_counter+1
    if username_counter>=5:
        print('ok, user')
    else:
        print('invalusername')
        return -1
    for i in range(0,len(password)):
        if password[i] in 'abcdefghijklmnopqurtuvwxyz':
            password_counter=password_counter+1
        elif password[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            password_counter=password_counter+1
        elif password[i]in '0123456789':
            password_counter=password_counter+1
        elif password[i] in '@#$':
            password_counter=password_counter+1
        elif len(password)>=6 and len(password)<=20:
            password_counter=password_counter+1
    if password_counter>=5:
        print ('good job')
    else:
        print('Invalid pass please try again')
        return -1

    if password_counter>=5 and username_counter>=3:
        print('Good job:) Accepted User Name & Password!')
        # file = open('pass&usernamefile.txt', 'r')
        # file_content=file.readlines()
        # length=len(file_content)
        filewrite=open('test2.txt', 'a')
        filewrite.write('%-20s %-20s %-20s' % (username,password, '0'))
        filewrite.close()
    else:
        print('Error Invalid Username or passward')
        return -1
    return 1

def check_validity(username):
    c=0
    file = open('test2.txt','r')
    file_content=file.readlines()#we, now ,have, an, array with elements of each row
    length=len(file_content)
    array_of_usernames=[]
    array_of_passwords=[]
    for i in range(0, length):
        col_1=file_content[i].split()#here we split each element at space and take the first, element, as, the, username
        usernames_only=col_1[0]#say, that, the, first, col, 's, usernames,
        passwords_only=col_1[1]#say, that, the, 2nd, col, 's, pass,
        array_of_usernames.append(usernames_only)#now, we, have, an, array, with, usernames, only
        array_of_passwords.append(passwords_only)#now, we, have, an, array, with, pass, only
    # for j in range(0, len(array_of_usernames)):# we will move along the array of usernames to check whether the entered username is in the array or not
    #     if array_of_usernames[j]==username:
    #         c=c+1
    #     if c==1:#when, c, =1, means, that, we ,find, the, username, in, the, array, so, we, must, get, the, index, where, we, found ,it, and, print, arrayofpass, of ,this, index
        if username in array_of_usernames:
            j=array_of_usernames.index(username)
            return j, array_of_passwords[j]
    return -1
def sign_in(username, password):
    x=check_validity(username)#as,the,above,return,returns,2,things,so they,are,in, an,array,that's,why,we, will,compare,by,the,x[1],as,this,'s,the,pass
    if x==-1:
        return -1
    if x[1] == password:
        pass_index=x[0]#we,will,save,this,to,be,used,later
        print('successed process :) .You are user no., ', (pass_index))
        return pass_index#this ,gives, me, its, index, in, the, array(0, 1, 2, ....etc) and will, be, used, later
    else:
        print('sorry try again!!!')
        return -1
    return 1
# note::: when, we, link, between, func, we, will, use, the ,return, above, in, order, to ,decide, whether, the, program, will, continue ,or, not, in, other ,words,
# if, we, have, this ,value, of ,the ,return, move ,to, the, next, step, else, the, pass, isnot, correct, try, again
def convert_file_to_dict():
    dict_array=[]
    a_file = open("test2.txt", 'r')
    a_file_con=a_file.readlines()
    for i in range (1,len(a_file_con)-1):
        dict={}
        col_1=a_file_con[i].split()
        name=col_1[0]
        password=col_1[1]
        amount_of_money=col_1[2]
        dict['name']=name
        dict['password']=password
        dict['money']=amount_of_money
        dict_array.append(dict)
    return dict_array


def convert_transactionfile_to_dict():
    dict_array=[]
    a_file = open("Transaction.txt", 'r')
    a_file_con=a_file.readlines()
    for i in range (1,len(a_file_con)-1):#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        dict={}
        col_1=a_file_con[i].split()
        date=col_1[0]
        Time=col_1[1]
        Process=col_1[2]
        amount_of_money=col_1[3]
        RecieverName=col_1[4]
        SenderName=col_1[5]
        dict['date']=date
        dict['Time']=Time
        dict['Process']=Process
        dict['amount_of_money']=amount_of_money
        dict['Reciever Name']=RecieverName
        dict['Sender Name']=SenderName
        dict_array.append(dict)
    return dict_array
trans_dict=convert_transactionfile_to_dict()
dict_file=convert_file_to_dict()

def Transaction_file(dict_array):
    file2=open('Transaction.txt', 'a')
    # file2.write('%-20s %-20s %-20s %-20s %-20s %-20s\n' %('Date','Time',  'Process','AmountOfMoney','RecieverName', 'SenderName' ))
    for j in range(len(dict_array)):
        for key in dict_array[j]:
            file2.write('%-20s ' %(dict_array[j][key]))
        file2.write('\n')
    file2.close()
    return file2


def Transection_fun(your_name):
    array=[]
    x=int(input('how many processes you will do?!'))
    day=date.today()
    d=day.strftime("%d/%m/%y")
    for i in range(x):
        trans_Dict={}
        p=input('what process you will do?')
        if p=='Transfer':
            amount_of_money=float(input('how much money?!'))
            # from_account_no= int(input('enter your account number'))
            # To_account_number=int(input('enter your reciever account number'))
            reciever_name=input('what is the reciever name?!')
            t=datetime.now()
            time=t.strftime("%H:%M:%S")
            trans=transfer_money_from_account_to_another(reciever_name,your_name,amount_of_money, dict_file)
            if trans != -1:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']=p
                trans_Dict['amount']=amount_of_money
                # trans_Dict['from']=from_account_no
                # trans_Dict['To']=To_account_number
                trans_Dict['Reciever Name']=reciever_name
                trans_Dict['Your Name']=your_name
                print('wohoooooooo Successful Transfer process!!')
                # print(y)
            else:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']=' Process Transfer Not Successful!!'
            array.append(trans_Dict)
        elif p=='withdraw':
            amount_of_money=float(input('how much money?!'))
            t=datetime.now()
            time=t.strftime("%H:%M:%S")
            w=withdraw(your_name, amount_of_money, dict_file)
            if w!=-1:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']=p
                trans_Dict['amount']=amount_of_money
                trans_Dict['Your Name']=your_name
                trans_Dict['Reciever Name']=your_name
                print('wohoooooooo Successful withdraw process!!')
            else:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']='Process WithDraw Not Successful!!'

            array.append(trans_Dict)

            # print(c)
        elif p=='diposte':
            amount_of_money=float(input('how much money?!'))
            t=datetime.now()
            time=t.strftime("%H:%M:%S")
            r=diposte(your_name, amount_of_money, dict_file)
            if r!=-1:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']=p
                trans_Dict['amount']=amount_of_money
                trans_Dict['Your Name']=your_name
                trans_Dict['Reciever Name']=your_name
                print('wohoooooooo Successful diposte process!!')
            else:
                trans_Dict['date']=d
                trans_Dict['Time']=time
                trans_Dict['process']='Process Diposte Not Successful!!'
            array.append(trans_Dict)

            # print(n)
        # print(trans_Dict)
    Transaction_file(array)
    return array

def update_file(dict_file):
    file=open('test2.txt', 'w')
    file.write('%-20s %-20s %-20s \n' %('UserName','Password', 'AmountOfMoney'))
    for j in range(len(dict_file)):
        for key in dict_file[j]:
            file.write('%-20s ' %(dict_file[j][key]))
        file.write('\n')
    file.close()
    return file


def transfer_money_from_account_to_another(username_to_transfer_to,my_username,  amount_of_money_to_send, dict_file):
    check_reciever=check_validity(username_to_transfer_to)
    check_sender=check_validity(my_username)
    if check_sender!=-1 and check_reciever!=-1:#this,line,to,makesure,that,the,check_validity,returns,an,array,of,j,and,array_of_passwords[j],not,-1(in,othe)
        amount_of_money_only_of_the_sender=float(dict_file[check_sender[0]-1]['money'])#minus 1 because user number 1 is user
        # no., 0 in the array of dict as we donot put the first row in the file in the array...
        amount_of_money_only_of_the_reciever=float(dict_file[check_reciever[0]-1]['money'])
        if amount_of_money_only_of_the_sender>=amount_of_money_to_send:
            dict_file[check_sender[0]-1]['money']= amount_of_money_only_of_the_sender-amount_of_money_to_send #must be updated in the file
            dict_file[check_reciever[0]-1]['money']=amount_of_money_only_of_the_reciever+amount_of_money_to_send
            update_file(dict_file)
            return dict_file
        else:
            print('Not, enough, money!')
            return -1
    else:
        print('no user found')
        return -1

def diposte(your_user_name, amount_of_money_to_diposte, dict_file):
    x=check_validity(your_user_name)
    if x!=-1:#this,line,to,makesure,that,the,check_validity,returns,an,array,of,j,and,array_of_passwords[j],not,-1(in,othe)
        your_amount_of_money=float(dict_file[x[0]-1]['money'])#minus 1 because user number 1 is user
        # no., 0 in the array of dict as we donot put the first row in the file in the array...
        # amount_of_money_only_of_the_reciever=int(dict_file[x[0]-1]['money'])
        dict_file[x[0]-1]['money']=your_amount_of_money+ amount_of_money_to_diposte#must be updated in the file
        update_file(dict_file)

        return dict_file
    else:
        print('no user found')
        return -1



def withdraw(your_username, amount_of_money_to_withdraw, dict_file):
    x=check_validity(your_username)
    if x!=-1:#this,line,to,makesure,that,the,check_validity,returns,an,array,of,j,and,array_of_passwords[j],not,-1(in,othe)
        amount_of_your_money=float(dict_file[x[0]-1]['money'])#minus 1 because user number 1 is user
        # no., 0 in the array of dict as we donot put the first row in the file in the array...
        if amount_of_your_money>=amount_of_money_to_withdraw:
            dict_file[x[0]-1]['money']=amount_of_your_money-amount_of_money_to_withdraw
            update_file(dict_file)
            return dict_file
        else:
            print('Not, enough, money!')
            return -1
    else:
        print('no user found')
        return -1

def all_Trans(username):

    print('Your Transactions Are:')
    for j in range(len(trans_dict)):
        if username==trans_dict[j]['Sender Name'] or username==trans_dict[j]['Reciever Name']:
            print(trans_dict[j])
    print('Your Total Amount Of Money is')
    for l in range(len(dict_file)+1):
        if username==dict_file[l]['name']:
            print(dict_file[l]['money'])
            return

















# username_to_transfer_to_index=x[0]
        # array_of_money=[]#used, below, to, add, money
        # #from, here, to, the, down, #, is, to, check, on, the, recieving ,side, of, the, reciever
        # file = open('pass&usernamefile.txt','r')
        # file_content=file.readlines()#we, now ,have, an, array with elements of each row
        # length=len(file_content)
        # for i in range(0, length):
        #     col_1=file_content[i].split()#here we split each element at space and take the first, element, as, the, username
        #     Recieving_part_only=col_1[3]
        #     money_part_only=col_1[2]#used, below, to, add, money
        #     array_of_money.append(money_part_only)#used, below, to, add, money
        # a=Recieving_part_only[username_to_transfer_to_index]
        # a==1
        # file_write=open('pass&usernamefile.txt', 'w')
        # file_write.write(a)
        # #######, to, here
        # amount_of_money=array_of_money[username_to_transfer_to_index]+amount_of_money#to, increase, the, money, of, the, user
        # print('You sucessfully send the money, :)')
        # file_read=open('pass&usernamefile.txt', 'r')
        # contnent=file_read.read()
        # print(contnent)








#
# def Transection_fun():
#     dict_array=[]
#     x=int(input('how many processes you will do?!'))
#     for i in range(x):
#         trans_Dict={}
#         d=(input('enter the date of today'))
#         p=input('what process you will do?')
#         amount_of_money=float(input('how much money?!'))
#         from_account_no= int(input('enter your account number'))
#         your_name=input('what is your name?!')
#         To_account_number=int(input('enter your reciever account number'))
#         reciever_name=input('what is the reciever name?!')
#         trans_Dict['date']=d
#         trans_Dict['process']=p
#         trans_Dict['amount']=amount_of_money
#         trans_Dict['from']=from_account_no
#         trans_Dict['To']=To_account_number
#         trans_Dict[' Reciever Name']=reciever_name
#         trans_Dict[' Your Name']=your_name
#         dict_array.append(trans_Dict)
#         if p=='Transfer':
#             y=transfer_money_from_account_to_another(reciever_name,from_account_no,amount_of_money, dict_file)
#             print(y)
#         elif p=='withdraw':
#             c=withdraw(reciever_name, amount_of_money, dict_file)
#             print(c)


# def transfer_money_from_account_to_another(username_to_transfer_to,no_of_account_of_sender, amount_of_money_to_send):
#     x=check_validity(username_to_transfer_to)
#     if len(x)==2:#this,line,to,makesure,that,the,check_validity,returns,an,array,of,j,and,array_of_passwords[j],not,-1(in,other,words,the,account,is,valid)
#         file = open('pass&usernamefile.txt','r')
#         file_content=file.readlines()#we, now ,have, an, array with elements of each row
#         file.close()
#         row_of_the_reciever_user=file_content[x[0]].split()
#         row_of_the_sender_user=file_content[no_of_account_of_sender].split()#here we split each element at space and take the first, element, as, the, username
#         amount_of_money_only_of_the_sender=int(row_of_the_sender_user[2])#the col of the amount of money in the sender row
#         amount_of_money_only_of_the_reciever=int(row_of_the_reciever_user[2])
#         if amount_of_money_only_of_the_sender>=amount_of_money_to_send:
#             row_of_the_sender_user[2]= str(amount_of_money_only_of_the_sender-amount_of_money_to_send) #must be updated in the file
#             row_of_the_reciever_user[2]=str(amount_of_money_only_of_the_reciever+amount_of_money_to_send)
#             r= ' '.join(row_of_the_reciever_user)
#             s= ' '.join(row_of_the_sender_user)
#             file_content[x[0]]=r
#             file_content[no_of_account_of_sender]=s
#             file_2=open('pass&usernamefile.txt','w')
#             for i in range (len(file_content)):
#                 file_2.write(file_content[i])
#             file_2.close()
#how to update these 2 new values in the file....

        # else:
        #     print('you donot have enough money!')
        #     return -1
