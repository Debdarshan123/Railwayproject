import mysql.connector 
import datetime
import random
import time

d_tt1=datetime.datetime.now()
d_tt=str(d_tt1)
d_t1=d_tt.split()
date_t=d_t1[0]

time.sleep(2)
print('\n---------------------- WELCOME TO INDIAN RAILWAYS ------------------------------')
print('***user is requested to take a soft copy of his/her train number and train name\n\n')
def password():
    con=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor9=''
    cursor9=con.cursor()
    time.sleep(2.5) 
    passwordnew=input('Enter new strong password :')
    pnew="@@".join(passwordnew)
    if len(passwordnew)>=5:
        cursor9.execute("update user_info set pass='{}' where username='{}'".format(pnew,user_id))
        con.commit()
        time.sleep(2.5) 
        print("password updated\nplease login again\n------------------")
        login()

    else:
        print('password less than 8 is not allowed. Try again \n')
        password()

def update_phone():
    con=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    time.sleep(2.5) 
    updated_phone=input('Enter 10 digit new phone')
    if len(str(updated_phone))==10:
        cursor8=con.cursor()
        
        cursor8.execute("update user_info set phone='{}' where username='{}'".format(updated_phone,user_id))
        con.commit()
        time.sleep(2.5) 
        print("phone number updated.PLEASE LOGIN AGAIN.\n------------------") 
        login()

          
    else:
        time.sleep(2.5) 
        print('phone number is invalid. Try again \n')
        update_phone()

def check(ck1,ck3,b):
    co=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor1=''
    cursor1=co.cursor()
    sqlc="select avlble_"+ck3+" from trains_detail where train_no={} ".format(ck1)
    cursor1.execute(sqlc)
    l=cursor1.fetchone()
    w=l[0]
    if b>int(w):
        time.sleep(2.5) 
        print('all desired seats are booked')
        print('extremely sorry for the incovinience')
        print('check for some other seats under enquiry section ')
        main()
    else:
        return w
    
def book():
    co=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor1=''
    cursor1=co.cursor()
    time.sleep(2.5)
    tname=input('enter train name')
    tno=input('ENTER TRAIN NO.  ')
    number=int(input('enter the number of tickets you want to book'))
    seat=input('ENTER seat type \'e.g. ac1(1st economy),ac2(2nd economy),slp(sleeper)\'')
    time.sleep(2.5)
    print('checking availability.....please wait')
    q=check(tno,seat,number)
    time.sleep(5.0)
    print('seats are available.....please proceed')
    time.sleep(2.5)
    srt_point=input('enter your starting point')
    end_point=input('enter your ending point')
    date=input('enter date of journey')
    month=input('enter month of journey')
    j_date=str(date+'-'+month+'-2022')
    for i in range(1,number+1):
        name=input('enter passenger name')
        age=int(input('enter passenger age'))
        cursor1.execute("insert into book_ticket values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(user_id, name,age,srt_point,end_point,phone,date_t,j_date,tname,tno,seat))
        co.commit()
        time.sleep(2.5)
        print(i,"ticket registered")
        sqlm="avlble_"+seat
        cursor1.execute("update trains_detail set "+sqlm+" ="+sqlm+"-1 where train_no={} ".format(tno))
        print('database updated\n--------------------------------')
        
        co.commit()    
        main()

def cancel():
    co=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor2=''
    cursor2=co.cursor()
    time.sleep(2.5)
    pho=phone
    
    print('go to view ticket section to know your ticket id\n--------------')
    sql="select * from book_ticket where phone={}".format(pho)
    cursor2.execute(sql)
    a=cursor2.fetchall()
    for result in a:
        print(result)
    if cursor2.rowcount >=1:
        time.sleep(2.5)
        idd=int(input('how many tickets you want to delete?'))
        for i in range(1,idd+1):
            tq2=''
            ticket_id=input('enter your ticket id:')
            for tk2 in ticket_id:
                if tk2.isdigit():
                    pass
                else:
                    tq2=tq2+tk2
            s="delete from book_ticket where phone='{}' and name='{}';".format(str(phone),str(tq2))
            cursor2.execute(s)
            co.commit()
            print("1 ticket canceled\n-----------------------")
        main()   
        
    else :
        print('no tickets of the given id are registered!!!')
        main()
        
def update():
    time.sleep(2.5)
    user3=int(input('enter 1 for phone 2 for password to change and any key to exit'))
    if user3==1:
        update_phone()
    elif user3==2 :
        password()
    else :
        main()
        


def view():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(2.5) 
    cursor.execute("select * from book_ticket where phone={}".format(phone))
    a1=not None
    a1=cursor.fetchall()
    i=0
    for i in range(len(a1)):
        print('ticket id :',(a1[i][1]+str(a1[i][2])))
    main()

def delete_acc():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    cursor.execute("delete from user_info where username='{}'".format(user_id))
    conn.commit()
    time.sleep(2.5)
    print("account deleted")
    log_sign()
    
    main()

def generate():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(2.5)
    sql="select * from book_ticket where phone={} ".format(phone)
    cursor.execute(sql)
    lo=list(cursor.fetchall())
    loi=len(lo)
    print("please visit this section with your ticket_id\n-----------------")
    no_of_tkt=int(input('enter number of tickets you want to generate'))
    for j in range(1,(no_of_tkt)+1):
        for i in range(0,loi):
            tq=''
            tkt_id=input('enter the ticket id:')
            for tk1 in tkt_id:
                if tk1.isdigit():
                    pass
                else:
                    tq=tq+tk1
            cursor.execute("select * from book_ticket where phone={} and name='{}'".format(phone,tq))
            a=cursor.fetchall()

            
            tktnm=len(tkt_id)
            gap0=15-tktnm
            fill0=''
            fil0=''
            for k in range(0,gap0+1):
                fill0=fill0+str(random.randint(0,9))
            if tktnm<18:
                ii=str(fill0)+str(tkt_id)
            else:
                ttt=[]
                ttt=tkt_id.split()
                hn=len(ttt[0])+len(ttt[1])
                hd=15-hn
                for u in range(0,hd+1):
                    fil0=fil0+str(random.randint(0,9))
                ii=str(ttt[0]+ttt[1]+fil0)

            
            nm=len(a[i][1])
            gap=18-nm
            fill=''
            for k in range(0,gap+1):
                fill=fill+'_'
            if nm<18:
                name=str(a[i][1][:]).upper()+str(fill)
            else:
                name=str(a[i][1][:18]).upper()
            age=str(a[i][2])
            st_p=str(a[i][3][:3]).upper()
            ed_p=str(a[i][4][:3]).upper()
            ph=str(a[i][5])
            bkdt=str(a[i][6])
            jrdt=str(a[i][7])
            ttnm=len(a[i][8])
            gap1=18-ttnm
            fill1=''
            for k in range(0,gap1+1):
                fill1=fill1+'_'
            if ttnm<18:
                tnm=str(a[i][8][:]).upper()+str(fill1)
            else:
                tnm=str(a[i][8][:18]).upper()
            
            tno=str(a[i][9])
            stp=str(a[i][10])
            x=str(tkt_id)
            file=open("rail_ticket_"+x+".txt","w")
            a1= '''                     * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                     *                 INDIAN RAILWAYS RESERVATION MANAGEMENT                  *
                     * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                     *                                                                         *
                     * TICKET ID   :'''+ ii +'''     RESERVATION DATE  :'''+ bkdt+'''         *
                     *                                                                         *
                     * NAME        :'''+ name+'''  AGE               :'''+ age+'''                 *
                     *                                                                         *
                     * TRAIN NAME  :'''+ tnm +'''  TRAIN NUMBER      :'''+ tno +'''              *
                     *                                                                         *
                     * PHONE No.   :'''+ ph +'''           DATE OF JOURNEY   :'''+ jrdt +'''         *
                     *                                                                         *
                     * ROUTE       :'''+ st_p +''' to '''+ ed_p +'''           SEAT TYPE         :'''+ stp +'''                *
                     *                                                                         *
                     * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                     * *T&C Apply: Please do not try to make a fake ticket.TC will get to know *
                     *             if the ticket is real or fake, and you will be punished.    *
                     *                                                                         * 
                     *         THE RAILWAY MANAGEMENT WISHES YOU A VERY HAPPY JOURNEY.         *
                     *                STAY HEALTHY AND STAY SAFE. VISIT AGAIN                  *
                     *                                                                         *
                     * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *''' 

            file.write(a1+'\n')
            file.close()
            time.sleep(2.5)
            print(j,"ticket generated as rail_ticket_"+x+".txt\n")
    main()        


def issue():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(2.5)
    problem=input('enter your issue')
    cursor=conn.cursor()
    sql="insert into report (phone,report) values({},'{}')".format(phone,problem)
    cursor.execute(sql)
    conn.commit()
    time.sleep(2.5)
    print("report submitted successfully .")
    time.sleep(2.5)
    print('thanks for your valuable feedback')
    main()
   

def alldetails():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(2.5)
    cursor=conn.cursor()
    sql="select * from trains_detail" 
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        print(i)
    traindetails()

def enquiry1():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(1)
    n1=input('enter train no. whose details you want to search')
    cursor=conn.cursor()
    cursor.execute("select * from trains_detail where train_no={}".format(n1))
    l=cursor.fetchone()
    print('train name                :' +l[0])
    print('train number              :' +l[1])
    print('train source              :' +l[2])
    print('train destination         :' +l[3])
    print('total ac1 seats           :' +l[4])
    print('available ac1 seats       :' +l[5])
    print('total ac2 seats           :' +l[6])
    print('available ac2 seats       :' +l[7])
    print('total sleeper class seats :' +l[8])
    print('available sleeper seats   :' +l[9])
    main()
    

def enquiry():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(1)
    n1=input('enter train no. whose details you want to search')
    cursor=conn.cursor()
    cursor.execute("select * from trains_detail where train_no={}".format(n1))
    l=cursor.fetchone()
    print('train name                :' +l[0])
    print('train number              :' +l[1])
    print('train source              :' +l[2])
    print('train destination         :' +l[3])
    print('total ac1 seats           :' +l[4])
    print('available ac1 seats       :' +l[5])
    print('total ac2 seats           :' +l[6])
    print('available ac2 seats       :' +l[7])
    print('total sleeper class seats :' +l[8])
    print('available sleeper seats   :' +l[9])
    traindetails()

def traindetails():
    conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor=''
    cursor=conn.cursor()
    time.sleep(2.5)
    print("1. ALL train details\n2. PARTICULAR train details\n3.exit\n---------------------------")
    chc=int(input("enter your choice"))
    if chc==1:
        alldetails()
    elif chc==2:
        enquiry()
    elif chc==3:
        log_sign()
    else:
        print('wrong choice.\n try again\n-------------------')
        traindetails()    

def out():
    user_id=""
    time.sleep(2.5)
    print("you are logged out properly\n")
    log_sign()

def main():
    time.sleep(2.5)
    print('''-----------------------\n
        1. Book a ticket
        2. Cancel ticket
        3. Update your profile
        4. view tickets
        5. report issue
        6. delete account
        7. generate tickets(soft copy)
        8. enquiry
        9. Log out''')
    ch=input('enter your choice')
    if ch=='1':
        book()
    elif ch=='2':
        cancel()
    elif ch=='3' :
        update()
    elif ch=='4' :
        view()
    elif ch=='5' :
        issue()
    elif ch=='6' :
        delete_acc()    
    elif ch=='7' :
        generate()                   
    elif ch=='8' :
        enquiry1()
    elif ch=='9' :
        out() 
    else:
        print('wrong choice!!!\ntry again')
        main()
   
def login():
    conn12=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
    cursor7=''
    cursor7=conn12.cursor()
    global phone
    phone= ''
    global user_id
    a=[]
    time.sleep(2.5)
    ph=input('enter your phone number')
    phone=ph
    if len(str(ph))==10:
        user_id=''
        cursor7=conn12.cursor()
        cursor7.execute("select * from user_info where phone={}".format(ph))
        a=cursor7.fetchall()
        user_id=a[0][0]
        pn=a[0][2]
        p1=a[0][1]
        paswd=input('enter your password')
        p2="@@".join(paswd)
        if p2==p1 and ph==pn:
            main()
        else:
            time.sleep(2.5)
            print("incorrect details\n------------")
            login()
    else:
        time.sleep(2.5)
        print('invalid phone datails')
        ph=''
        login()

def signup():
    cursor=''
    cursor=conn.cursor()
    global c_pass
    time.sleep(2.5)
    username=input('enter your username : ')
    time.sleep(2.5)
    password=input('enter your password : ')
    time.sleep(2.5)
    c_pass=input('enter your password again : ')
    
    if password==c_pass :
        p="@@".join(password)
        time.sleep(2.5)
        phone=input('enter your phone number')
        r1=random.randint(100,200)
        r2=random.randint(100,200)
        r3=r1+r2
        time.sleep(2.5)
        print("prove that you are not a robot",r1,"+",r2)
        ans=int(input('enter your answer'))
        if ans==r3:
           if len(str(phone))==10:
               cursor=conn.cursor()
               sql="insert into user_info (username,pass,phone) values('{}','{}','{}')".format(username,p,phone)
               cursor.execute(sql)
               conn.commit()
               time.sleep(2.5)
               print("account created successfully\n------------------")
               log_sign()
                   
               
        else:
            time.sleep(2.5)
            print("wrong answer\n sign up again\n----------------------")
            signup()
    else:
        time.sleep(2.5)
        print("password doesn't match\n---------------------------")
        log_sign()


def log_sign():
    time.sleep(2.5)
    print("1. Sign up\n2. Login\n3. Train Details\n---------------------------")
    ch_1=int(input("enter choice"))
    if ch_1==1:
        signup()
    elif ch_1==2:
        login()
    elif ch_1==3:
        traindetails()     
    else:
        time.sleep(2.5)
        print('wrong choice.\n try again\n-------------------')
        log_sign()

user_id=''
conn=mysql.connector.connect(host='localhost',user='root',passwd='',database='rail_inq')
cursor=conn.cursor()
if conn.is_connected():
    print('succesfully connected to the server')    
if user_id!="":
    main()
else:
    log_sign()


    

        
    

    

    
            
            
            
            
        
        

        
            
    
    
          
           
        
    
        
               
                   
