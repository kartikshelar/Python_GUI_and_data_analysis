from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from tkinter import Frame
import tkinter.messagebox as tm
import re
from datetime import datetime
import pandas as pd
from pandastable import Table, TableModel
import tkinter as tk
import pymysql
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import itertools

import matplotlib
from matplotlib.figure import Figure
root = Tk()
root.title("Welcome")
root.geometry('{}x{}'.format(900,600 ))
root.config(bg="cadet blue")
#l = tk.Label(root,width=30, text='Welcome to Sunville Properties',fg="red",font=('arial', 20))
#l.pack()
label_0 =tk.Label(root, text="Welcome to Sunville Properties",width=50,background="cadet blue",fg="white",font=('arial', 24,"italic","bold"))
label_0 .place(x=0,y=80)
global NameEntry ,emailEntry ,idEntry_1 ,passEntry_1
global name,email,user_id_1,password_1
global custcodeEntry,select_year,my_canvas
global ordernoEntry
global TableValue
global order_number
global order_date
global customer_code
global yearOrder
global monthOrder
global dayOrder
global selected
global user_id
global password
global passEntry
global idEntry
global flag
global adddatawindow
global agentcode,agentname,agentarea,agentcommission,agentphone,agentcountry,selected_table,agcodeEntry,agnameEntry,agareaEntry,agcommEntry,agphoneEntry,agcountryEntry
global comidEntry,comnameEntry,comcityEntry,company_id,company_name,company_city
global agentcodeEntry,custcodeEntry,custcityEntry,custnameEntry,custareaEntry,custcountryEntry,gradeEntry,openamtEntry,recamtEntry,payamtEntry,outamtEntry,custphoneEntry,cust_phone,agent_code,out_amt,pay_amt, receive_amt,open_amount,grade,cust_country,cust_area,cust_name,cust_city,cust_name,cust_code
global ornumEntry,oramtEntry,adamtEntry,ordateEntry,custcodeEntry_1,orddesEntry,agcodeEntry_1,ord_num,ord_amt,ad_amt,ord_date,cust_code_1,agent_code_1,ord_des,yearBirth,monthBirth,dayBirth
def is_valid_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
        
    return False
def validate(event , input):
    
    if(input=="Name"):
        temp=name.get().lstrip()
        if  all(x.isalpha() or x.isspace() for x in temp) and (0<len(temp)<40):
           emailEntry.focus_set()
           emailEntry.config(state='normal') 
           
        else:
            tm.showerror("Invalidate!" ," Name cannot contain digits or special characters . Spaces are allowed. length should be less than 40") 
            NameEntry.focus_set()
    if( input == "email"):
        if is_valid_email(email.get()):
            idEntry_1.focus_set()
            idEntry_1.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Incorrect email formats. ")
            emailEntry.focus_set()
    if (input=="user id 1"):
        uid=user_id_1.get().lstrip()
        if (len(uid) < 5 or len(uid) > 30):
            tm.showerror("Invalidate!" ,"User id has to alphanumeric having length between 5 and 30.")
            idEntry_1.focus_set()
        else:
            passEntry_1.focus_set()
            passEntry_1.config(state='normal')
    if (input=="password 1"):
        
        pass1=password_1.get().lstrip()
        if  (len(pass1) < 5 or len(pass1) > 20):
            tm.showerror("Invalidate!" ,"Password has to alphanumeric having length between 5 and 20.")
            passEntry_1.focus_set()
    
    global passEntry
    if( input == "Order Number"):
        
        order_num = order_number.get()
        x=bool(re.fullmatch(r"([0-9]+)",order_num))
        if (x==False):
            tm.showerror("Invalid!" ,"Order number has to numeric")
            ordernoEntry.focus_set()
        
    if (input=="Customer code"):
        temp=customer_code.get()
        cust_co_1=temp[0]
        cust_co_rest=temp[1:]
        if cust_co_1!="C":
            tm.showerror("Invalid!" ,"Customer Code should start with C")
        x=bool(re.fullmatch(r"([0-9]+)",cust_co_rest))
        if x==False:
            tm.showerror("Invalid!" ,"Customer Code should start with C and the rest should be numeric")
    if (input=="user id"):
        global idEntry
        
        uid=user_id.get()
        if (len(uid) < 5 or len(uid) > 30):
            tm.showerror("Invalidate!" ,"User id has to alphanumeric having length between 5 and 20.")
            idEntry.focus_set()
        else:
            passEntry.focus_set()
            passEntry.config(state='normal')
    if (input=="password"):
        
        pass1=password.get()
        if (len(pass1) < 5 or len(pass1) > 30):
            tm.showerror("Invalidate!" ,"Password has to alphanumeric having length between 5 and 20.")
            passEntry.focus_set()
    if(input=="agent code"):
        temp=agentcode.get()
        acode_1=temp[0]
        acode_rest=temp[1:]
        x=bool(re.fullmatch(r"([0-9]+)",acode_rest))
        if (acode_1!="A") or x==False or len(temp)<1 or len(temp)>6:
            tm.showerror("Invalidate!" ,"Agent code should start with A and rest should be numeric and length should be less than 6")
        else:
            agnameEntry.focus_set()
            agnameEntry.config(state='normal')
            

    if(input=="agent name"):
        temp=agentname.get().lstrip()
        if  all(x.isalpha() or x.isspace() for x in temp) and (0<len(temp)<40):
           agareaEntry.focus_set()
           agareaEntry.config(state='normal') 
           
        else:
            tm.showerror("Invalidate!" ,"Agent name cannot contain digits or special characters . Spaces are allowed. length should be less than 40") 
            agnameEntry.focus_set()
            
    if(input=="agent area"):
        temp=agentarea.get().lstrip()
        if  all(x.isalpha() or x.isspace() for x in temp) and (0<len(temp)<35):
            agcommEntry.focus_set()
            agcommEntry.config(state='normal')  
        else:
            
            tm.showerror("Invalidate!" ,"Agent area cannot contain digits or special characters . Spaces are allowed. and length should be less than 35") 
            agareaEntry.focus_set()
            
    if(input=="agent commission"):
        
        if (agentcommission.get().isnumeric() or agentcommission.get().replace('.', '', 1).isdigit()) and (len(agentcommission.get())<=10) :
            agphoneEntry.focus_set()
            agphoneEntry.config(state='normal')
           
        else:
            tm.showerror("Invalidate!" ,"Agent commission should be a numeric value.Length should be less than 10") 
            agcommEntry.focus_set()
            
    if(input=="agent phone"):
        x=bool(re.fullmatch(r'^(\d{3}-\d{8})$',agentphone.get()))
        
        if x==True:
            agcountryEntry.focus_set()
            agcountryEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Invalid Phone Number (eg:-075-12458969). ")
            agphoneEntry.focus_set()
    if(input=="agent country"):
        if agentcountry.get()!="":
            temp=agentcountry.get().lstrip()
            x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
            if x==False  or len(temp)>25 :
                tm.showerror("Invalidate!" ,"Country Should be Alphabetical length should be less than 25")
                agcountryEntry.focus_set()
        
                
    if(input=="company id"):
        if company_id.get().isnumeric() and 0<len(company_id.get())<7:
            comnameEntry.focus_set()
            comnameEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Company ID: digits only length should be less than 7 ")
            comidEntry.focus_set()
    if(input=="company name"):
        temp=company_name.get().lstrip()
        if  all(x.isalpha() or x.isspace() for x in temp) and (0<len(temp)<40):
            comcityEntry.focus_set()
            comcityEntry.config(state='normal')
            
        else:
            tm.showerror("Invalidate!" ,"Company name should be alphabetical. Spaces are allowed length should be less than 25")
            comnameEntry.focus_set()
    if(input=="company city"):
        temp=company_city.get().lstrip()
        x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
        if x==False or 1>len(temp)>25:
            tm.showerror("Invalidate!" ,"Company City should be alphabetical. Spaces are allowed length should be less than 25")
            comcityEntry.focus_set()
    if (input=="customer code"):
        temp=cust_code.get()
        cust_co_1=temp[0]
        cust_co_rest=temp[1:]
        x=bool(re.fullmatch(r"([0-9]+)",cust_co_rest))
        if cust_co_1!="C" or x==False or len(temp)<0 or len(temp)>6:
            tm.showerror("Invalid!" ,"Customer Code should start with C and the rest should be numeric length should be less then 6")
            custcodeEntry.focus_set()
        else:
            custnameEntry.focus_set()
            custnameEntry.config(state='normal')
            
        
    if(input=="customer name"):
        temp=cust_name.get().lstrip()
        if all(x.isalpha() or x.isspace() for x in temp) and len(temp)>0 and len(temp)<40 :
        
            custcityEntry.focus_set()
            custcityEntry.config(state='normal')
        else:
            tm.showerror("Invalid!" ,"Customer name cannot contain digits or special characters, length should be less than 40")
            custnameEntry.focus_set()
        
    if(input=="customer city"):
        temp=cust_city.get().lstrip()
        x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
        if x==False or  len(temp)<1 or len(temp)>40:
            tm.showerror("Invalidate!" ,"Coustomer City should be alphabetical. Spaces are allowed .length should be less than 35")
            custcityEntry.focus_set()
        else:
            
            custareaEntry.focus_set()
            custareaEntry.config(state='normal')
    if(input=="customer area"):
        temp=cust_area.get().lstrip()
        x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
        if x==False or   len(temp)<1 or len(temp)>35:
            tm.showerror("Invalidate!" ,"Coustomer Area should be alphabetical. Spaces are allowed , length should be less than 35")
            custareaEntry.focus_set()
        else:
            
            custcountryEntry.focus_set()
            custcountryEntry.config(state='normal')
    if(input=="customer country"):
        temp=cust_country.get().lstrip()
        x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
        if x==True and  len(temp)>0 and len(temp)<21 :
            gradeEntry.focus_set()
            gradeEntry.config(state='normal')
            
        else:
            tm.showerror("Invalidate!" ,"Coustomer Country should be alphabetical ,length should be less than 20")
            custcountryEntry.focus_set()
    if(input=="grade"):
        
        if grade.get().isdigit() and len(grade.get())>0 and len(grade.get())<40 :
            openamtEntry.focus_set()
            openamtEntry.config(state='normal')
            
        else:
            tm.showerror("Invalidate!" ,"Grade Should be a number ")
            gradeEntry.focus_set()
    if(input=="opening amount"):
        
        if (open_amount.get().isnumeric() or open_amount.get().replace('.', '', 1).isdigit()) and 0<(len(open_amount.get()))<13:
            recamtEntry.focus_set()
            recamtEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ,length should not be greater than 12")
            openamtEntry.focus_set()
    if(input=="receive amount"):
        if (receive_amt.get().isnumeric() or receive_amt.get().replace('.', '', 1).isdigit()) and 0<len(receive_amt.get())<13:
            payamtEntry.focus_set()
            payamtEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ,length should not be greater than 12")
            recamtEntry.focus_set()
    if(input=="payment amount"):
        if (pay_amt.get().isnumeric() or pay_amt.get().replace('.', '', 1).isdigit()) and 0<(len(pay_amt.get()))<13:
            outamtEntry.focus_set()
            outamtEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ,length should not be greater than 12")
            payamtEntry.focus_set()
    if(input=="outstanding amount"):
        if ( out_amt.get().isnumeric() or out_amt.get().replace('.', '', 1).isdigit()) and 0<(len(out_amt.get()))<13:
            custphoneEntry.focus_set()
            custphoneEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ,length should not be greater than 12")
            outamtEntry.focus_set()
    if(input=="cust phone"):
        x=bool(re.fullmatch(r'^(\d{3}-\d{8})$',cust_phone.get()))
        
        if x==True:
        
            agentcodeEntry.focus_set()
            agentcodeEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Invalid Phone Number (eg:-075-12458969). ")
            custphoneEntry.focus_set()
    if(input=="agent code 2"):
        temp=agent_code.get()
        acode_1=temp[0]
        acode_rest=temp[1:]
        x=bool(re.fullmatch(r"([0-9]+)",acode_rest))
        if (acode_1!="A") or x==False or 1>(len(temp))>6:
            tm.showerror("Invalidate!" ,"Agent code should start with A and rest should be numeric ,length should not be more than 6")
        
            
    if( input == "order number"):
        if ord_num.get().isnumeric() and len(ord_num.get())==6 :
            oramtEntry.focus_set()
            oramtEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Order number should be numeric and 6 digits")
            ornumEntry.focus_set()
    if(input=="order amount"):
        
        if ord_amt.get().isnumeric() and ord_amt.get().replace('.', '', 1).isdigit() and 0<(len(ord_amt.get()))<13:
            adamtEntry.focus_set()
            adamtEntry.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ")
            oramtEntry.focus_set()
    if(input=="Advance Amount"):
        
        if ad_amt.get().isnumeric() and ad_amt.get().replace('.', '', 1).isdigit() and 0<(len(ad_amt.get()))<13:
            custcodeEntry_1.focus_set()
            custcodeEntry_1.config(state='normal')
        else:
            tm.showerror("Invalidate!" ,"Amount Should be Numeric ")
            adamtEntry.focus_set()
    if (input=="customer code 2"):
        temp=cust_code_1.get()
        cust_co_1=temp[0]
        cust_co_rest=temp[1:]
        x=bool(re.fullmatch(r"([0-9]+)",cust_co_rest))
        if cust_co_1!="C" or x==False or len(temp)>6:
            tm.showerror("Invalid!" ,"Customer Code should start with C and the rest should be numeric ,length should not be more than 6")
            custcodeEntry_1.focus_set()
        else:
            agcodeEntry_1.focus_set()
            agcodeEntry_1.config(state='normal')
            
        
    if(input=="agent code 3"):
        temp=agent_code_1.get()
        acode_1=temp[0]
        acode_rest=temp[1:]
        x=bool(re.fullmatch(r"([0-9]+)",acode_rest))
        if (acode_1!="A") or x==False or len(temp)>6:
            tm.showerror("Invalidate!" ,"Agent code should start with A and rest should be numeric,length should not be more than 6")
            agcodeEntry_1.focus_set()
        else:
            orddesEntry.focus_set()
            orddesEntry.config(state='normal')
            

    if(input=="order description"):
        if ord_des.get().isalpha()==False:
            tm.showerror("Invalidate!" ,"order description should be alphabetic")
    
            
def show_order():
     
    fill_no=0
    filled=[]
    global order_date
    if order_number.get()!="":
        fill_no=fill_no+1
        filled.append("order number")
    if customer_code.get()!="":
        fill_no=fill_no+1
        filled.append("customer code")
        
    if (yearOrder.get()!="") and (monthOrder.get()!="") and (dayOrder.get()!=""):
        fill_no=fill_no+1
        filled.append("order date")
        order_date=datetime.strptime(yearOrder.get() + "-" + monthOrder.get() + "-" + dayOrder.get(),'%Y-%m-%d')
        order_date=datetime.date(order_date)
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select * from orders"
        cur.execute(query)
        rows=list(cur.fetchall())
           
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to show")
    list_rows=[]
    df = pd.DataFrame()
    flag=0
    if fill_no==1:
        if filled[0]=="order number":
            order_num = order_number.get()
            x=bool(re.fullmatch(r"([0-9]+)",order_num))
            if (x==False):
                tm.showerror("Invalid!" ,"Order number has to numeric")
                ordernoEntry.focus_set()
                return
            for i in rows:
                i=list(i)
                i[0]=str(i[0])
                if i[0]==order_number.get():
                    list_rows.append(i)
                
    
        if filled[0]=="customer code":
            temp=customer_code.get()
            cust_co_1=temp[0]
            cust_co_rest=temp[1:]
            if cust_co_1!="C":
                tm.showerror("Invalid!" ,"Customer Code should start with C")
                return
                x=bool(re.fullmatch(r"([0-9]+)",cust_co_rest))
                if x==False:
                    tm.showerror("Invalid!" ,"Customer Code should start with C and the rest should be numeric")
                    return
            for i in rows:
                i=list(i)
                i[4]=str(i[4])
                if i[4]==customer_code.get():
                    list_rows.append(i)
            
        if filled[0]=="order date":
            for i in rows:
                i=list(i)
                #print(i[1])
                if i[3]==order_date:
                    list_rows.append(i)
    if fill_no==2:
        tm.showerror("ERROR" ,"User can fill either one or all of them together at a time")
        return
    if fill_no==3:
        order_num = order_number.get()
        x=bool(re.fullmatch(r"([0-9]+)",order_num))
        if (x==False):
            tm.showerror("Invalid!" ,"Order number has to numeric")
            ordernoEntry.focus_set()
            return
        temp=customer_code.get()
        cust_co_1=temp[0]
        cust_co_rest=temp[1:]
        if cust_co_1!="C":
            tm.showerror("Invalid!" ,"Customer Code should start with C")
            return
            x=bool(re.fullmatch(r"([0-9]+)",cust_co_rest))
            if x==False:
                tm.showerror("Invalid!" ,"Customer Code should start with C and the rest should be numeric")
                return
        for i in rows:
            i=list(i)
            i[0]=str(i[0])
            i[4]=str(i[4])
            if (i[0]==order_number.get()) and (i[3]==order_date) and (i[4]==customer_code.get()) :
                    list_rows.append(i)
    if len(list_rows)==0:
        tm.showerror("FAIL" ,"Order Not Found")
        return
               
    else:
        showorder_window=Toplevel()
        showorder_window.title("Orders")
        showorder_window.geometry('{}x{}'.format(800,700))
        df =pd.DataFrame(list_rows,columns=["ORD_NUM","ORD_AMOUNT","ADVANCE_AMOUNT","ORD_DATE","CUST_CODE","AGENT_CODE","ORD_DESCRIPTION"])
        table =Table(showorder_window, dataframe=df,showtoolbar=True, showstatusbar=True )
        table.currwidth = 700
        table.currheight = 500
        table.show()
    

def check():
    global user_id
    global password
    global flag
    global TableValue
    try:
        found=0
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        sql="select User_id,Password from employee_id"
        cur.execute(sql)
        rows_user=list(cur.fetchall())
        for i in rows_user:
            i=list(i)
            
            #print("in for")
            if(i[0]==user_id.get()) and (i[1]==password.get()):
                
                found=1
                break
        if found==1:
            flag=1
            
        else:
            tm.showerror("Login" ,"user not found")
        
        conn.close()

    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")
        
    if flag==1:
        adddatamainframe=Frame(adddatawindow)
        adddatamainframe.place(x=50,y=200)
        TableValue=StringVar()
        Label(adddatamainframe, text='Select the table you want to add data', anchor='w').grid(row=0, padx=5, pady=5, sticky="w")
        Radiobutton(adddatamainframe, text="Agents" ,variable=TableValue, value="agents" ).grid(row=1, padx=5, pady=5,sticky="w")
        Radiobutton(adddatamainframe, text="Company" ,variable=TableValue, value="company").grid(row=2,  padx=5, pady=5,sticky="w")
        Radiobutton(adddatamainframe, text="Customer" ,variable=TableValue, value="customer" ).grid(row=3, padx=5, pady=5,sticky="w")
        Radiobutton(adddatamainframe, text="Orders" ,variable=TableValue, value="order").grid(row=4,  padx=5, pady=5,sticky="w")
        Button(adddatamainframe, text="Submit",command=makeform).grid(row=5, padx=5)

def reg_form():
    global name,email,user_id_1,password_1
    global NameEntry ,emailEntry ,idEntry_1 ,passEntry_1 
    name=StringVar()
    email=StringVar()
    user_id_1=StringVar()
    password_1=StringVar()
    regform=Toplevel()
    regform.title("Registration form")
    regform.geometry('{}x{}'.format(500, 400))
    frame_reg_form=Frame(regform)
    frame_reg_form.place(x=50,y=20)
    Label(frame_reg_form, text='Full Name:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
    Label(frame_reg_form, text='Email:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
    Label(frame_reg_form, text='User ID:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
    Label(frame_reg_form ,text='Password:*', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w")
    NameEntry = Entry(frame_reg_form, width=20, textvariable=name)
    NameEntry .grid(row=0, column=1 ,padx=5, pady=5)
    NameEntry .bind("<Return>", lambda event: validate(event, "Name"))
    NameEntry .bind("<Tab>", lambda event: validate(event, "Name"))
    emailEntry = Entry(frame_reg_form, width=20, textvariable=email)
    emailEntry .grid(row=1, column=1 ,padx=5, pady=5)
    emailEntry .bind("<Return>", lambda event: validate(event, "email"))
    emailEntry .bind("<Tab>", lambda event: validate(event, "email"))
    idEntry_1 = Entry(frame_reg_form, width=20, textvariable=user_id_1)
    idEntry_1.grid(row=2, column=1 ,padx=5, pady=5)
    idEntry_1.bind("<Return>", lambda event: validate(event, "user id 1"))
    idEntry_1.bind("<Tab>", lambda event: validate(event, "user id 1"))
    passEntry_1 = Entry(frame_reg_form, width=20, textvariable=password_1)
    passEntry_1.grid(row=3, column=1 ,padx=5, pady=5)
    passEntry_1.bind("<Return>", lambda event: validate(event, "password 1"))
    passEntry_1.bind("<Tab>", lambda event: validate(event, "password 1"))
    passEntry_1.config(state='disabled')
    emailEntry .config(state='disabled')
    idEntry_1 .config(state='disabled')
    Button(frame_reg_form, text="Sign in",command=signin).grid(row=4, column=1, padx=5, pady=5)
def signin():
    
    pass1=password_1.get().lstrip()
    if (len(pass1) < 5 or len(pass1) > 30):
        tm.showerror("Invalidate!" ,"Password has to alphanumeric having length between 5 and 30. Space not allowed")
        passEntry_1.focus_set()
        return
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        
        sql="CREATE TABLE IF NOT EXISTS employee_id ( Name varchar(40),email varchar(30) ,User_id varchar(30),Password varchar(20) )"
        cur.execute(sql)
        sql_insert="INSERT INTO employee_id(Name, email, User_id, Password)  VALUES (%s,%s,%s,%s)"
        cur.execute(sql_insert ,(name.get(),email.get(),user_id_1.get(),password_1.get()))
        conn.close()
        tm.showinfo("Save" , "Success!")
        return
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")
    
def login(event):
    global adddatawindow
    adddatawindow=Toplevel()
    adddatawindow.title("Login")
    adddatawindow.geometry('{}x{}'.format(500, 400))
    frame_adddata=Frame(adddatawindow)
    frame_adddata.place(x=50,y=20)
    global user_id
    global password
    user_id=StringVar()
    password=StringVar()
    global passEntry
    global idEntry
    global flag
    flag=0
    
    Label(frame_adddata, text='User ID:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
    Label(frame_adddata, text='Password:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
    idEntry = Entry(frame_adddata, width=20, textvariable=user_id)
    idEntry.grid(row=0, column=1 ,padx=5, pady=5)
    idEntry.bind("<Return>", lambda event: validate(event, "user id"))
    idEntry.bind("<Tab>", lambda event: validate(event, "user id"))
    passEntry = Entry(frame_adddata,show="*", width=20, textvariable=password)
    passEntry.grid(row=1, column=1 ,padx=5, pady=5)
    passEntry.bind("<Return>", lambda event: validate(event, "password"))
    passEntry.bind("<Tab>", lambda event: validate(event, "password"))
    passEntry.config(state='disabled')
    Button(frame_adddata, text="Sign in",command=reg_form).grid(row=2, column=0, padx=5, pady=5)
    Button(frame_adddata, text="Log In",command=check).grid(row=2, column=1, padx=5, pady=5)
   
    adddatawindow.mainloop()
def makeform():
    #print(TableValue.get())
    global selected_table
    
    makeformwindow=Toplevel()
    makeformwindow.title("Login")
    makeformwindow.geometry('{}x{}'.format(500, 600))
    frame_makeform_0=Frame(makeformwindow)
    frame_makeform_0.pack()
    Label(frame_makeform_0, text='Please fill in the details to add data to the tabel', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
    frame_makeform=Frame(makeformwindow)
    frame_makeform.pack()
    if TableValue.get()=="agents":
        
        Label(frame_makeform, text='Agent Code:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Agent Name:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Working Area:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Commission:*', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Phone number:*', anchor='w').grid(row=4, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Country:', anchor='w').grid(row=5, column=0 ,padx=5, pady=5, sticky="w")
        global agcodeEntry,agentcode,agentname,agentarea,agentcommission,agentphone,agentcountry,agnameEntry,agareaEntry,agcommEntry,agphoneEntry,agcountryEntry
        selected_table="Agents Table"
        agentcode=StringVar()
        agentname=StringVar()
        agentarea=StringVar()
        agentcommission=StringVar()
        agentphone=StringVar()
        agentcountry=StringVar()
        agcodeEntry = Entry(frame_makeform, width=20, textvariable=agentcode)
        agcodeEntry.grid(row=0, column=1 ,padx=5, pady=5)
        agcodeEntry.bind("<Return>", lambda event: validate(event, "agent code"))
        agcodeEntry.bind("<Tab>", lambda event: validate(event, "agent code"))
        agnameEntry = Entry(frame_makeform, width=20, textvariable=agentname)
        agnameEntry.grid(row=1, column=1 ,padx=5, pady=5)
        agnameEntry.bind("<Return>", lambda event: validate(event, "agent name"))
        agnameEntry.bind("<Tab>", lambda event: validate(event, "agent name"))
        agareaEntry = Entry(frame_makeform, width=20, textvariable=agentarea)
        agareaEntry.grid(row=2, column=1 ,padx=5, pady=5)
        agareaEntry.bind("<Return>", lambda event: validate(event, "agent area"))
        agareaEntry.bind("<Tab>", lambda event: validate(event, "agent area"))
        agcommEntry = Entry(frame_makeform, width=20, textvariable=agentcommission)
        agcommEntry.grid(row=3, column=1 ,padx=5, pady=5)
        agcommEntry.bind("<Return>", lambda event: validate(event, "agent commission"))
        agcommEntry.bind("<Tab>", lambda event: validate(event, "agent commission"))
        agphoneEntry = Entry(frame_makeform, width=20, textvariable=agentphone)
        agphoneEntry.grid(row=4, column=1 ,padx=5, pady=5)
        agphoneEntry.bind("<Return>", lambda event: validate(event, "agent phone"))
        agphoneEntry.bind("<Tab>", lambda event: validate(event, "agent phone"))
        agcountryEntry = Entry(frame_makeform, width=20, textvariable=agentcountry)
        agcountryEntry.grid(row=5, column=1 ,padx=5, pady=5)
        agcountryEntry.bind("<Return>", lambda event: validate(event, "agent country"))
        agcountryEntry.bind("<Tab>", lambda event: validate(event, "agent country"))
        
        agnameEntry.config(state='disabled')
        agareaEntry.config(state='disabled')
        agcommEntry.config(state='disabled')
        agphoneEntry.config(state='disabled')
        agcountryEntry.config(state='disabled')
        Button(frame_makeform, text="Submit",command=saveTable).grid(row=6, column=0, padx=20, pady=5)
    elif TableValue.get()=="company":
        selected_table="Company Table"
        Label(frame_makeform, text='Company ID*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Company Name:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Company City:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
        global comidEntry,comnameEntry,comcityEntry,company_id,company_name,company_city
        company_id=StringVar()
        company_name=StringVar()
        company_city=StringVar()
        comidEntry = Entry(frame_makeform, width=20, textvariable=company_id)
        comidEntry.grid(row=0, column=1 ,padx=5, pady=5)
        comidEntry.bind("<Return>", lambda event: validate(event, "company id"))
        comidEntry.bind("<Tab>", lambda event: validate(event, "company id"))
        comnameEntry = Entry(frame_makeform, width=20, textvariable=company_name)
        comnameEntry.grid(row=1, column=1 ,padx=5, pady=5)
        comnameEntry.bind("<Return>", lambda event: validate(event, "company name"))
        comnameEntry.bind("<Tab>", lambda event: validate(event, "company name"))
        comcityEntry = Entry(frame_makeform, width=20, textvariable=company_city)
        comcityEntry.grid(row=2, column=1 ,padx=5, pady=5)
        comcityEntry.bind("<Return>", lambda event: validate(event, "company city"))
        comcityEntry.bind("<Tab>", lambda event: validate(event, "company city"))
        
        comnameEntry.config(state='disabled')
        comcityEntry.config(state='disabled')
        Button(frame_makeform, text="Submit",command=saveTable).grid(row=3, column=0, padx=10, pady=5)
        
    elif TableValue.get()=="customer":
        selected_table="Customer Table"
        Label(frame_makeform, text='Customer Code:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Customer Name:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Customer City:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Working Area:*', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Customer Country:*', anchor='w').grid(row=4, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Grade:', anchor='w').grid(row=5, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Opening Amount:*', anchor='w').grid(row=6, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Recive Amount:*', anchor='w').grid(row=7, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Payment Amount:*', anchor='w').grid(row=8, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Outstanding Amount:*', anchor='w').grid(row=9, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Phone NO:*', anchor='w').grid(row=10, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Agent Code', anchor='w').grid(row=11, column=0 ,padx=5, pady=5, sticky="w")
        
        global agentcodeEntry,custcodeEntry,custcityEntry,custnameEntry,custareaEntry,custcountryEntry,gradeEntry,openamtEntry,recamtEntry,payamtEntry,outamtEntry,custphoneEntry,cust_phone,agent_code,out_amt,pay_amt, receive_amt,open_amount,grade,cust_country,cust_area,cust_name,cust_city,cust_name,cust_code
        cust_phone=StringVar()
        agent_code=StringVar()
        out_amt=StringVar()
        pay_amt=StringVar()
        receive_amt=StringVar()
        open_amount=StringVar()
        grade=StringVar()
        cust_country=StringVar()
        cust_area=StringVar()
        cust_name=StringVar()
        cust_city=StringVar()
        cust_name=StringVar()
        cust_code=StringVar()
        
        
        custcodeEntry = Entry(frame_makeform, width=20, textvariable=cust_code)
        custcodeEntry.grid(row=0, column=1 ,padx=5, pady=5)
        custcodeEntry.bind("<Return>", lambda event: validate(event, "customer code"))
        custcodeEntry.bind("<Tab>", lambda event: validate(event, "customer code"))
        custnameEntry = Entry(frame_makeform, width=20, textvariable=cust_name)
        custnameEntry.grid(row=1, column=1 ,padx=5, pady=5)
        custnameEntry.bind("<Return>", lambda event: validate(event, "customer name"))
        custnameEntry.bind("<Tab>", lambda event: validate(event, "customer name"))
        custcityEntry = Entry(frame_makeform, width=20, textvariable=cust_city)
        custcityEntry.grid(row=2, column=1 ,padx=5, pady=5)
        custcityEntry.bind("<Return>", lambda event: validate(event, "customer city"))
        custcityEntry.bind("<Tab>", lambda event: validate(event, "customer city"))
        custareaEntry = Entry(frame_makeform, width=20, textvariable=cust_area)
        custareaEntry.grid(row=3, column=1 ,padx=5, pady=5)
        custareaEntry.bind("<Return>", lambda event: validate(event, "customer area"))
        custareaEntry.bind("<Tab>", lambda event: validate(event, "customer area"))
        custcountryEntry = Entry(frame_makeform, width=20, textvariable=cust_country)
        custcountryEntry.grid(row=4, column=1 ,padx=5, pady=5)
        custcountryEntry.bind("<Return>", lambda event: validate(event, "customer country"))
        custcountryEntry.bind("<Tab>", lambda event: validate(event, "customer country"))
        gradeEntry = Entry(frame_makeform, width=20, textvariable=grade)
        gradeEntry.grid(row=5, column=1 ,padx=5, pady=5)
        gradeEntry.bind("<Return>", lambda event: validate(event, "grade"))
        gradeEntry.bind("<Tab>", lambda event: validate(event, "grade"))
        openamtEntry = Entry(frame_makeform, width=20, textvariable=open_amount)
        openamtEntry.grid(row=6, column=1 ,padx=5, pady=5)
        openamtEntry.bind("<Return>", lambda event: validate(event, "opening amount"))
        openamtEntry.bind("<Tab>", lambda event: validate(event, "opening amount"))
        recamtEntry = Entry(frame_makeform, width=20, textvariable=receive_amt)
        recamtEntry.grid(row=7, column=1 ,padx=5, pady=5)
        recamtEntry.bind("<Return>", lambda event: validate(event, "receive amount"))
        recamtEntry.bind("<Tab>", lambda event: validate(event, "receive amount"))
        payamtEntry = Entry(frame_makeform, width=20, textvariable=pay_amt)
        payamtEntry.grid(row=8, column=1 ,padx=5, pady=5)
        payamtEntry.bind("<Return>", lambda event: validate(event, "payment amount"))
        payamtEntry.bind("<Tab>", lambda event: validate(event, "payment amount"))
        outamtEntry = Entry(frame_makeform, width=20, textvariable=out_amt)
        outamtEntry.grid(row=9, column=1 ,padx=5, pady=5)
        outamtEntry.bind("<Return>", lambda event: validate(event, "outstanding amount"))
        outamtEntry.bind("<Tab>", lambda event: validate(event, "outstanding amount"))
        custphoneEntry = Entry(frame_makeform, width=20, textvariable=cust_phone)
        custphoneEntry.grid(row=10, column=1 ,padx=5, pady=5)
        custphoneEntry.bind("<Return>", lambda event: validate(event, "cust phone"))
        custphoneEntry.bind("<Tab>", lambda event: validate(event, "cust phone"))
        agentcodeEntry = Entry(frame_makeform, width=20, textvariable=agent_code)
        agentcodeEntry.grid(row=11, column=1 ,padx=5, pady=5)
        agentcodeEntry.bind("<Return>", lambda event: validate(event, "agent code 2"))
        agentcodeEntry.bind("<Tab>", lambda event: validate(event, "agent code 2"))
        agentcodeEntry.config(state='disabled')
        custcityEntry.config(state='disabled')
        custnameEntry.config(state='disabled')
        custareaEntry.config(state='disabled')
        custcountryEntry.config(state='disabled')
        gradeEntry.config(state='disabled')
        openamtEntry.config(state='disabled')
        recamtEntry.config(state='disabled')
        payamtEntry.config(state='disabled')
        outamtEntry.config(state='disabled')
        custphoneEntry.config(state='disabled')
        Button(frame_makeform, text="Submit",command=saveTable).grid(row=12, column=0, padx=10, pady=5)
    elif TableValue.get()=="order":
        selected_table="Order Table"
        Label(frame_makeform, text='Order Number:*', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Order Amount:*', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Advance Amount:*', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Order Date:*', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Customer Code:*', anchor='w').grid(row=4, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Agent Code', anchor='w').grid(row=5, column=0 ,padx=5, pady=5, sticky="w")
        Label(frame_makeform, text='Order Descrription:*', anchor='w').grid(row=6, column=0 ,padx=5, pady=5, sticky="w")
        
        global ornumEntry,oramtEntry,adamtEntry,ordateEntry,custcodeEntry_1,orddesEntry,agcodeEntry_1,ord_num,ord_amt,ad_amt,ord_date,cust_code_1,agent_code_1,ord_des,yearBirth,monthBirth,dayBirth
        ord_num=StringVar()
        ord_amt=StringVar()
        ad_amt=StringVar()
        ord_date=StringVar()
        cust_code_1=StringVar()
        agent_code_1=StringVar()
        ord_des=StringVar()
        ornumEntry = Entry(frame_makeform, width=20, textvariable=ord_num)
        ornumEntry.grid(row=0, column=1 ,padx=5, pady=5)
        ornumEntry.bind("<Return>", lambda event: validate(event, "order number"))
        ornumEntry.bind("<Tab>", lambda event: validate(event, "order number"))
        oramtEntry = Entry(frame_makeform, width=20, textvariable=ord_amt)
        oramtEntry.grid(row=1, column=1 ,padx=5, pady=5)
        oramtEntry.bind("<Return>", lambda event: validate(event, "order amount"))
        oramtEntry.bind("<Tab>", lambda event: validate(event, "order amount"))
        adamtEntry = Entry(frame_makeform, width=20, textvariable=ad_amt)
        adamtEntry.grid(row=2, column=1 ,padx=5, pady=5)
        adamtEntry.bind("<Return>", lambda event: validate(event, "Advance Amount"))
        adamtEntry.bind("<Tab>", lambda event: validate(event, "Advance Amount"))
        
        birthFrame = Frame(frame_makeform)
        yearBirth = StringVar()
        choices = list(range(2018,2021))
        Combobox(birthFrame , width=5, values = choices ,textvariable = yearBirth ).grid(row=0, column=1, padx=5, pady=5)
        monthBirth = StringVar()
        choices = list(range(1,13))
        Combobox(birthFrame , width=5, values = choices ,textvariable = monthBirth ).grid(row=0, column=2, padx=5, pady=5)
        dayBirth = StringVar()
        choices = list(range(1,32))
        Combobox(birthFrame , width=5, values = choices ,textvariable = dayBirth ).grid(row=0, column=3, padx=5, pady=5)
        birthFrame.grid(row=3, column=1, padx=5, pady=5)
        
        yearBirth.set("2019")
        monthBirth.set("1")
        dayBirth.set("1")
        
        custcodeEntry_1 = Entry(frame_makeform, width=20, textvariable=cust_code_1)
        custcodeEntry_1.grid(row=4, column=1 ,padx=5, pady=5)
        custcodeEntry_1.bind("<Return>", lambda event: validate(event, "customer code 2"))
        custcodeEntry_1.bind("<Tab>", lambda event: validate(event, "customer code 2"))
        agcodeEntry_1 = Entry(frame_makeform, width=20, textvariable=agent_code_1)
        agcodeEntry_1.grid(row=5, column=1 ,padx=5, pady=5)
        agcodeEntry_1.bind("<Return>", lambda event: validate(event, "agent code 3"))
        agcodeEntry_1.bind("<Tab>", lambda event: validate(event, "agent code 3"))
        orddesEntry = Entry(frame_makeform, width=20, textvariable=ord_des)
        orddesEntry.grid(row=6, column=1 ,padx=5, pady=5)
        orddesEntry.bind("<Return>", lambda event: validate(event, "order description"))
        orddesEntry.bind("<Tab>", lambda event: validate(event, "order description"))
        

        oramtEntry.config(state='disabled')
        adamtEntry.config(state='disabled')
        custcodeEntry_1.config(state='disabled')
        orddesEntry.config(state='disabled')
        agcodeEntry_1.config(state='disabled')
        
        Button(frame_makeform, text="Submit",command=saveTable).grid(row=7, column=0, padx=10, pady=5)
        
    
def saveTable():
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        if selected_table=="Agents Table":
            if agentcountry.get()!="":
                temp=agentcountry.get().lstrip()
                x=bool(re.fullmatch('[a-zA-Z\s]+$',temp))
                if x==False  or len(temp)>25 :
                    tm.showerror("Invalidate!" ,"Country Should be Alphabetical length should be less than 25")
                    agcountryEntry.focus_set()
                    return
            sql_insert="INSERT INTO agents(AGENT_CODE, AGENT_NAME, WORKING_AREA, COMMISSION, PHONE_NO, COUNTRY)  VALUES (%s,%s,%s,%s,%s,%s)"
            cur.execute(sql_insert ,(agentcode.get(),agentname.get(),agentarea.get(),agentcommission.get(),agentphone.get(),agentcountry.get()))
            conn.close()
            tm.showinfo("Save" , "Success!")
               
           
           
        if selected_table=="Company Table":
            x=bool(re.fullmatch('[a-zA-Z\s]+$',company_city.get()))
            if x==False:
                tm.showerror("Invalidate!" ,"Company City should be alphabetical. Spaces are allowed ")
                return
            sql_insert="INSERT INTO company(COMPANY_ID, COMPANY_NAME, COMPANY_CITY)  VALUES (%s,%s,%s)"
            cur.execute(sql_insert ,(company_id.get(),company_name.get(),company_city.get()))
            conn.close()
            tm.showinfo("Save" , "Success!")
        if selected_table=="Customer Table":
            temp=agent_code.get()
            acode_1=temp[0]
            acode_rest=temp[1:]
            x=bool(re.fullmatch(r"([0-9]+)",acode_rest))
            if (acode_1!="A") or x==False or 1>(len(temp))>6:
                tm.showerror("Invalidate!" ,"Agent code should start with A and rest should be numeric ,length should not be more than 6")
                return

            sql_insert="INSERT INTO customer(CUST_CODE, CUST_NAME, CUST_CITY, WORKING_AREA, CUST_COUNTRY, GRADE, OPENING_AMT, RECEIVE_AMT, PAYMENT_AMT, OUTSTANDING_AMT, PHONE_NO, AGENT_CODE)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql_insert ,(cust_code.get(),cust_name.get(),cust_city.get(),cust_area.get(),cust_country.get(),grade.get(),open_amount.get(), receive_amt.get(),pay_amt.get(),out_amt.get(),cust_phone.get(),agent_code.get()))
            conn.close()
            tm.showinfo("Save" , "Success!")
        if selected_table=="Order Table":
            
             if ord_des.get().isalpha()==False:
                 tm.showerror("Invalidate!" ,"order description should be alphabetic")
                 return
             OrdDateObj=datetime.strptime(yearBirth.get() + "-" + monthBirth.get() + "-" + dayBirth.get(),'%Y-%m-%d')
             sql_insert="INSERT INTO orders(ORD_NUM, ORD_AMOUNT, ADVANCE_AMOUNT, ORD_DATE, CUST_CODE, AGENT_CODE, ORD_DESCRIPTION)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
             cur.execute(sql_insert ,(ord_num.get(),ord_amt.get(),ad_amt.get(),OrdDateObj.strftime("%Y-%m-%d"),cust_code_1.get(),agent_code_1.get(),ord_des.get()))
             conn.close()
             tm.showinfo("Save" , "Success!")
     
    except Exception as e:
        print(e)
        tm.showerror("Error" ,e)
  
def orderlookup(event):
    orderlookupwindow=Toplevel()
    orderlookupwindow.title("ORDER LOOK UP")
    orderlookupwindow.geometry('{}x{}'.format(600, 500))
    frame_0=Frame(orderlookupwindow)
    frame_0.pack()
    Label(frame_0, text='Please fill in the order details', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
    mainframe_order_search = Frame(orderlookupwindow)
    mainframe_order_search.pack()
    global order_number
    global customer_code
    global yearOrder
    global monthOrder
    global dayOrder
    global custcodeEntry
    global ordernoEntry
    yearOrder=StringVar()
    monthOrder=StringVar()
    dayOrder=StringVar()
    order_number=StringVar()
    customer_code=StringVar()
    Label(mainframe_order_search, text='Order Number', anchor='w').grid(row=1, column=0 ,padx=5, pady=5, sticky="w")
    ordernoEntry = Entry(mainframe_order_search, width=20, textvariable=order_number)
    ordernoEntry.grid(row=1, column=1 ,padx=5, pady=5)
    ordernoEntry.bind("<Return>", lambda event: validate(event, "Order Number"))
    ordernoEntry.bind("<Tab>", lambda event: validate(event, "Order Number"))
    Label(mainframe_order_search, text='Order Date', anchor='w').grid(row=3, column=0 ,padx=5, pady=5, sticky="w")
    birthFrame = Frame(mainframe_order_search)
    choices = list(range(2018,2020))
    Combobox(birthFrame , width=5, values = choices ,textvariable = yearOrder ).grid(row=0, column=1, padx=5, pady=5)
    choices = list(range(1,13))
    Combobox(birthFrame , width=5, values = choices ,textvariable = monthOrder ).grid(row=0, column=2, padx=5, pady=5)
    choices = list(range(1,32))
    Combobox(birthFrame , width=5, values = choices ,textvariable = dayOrder ).grid(row=0, column=3, padx=5, pady=5)
    
    
    birthFrame.grid(row=3, column=1, padx=5, pady=5)
    Label(mainframe_order_search, text='Customer code', anchor='w').grid(row=2, column=0 ,padx=5, pady=5, sticky="w")
    custcodeEntry = Entry(mainframe_order_search, width=20, textvariable=customer_code)
    custcodeEntry.grid(row=2, column=1 ,padx=5, pady=5)
    custcodeEntry.bind("<Return>", lambda event: validate(event, "Customer code"))
    custcodeEntry.bind("<Tab>", lambda event: validate(event, "Customer code"))
    Button(mainframe_order_search, text="search",command=show_order).grid(row=4,padx=10)

def balance(event):
    balance_window=Toplevel()
    balance_window.title("Balance")
    balance_window.geometry('{}x{}'.format(700, 600))
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select OUTSTANDING_AMT,AGENT_CODE from customer"
        cur.execute(query)
        rows_balnce=list(cur.fetchall())
        for i in range(0,len(rows_balnce)):
            rows_balnce[i]=list(rows_balnce[i])
        rows_balnce.sort()
        rows_balnce.reverse()
        
        query="select AGENT_CODE,AGENT_NAME from agents"
        cur.execute(query)
        rows_agents=list(cur.fetchall())
        for i in range(0,len(rows_agents)):
            rows_agents[i]=list(rows_agents[i])
            
        
        for i in rows_balnce:
            
            for j in rows_agents:
                if i[1]==j[0]:
                    i.append(j[1])

        
        df = pd.DataFrame()
        df = TableModel.getSampleData()
        df = pd.DataFrame( rows_balnce,columns =["Balance Amt","Agent Code","Agent Name"])
        conn.close()
        
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to show")
    table =Table(balance_window, dataframe=df,showtoolbar=True, showstatusbar=True )
    table.currwidth = 700
    table.currheight = 500
    
    table.show()
    try:
        
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        
        sql="CREATE TABLE IF NOT EXISTS Balance_Amount ( Balance_amount decimal(12,2),Agent_code varchar(6),Agent_name varchar(40) )"
        cur.execute(sql)
        
        sql_insert="INSERT INTO Balance_Amount(Balance_amount,Agent_code,Agent_name)  VALUES (%s,%s,%s)"
        for i in rows_balnce:
            cur.execute(sql_insert ,i)
        conn.close()
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make table")

def cust_country(event):
    cust_country_window=Toplevel()
    cust_country_window.title("Stats per Country")
    cust_country_window.geometry('{}x{}'.format(700, 600))
    try:
        
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select CUST_COUNTRY from customer"
        cur.execute(query)
        temp=list(cur.fetchall())
        countries=[]
    
        for i in temp:
            
            countries.append(i[0])
            
        
        in_country=list(set(countries))
        
        count= Counter(countries)
        country_count=[]
        for i in range(0,len(in_country)):
            counter=count[in_country[i]]
            country_count.append(counter)
        
        list_country_count=[]
        max=0
        for i in range(0,len(in_country)):
            temp_list=[]
            temp_list.append(in_country[i])
            temp_list.append(country_count[i])
            list_country_count.append(temp_list)
            if max<country_count[i]:
                max=country_count[i]
        in_country.sort()
        
        #print(dict_country_count)
        df1 =pd.DataFrame(list_country_count,columns=['Country','customers'])
        bar_label=tk.Label(cust_country_window,width=30, text='Registered Customers per Country',fg="blue",font=('arial', 15))
        bar_label.pack()
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1,cust_country_window)
        bar1.get_tk_widget().pack()
        df1 = df1[['Country','customers']].groupby('Country').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Customers per Country')
        conn.close()
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")
        
def country_pay(event):
    country_pay_window=Toplevel()
    country_pay_window.title("Stats per Country")
    country_pay_window.geometry('{}x{}'.format(500, 500))
    
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select CUST_COUNTRY,PAYMENT_AMT,OUTSTANDING_AMT from customer"
        cur.execute(query)
        amt=list(cur.fetchall())
        df_amt =pd.DataFrame(amt,columns=['Country','Pay_Amt','Out_Amt'])
        countries=list(set(df_amt["Country"].tolist()))
        list_country_amt=[]
        for i in countries:
            temp=(df_amt [(df_amt.Country==i)].Pay_Amt).tolist()
            total_amt=sum(temp)
            list_country_amt.append(total_amt)
        total=sum(list_country_amt)
        list_country_amt.append(total)
        countries.append("Total Outstanding Amt")
        
        
        list_country_payment=[]
        for i in range(0,len(countries)):
            temp=[countries[i],list_country_amt[i]]
            list_country_payment.append(temp)
        
        
        df2 = pd.DataFrame()
        df2 = TableModel.getSampleData()
        df2 =pd.DataFrame(list_country_payment,columns=['Country','Total Payment'])
        table =Table(country_pay_window, dataframe=df2,showtoolbar=True, showstatusbar=True )
        table.currwidth = 800
        table.currheight = 800
        
        table.show()
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")

def country_out(event):
    country_out_window=Toplevel()
    country_out_window.title("Stats per Country")
    country_out_window.geometry('{}x{}'.format(500, 400))
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select CUST_COUNTRY,PAYMENT_AMT,OUTSTANDING_AMT from customer"
        cur.execute(query)
        amt=list(cur.fetchall())
        df_amt =pd.DataFrame(amt,columns=['Country','Pay_Amt','Out_Amt'])
        
        countries=list(set(df_amt["Country"].tolist()))
        #print(countries)
        list_country_amt=[]
        for i in countries:
            temp=(df_amt [(df_amt.Country==i)].Out_Amt).tolist()
            total_amt=sum(temp)
            list_country_amt.append(total_amt)
        total=sum(list_country_amt)
        list_country_amt.append(total)
        countries.append("Total Outstanding Amt")
        list_country_outstanding=[]
        
        for i in range(0,len(countries)):
            temp=[countries[i],list_country_amt[i]]
            list_country_outstanding.append(temp)
            
        df3 = pd.DataFrame()
        df3 = TableModel.getSampleData()
        df3 =pd.DataFrame(list_country_outstanding,columns=['Country','Total Outstanding Amount'])
        table =Table(country_out_window, dataframe=df3,showtoolbar=True, showstatusbar=True )
        table.currwidth = 800
        table.currheight = 800
        
        table.show()
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")
    

def country(event):
    country_window=Toplevel()
    country_window.title("Country wise customer")
    country_window.geometry('{}x{}'.format(900, 600))
    l = tk.Label(country_window,width=30, text='Stats per Country',fg="blue",font=('arial', 20))
    l.pack()
    img_cust=ImageTk.PhotoImage(PIL.Image.open("max_customer.PNG"))
    customer_button=tk.Button(country_window,image=img_cust)
    customer_button.place(x=20,y=50)
    customer_button.bind("<Button-1>",cust_country)
    img_pay=ImageTk.PhotoImage(PIL.Image.open("payment_amt.PNG"))
    pay_button=tk.Button(country_window,image=img_pay)
    pay_button.place(x=450,y=50)
    pay_button.bind("<Button-1>",country_pay)
    img_out=ImageTk.PhotoImage(PIL.Image.open("outstanding_amt.PNG"))
    out_button=tk.Button(country_window,image=img_out)
    out_button.place(x=250,y=300)
    out_button.bind("<Button-1>",country_out)
    country_window.mainloop()
    
    
    
    
def employee(event):
    searchwindow=Toplevel()
    searchwindow.title("EMPLOYEE")
    searchwindow.geometry('{}x{}'.format(900, 600))
    searchwindow.config(bg="cadet blue")
    img_add=ImageTk.PhotoImage(PIL.Image.open("add_data.PNG"))
    add_data_button=tk.Button(searchwindow,image=img_add)
    add_data_button.place(x=10,y=10)
    add_data_button.bind("<Button-1>",login)
    img_look=ImageTk.PhotoImage(PIL.Image.open("order_lookup.PNG"))
    order_lookup_button=tk.Button(searchwindow,image=img_look)
    order_lookup_button.place(x=450,y=10)
    order_lookup_button.bind("<Button-1>",orderlookup)
    img_bal=ImageTk.PhotoImage(PIL.Image.open("balance_amt.PNG"))
    balance_button=tk.Button(searchwindow,image=img_bal)
    balance_button.place(x=10,y=300)
    balance_button.bind("<Button-1>",balance)
    img_country=ImageTk.PhotoImage(PIL.Image.open("stats_country.PNG"))
    country_button=tk.Button(searchwindow,image=img_country)
    country_button.place(x=450,y=300)
    country_button.bind("<Button-1>",country)
    searchwindow.mainloop()

def showagenttable(event):
    df_dataset=pd.DataFrame()
    for f in ["Dataset.xlsx"]:
        data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
        df_dataset=df_dataset.append(data)
            
    owneddeals=df_dataset.loc[df_dataset['Tenure'] == 'Owned']
    print(owneddeals)
    try:
        conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = conn.cursor()
        query="select AGENT_CODE,AGENT_NAME from agents"
        cur.execute(query)
        rows=list(cur.fetchall())
    except Exception as e:
        print(e)
        tm.showerror("Show" ,"Failed to make connection")
    temp_agent=[]
    if select_year.get()=="ALL":
        temp=owneddeals["Agent"].tolist()
        #print(agents)
        temp=list(set(temp))
        agents=[]
        for i  in temp:
            name=""
            words = i.split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            agents.append(name)
        agents=list(set(agents))
        #print(agents)
        
        for i in rows:
            i=list(i)
            for j in agents:
                i[1]=str(i[1])
                name = i[1].rstrip()

                j=str(j)
                if name==j:
                    temp=[j,i[0]]
                    temp_agent.append(temp)
        
        
    elif select_year.get()=="2019":
        owneddeals_2019=owneddeals.loc[owneddeals['Year'] == 2019]
        #print(owneddeals_2019)
        temp=owneddeals_2019["Agent"].tolist()
        #print(agents)
        temp=list(set(temp))
        agents=[]
        for i  in temp:
            name=""
            words = i.split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            agents.append(name)
        agents=list(set(agents))
        #print(agents)
        
        for i in rows:
            i=list(i)
            for j in agents:
                i[1]=str(i[1])
                name = i[1].rstrip()

                j=str(j)
                if name==j:
                    temp=[j,i[0]]
                    temp_agent.append(temp)
    elif select_year.get()=="2018":
        owneddeals_2018=owneddeals.loc[owneddeals['Year'] == 2018]
        temp=owneddeals_2018["Agent"].tolist()
        #print(agents)
        temp=list(set(temp))
        agents=[]
        for i  in temp:
            name=""
            words = i.split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            agents.append(name)
        agents=list(set(agents))
        #print(agents)
        
        for i in rows:
            i=list(i)
            for j in agents:
                i[1]=str(i[1])
                name = i[1].rstrip()

                j=str(j)
                if name==j:
                    temp=[j,i[0]]
                    temp_agent.append(temp)
    elif select_year.get()=="2017":
        owneddeals_2017=owneddeals.loc[owneddeals['Year'] == 2017]
        temp=owneddeals_2017["Agent"].tolist()
        #print(agents)
        temp=list(set(temp))
        agents=[]
        for i  in temp:
            name=""
            words = i.split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            agents.append(name)
        agents=list(set(agents))
        #print(agents)
        
        for i in rows:
            i=list(i)
            for j in agents:
                i[1]=str(i[1])
                name = i[1].rstrip()

                j=str(j)
                if name==j:
                    temp=[j,i[0]]
                    temp_agent.append(temp)
    elif select_year.get()=="2020":
        owneddeals_2020=owneddeals.loc[owneddeals['Year'] == 2020]
        temp=owneddeals_2020["Agent"].tolist()
        #print(agents)
        temp=list(set(temp))
        agents=[]
        for i  in temp:
            name=""
            words = i.split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            agents.append(name)
        agents=list(set(agents))
        #print(agents)
        
        for i in rows:
            i=list(i)
            for j in agents:
                i[1]=str(i[1])
                name = i[1].rstrip()

                j=str(j)
                if name==j:
                    temp=[j,i[0]]
                    temp_agent.append(temp)
    df_agentcode=pd.DataFrame(temp_agent,columns=['Agent Name','Agent Code'])
    agentcodewin=Toplevel()
    agentcodewin.title("Agents And Their Code")
    agentcodewin.geometry('{}x{}'.format(600, 500))
    table =Table(agentcodewin, dataframe=df_agentcode,showtoolbar=True, showstatusbar=True )
    table.currwidth = 300
    table.currheight = 400
    table.show()
    
                    
def showcitycounttable(event):
    df_dataset=pd.DataFrame()
    for f in ["Dataset.xlsx"]:
        data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
        df_dataset=df_dataset.append(data)
    
    if select_year.get()=="ALL": 
        cities=df_dataset["City"].tolist()
        temp=list(set(cities))
        count=[]
        city=[]
        cities_count_list=[]
        for i in temp:
            if type(i)==str:
                city.append(i)
                count.append(cities.count(i))
        for i in range(0,len(city)):
            cities_count_list.append([count[i],city[i]])
        cities_count_list.sort()
        cities_count_list.reverse()
        cities_count_list_1=[]
        for i in range(0,len(cities_count_list)):
            cities_count_list_1.append([cities_count_list[i][1],cities_count_list[i][0]])
    
    elif select_year.get()=="2019":
        dataset_2019=df_dataset.loc[df_dataset['Year'] == 2019]
        cities=dataset_2019["City"].tolist()
        temp=list(set(cities))
        count=[]
        city=[]
        cities_count_list=[]
        for i in temp:
            if type(i)==str:
                city.append(i)
                count.append(cities.count(i))
        for i in range(0,len(city)):
            cities_count_list.append([count[i],city[i]])
        cities_count_list.sort()
        cities_count_list.reverse()
        cities_count_list_1=[]
        for i in range(0,len(cities_count_list)):
            cities_count_list_1.append([cities_count_list[i][1],cities_count_list[i][0]])
    
    elif select_year.get()=="2018":
        dataset_2018=df_dataset.loc[df_dataset['Year'] == 2018]
        cities=dataset_2018["City"].tolist()
        temp=list(set(cities))
        count=[]
        city=[]
        cities_count_list=[]
        for i in temp:
            if type(i)==str:
                city.append(i)
                count.append(cities.count(i))
        for i in range(0,len(city)):
            cities_count_list.append([count[i],city[i]])
        cities_count_list.sort()
        cities_count_list.reverse()
        cities_count_list_1=[]
        for i in range(0,len(cities_count_list)):
            cities_count_list_1.append([cities_count_list[i][1],cities_count_list[i][0]])
    
    elif select_year.get()=="2017":
        dataset_2017=df_dataset.loc[df_dataset['Year'] == 2017]
        cities=dataset_2017["City"].tolist()
        temp=list(set(cities))
        count=[]
        city=[]
        cities_count_list=[]
        for i in temp:
            if type(i)==str:
                city.append(i)
                count.append(cities.count(i))
        for i in range(0,len(city)):
            cities_count_list.append([count[i],city[i]])
        cities_count_list.sort()
        cities_count_list.reverse()
        cities_count_list_1=[]
        for i in range(0,len(cities_count_list)):
            cities_count_list_1.append([cities_count_list[i][1],cities_count_list[i][0]])
    
    elif select_year.get()=="2020":
        dataset_2020=df_dataset.loc[df_dataset['Year'] == 2020]
        cities=dataset_2020["City"].tolist()
        temp=list(set(cities))
        count=[]
        city=[]
        cities_count_list=[]
        for i in temp:
            if type(i)==str:
                city.append(i)
                count.append(cities.count(i))
        for i in range(0,len(city)):
            cities_count_list.append([count[i],city[i]])
        cities_count_list.sort()
        cities_count_list.reverse()
        cities_count_list_1=[]
        for i in range(0,len(cities_count_list)):
            cities_count_list_1.append([cities_count_list[i][1],cities_count_list[i][0]])
    
        
    cities_count =pd.DataFrame(cities_count_list_1,columns=["City","no of deals"])  
    cities_count_win=Toplevel()
    cities_count_win.title("City And the Number of Deals")
    cities_count_win.geometry('{}x{}'.format(600, 700))
    table =Table(cities_count_win, dataframe=cities_count,showtoolbar=True, showstatusbar=True )
    table.currwidth = 300
    table.currheight = 400
    table.show()   

def make_graph():
    if select_year.get()=="ALL":
        analystframe_1=Frame(my_canvas)
        my_canvas.create_window((20,100),window=analystframe_1,anchor="nw")
        l = tk.Label(analystframe_1,width=50, text='Total property area sold vs total property are leased in Sq-M only.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_dataset=pd.DataFrame()
        for f in ["Dataset.xlsx"]:
            data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
            df_dataset=df_dataset.append(data)
    
        
        owned_area=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_area_HA=owned_area.loc[owned_area['UoM'] == 'HA']
        owned_area_SQM=owned_area.loc[owned_area['UoM'] == 'SQ-M']
        
        leased_area=df_dataset.loc[df_dataset["Tenure"]=="Leased"]
        leased_area_HA=leased_area.loc[leased_area['UoM'] == 'HA']
        leased_area_SQM=leased_area.loc[leased_area['UoM'] == 'SQ-M']
        
        totalareaowned=0
        totalarealeased=0
        temp_HA=owned_area_HA["Area"].tolist()
        
        temp_SQM=owned_area_SQM["Area"].tolist()
        
        totalareaowned=(sum(temp_HA)*10000)+sum(temp_SQM)
        
        temp_HA=leased_area_HA["Area"].tolist()
        temp_SQM=leased_area_SQM["Area"].tolist()
        totalarealeased=(sum(temp_HA)*10000)+sum(temp_SQM)
         
        totalareaowned=round(totalareaowned,3)
        totalarealeased=round(totalarealeased,3)
        list_area_owned=[totalareaowned,"Owned"]
        list_area_leased=[totalarealeased,"Leased"]
        list_area=[list_area_owned,list_area_leased]
        df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])
        
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_count= df_count[['Area','Tenure']].groupby('Tenure').sum()
        df_count.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_count["Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total area Owned Vs Total area Leased in SQ-M')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_1)
        bar1.get_tk_widget().pack()
    
        ca_property=df_dataset.loc[df_dataset['Country'] == 'CA']
        
        ca_leased_property=ca_property.loc[ca_property['Tenure'] == 'Leased']
        ca_leased_property_HA=ca_leased_property.loc[ca_leased_property['UoM'] == 'HA']
        
        ca_leased_property_SQM=ca_leased_property.loc[ca_leased_property['UoM'] == 'SQ-M']
        
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        
        area_2019=round(area_2019,3)
        temp_2018_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        
        area_2018=round(area_2018,3)
        temp_2017_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        
        area_2017=round(area_2017,3)
        temp_ca=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        
        analystframe_2=Frame(my_canvas)
        my_canvas.create_window((600,750),window=analystframe_2,anchor="nw")
        l = tk.Label(analystframe_2,width=50, text='Year that got maximum leased area in CA countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_CA_area =pd.DataFrame(temp_ca,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_CA_area= df_CA_area[['Total Area','Year']].groupby('Year').sum()
        df_CA_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_CA_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in CA (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_2)
        bar1.get_tk_widget().pack()
        max_year_ca=str(max(temp_ca)[1])
        text1="Year that got maximum leased area in CA : "+max_year_ca
        analystframe_2_1=Frame(my_canvas)
        my_canvas.create_window((600,1250),window=analystframe_2_1,anchor="nw")
        l = tk.Label(analystframe_2_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        ws_property=df_dataset.loc[df_dataset['Country'] == 'WS']
    
        ws_leased_property=ws_property.loc[ws_property['Tenure'] == 'Leased']
    
        ws_leased_property_HA=ws_leased_property.loc[ws_leased_property['UoM'] == 'HA']
        
        ws_leased_property_SQM=ws_leased_property.loc[ws_leased_property['UoM'] == 'SQ-M']
        
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        area_2019=round(area_2019,3)
        temp_2018_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        area_2018=round(area_2018,3)
        temp_2017_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        area_2017=round(area_2017,3)
        temp_ws=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        analystframe_3=Frame(my_canvas)
        my_canvas.create_window((20,750),window=analystframe_3,anchor="nw")
        l = tk.Label(analystframe_3,width=50, text='Year that got maximum leased area in WS countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_WS_area =pd.DataFrame(temp_ws,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_WS_area= df_WS_area[['Total Area','Year']].groupby('Year').sum()
        df_WS_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_WS_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in WS (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_3)
        bar1.get_tk_widget().pack()
        max_year_ws=str(max(temp_ws)[1])
        text1="Year that got maximum leased area in WS : "+max_year_ws
        analystframe_3_1=Frame(my_canvas)
        my_canvas.create_window((20,1250),window=analystframe_3_1,anchor="nw")
        l = tk.Label(analystframe_3_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        #print(temp_ca)
        #print(temp_ws)
        find_max_year=[]
        for i in range(0,len(temp_ca)):
            total=temp_ca[i][0]+temp_ws[i][0]
            find_max_year.append([total,temp_ca[i][1]])
        max_year=str(max(find_max_year)[1])
        text1="Year that got maximum leased area in both CA and WS countries : "+max_year
        analystframe_3_2=Frame(my_canvas)
        my_canvas.create_window((80,1280),window=analystframe_3_2,anchor="nw")
        l = tk.Label(analystframe_3_2,width=80, text=text1,font=('arial', 12))
        l.pack()
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((10,1350),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=70, text='The Agent codes of all the agents who have got deals in ‘OWNED’ categories:',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        Agents_bu=tk.Button(analystframe_5,text="click here")
        Agents_bu.pack()
        Agents_bu.bind("<Button-1>",showagenttable)
        
        leasedproperty=df_dataset.loc[df_dataset['Tenure'] == 'Leased']
        chillwack_leasedproperty=leasedproperty.loc[leasedproperty['City'] == 'Chilliwack']
        #print(chillwack_leasedproperty)
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select AGENT_NAME from agents"
            cur.execute(sql)
            list_agents=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        chillwack_agents=chillwack_leasedproperty["Agent"].tolist()
        #print(chillwack_agents)
        #print(list_agents)
        deals=[]
        max1=0
        for i in list_agents:
            name=""
            words = i[0].split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            count=chillwack_agents.count(name)
            #print(count)
            if count > max1:
                max1=count
                max_name=name
            temp=[name,count]
            deals.append(temp)
        analystframe_4=Frame(my_canvas)
        my_canvas.create_window((600,100),window=analystframe_4,anchor="nw")    
        l = tk.Label(analystframe_4,width=50, text='For the city of chillwack, agent hs got the maximum leased deals:-',fg="blue",font=('arial', 12))
        l.pack()
        temp_df=pd.DataFrame(deals,columns=['Agent Name','Deals'])
        figure3 = plt.Figure(figsize=(6,7), dpi=80)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(temp_df['Agent Name'],temp_df['Deals'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3,analystframe_4 ) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(["Leased Deals"]) 
        ax3.set_xlabel('Agent Name')
        ax3.set_xticklabels(temp_df['Agent Name'],rotation=45)
        ax3.set_title('No. of deals done by agents on leased form in city of Chilliwack')
        text1="agent which has got the maximum deals in leased form: "+max_name
        analystframe_4_1=Frame(my_canvas)
        my_canvas.create_window((600,680),window=analystframe_4_1,anchor="nw")
        l = tk.Label(analystframe_4_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        #print(df_dataset)
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals["Agent"].replace(dict, inplace=True)
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        agents=[]
        for i in listagents:
            if type(i)==str:
                agents.append(i)
        #print(agents)
        all_owneddeals=all_deals.loc[all_deals["Tenure"]=="Owned"]
        all_owneddeals_HA=all_owneddeals.loc[all_owneddeals['UoM'] == 'HA']
        all_owneddeals_SQM=all_owneddeals.loc[all_owneddeals['UoM'] == 'SQ-M']
        all_leaseddeals=all_deals.loc[all_deals["Tenure"]=="Leased"]
        all_leaseddeals_HA=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'HA']
        all_leaseddeals_SQM=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'SQ-M']
        
        agents_owned_area=[]
        agents_leased_area=[]
        for i in agents:
            temp_ha=(all_owneddeals_HA[(all_owneddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_owneddeals_SQM[(all_owneddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            
            totalarea=round(totalarea,3)
            agents_owned_area.append(totalarea)
        for i in agents:
            temp_ha=(all_leaseddeals_HA[(all_leaseddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_leaseddeals_SQM[(all_leaseddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            totalarea=round(totalarea,3)
            agents_leased_area.append(totalarea)
        agent_area=[] 
        find_max=[]
        for i in range(0,len(agents)):
            temp=[agents[i],agents_owned_area[i],agents_leased_area[i]]
            find_max.append([agents_owned_area[i]+agents_leased_area[i],agents[i]])
            agent_area.append(temp)
        #print(max(find_max))
        max_agent=max(find_max)[1]
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((20,1400),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=90, text='The performance of all agents based on the area leased and owned for the years 2017,2018 and 2019:-',fg="blue",font=('arial', 12))
        l.pack()
        df_agent_own_lease =pd.DataFrame(agent_area,columns=['Agent','Total Owned Area',"Total Leased Area"])
        #print(df_agent_own_lease)
        figure1 = Figure(figsize=(12,8), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_agent_own_lease = df_agent_own_lease [['Agent','Total Owned Area',"Total Leased Area"]].groupby('Agent').sum()
        df_agent_own_lease.plot(kind='bar', legend=True, ax=ax1,width=1)
        for i, v in enumerate(df_agent_own_lease["Total Owned Area"]):
            ax1.text(i- 0.75, v+3, str(v),color ="blue")
        for i, v in enumerate(df_agent_own_lease["Total Leased Area"]):
            ax1.text(i, v+3, str(v),color ="red")
        
        ax1.set_title('Performance of each agent for years 2017,18,19 (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_5)
        bar1.get_tk_widget().pack()
        text1="Agent who has been the best performer is "+max_agent
        analystframe_5_1=Frame(my_canvas)
        my_canvas.create_window((20,2100),window=analystframe_5_1,anchor="nw")
        l = tk.Label(analystframe_5_1,width=90, text=text1,font=('arial', 12))
        l.pack()
        
        
        owned_property=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_Jul_property=owned_property.loc[owned_property["Month"]=="JUL"]
        owned_Jul_property_HA=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'HA']
        owned_Jul_property_SQM=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'SQ-M']
        years=list(set(owned_Jul_property["Year"].tolist()))
        #print(years)
        total_area=[]
        for i in years:
            temp_ha=(owned_Jul_property_HA[(owned_Jul_property_HA.Year==i)].Area).tolist()
            temp_sqm=(owned_Jul_property_SQM[(owned_Jul_property_SQM.Year==i)].Area).tolist()
            area=(sum(temp_ha)*10000)+sum(temp_sqm)
            area=round(area,3)
            total_area.append(area)
        temp_list=[]
        add=0
        for i in range(0,len(years)):
            temp=[years[i],total_area[i]]
            add=add+total_area[i]
            temp_list.append(temp)
        temp_list.append(["Total",add])
        #print(temp_list)
        analystframe_6=Frame(my_canvas)
        my_canvas.create_window((20,2180),window=analystframe_6,anchor="nw")
        l = tk.Label(analystframe_6,width=50, text='Amount of property area sold for the month of july for all the years.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_owned_year =pd.DataFrame(temp_list,columns=['Year','Total Owned Area'])

        figure1 = Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_owned_year= df_owned_year[['Year','Total Owned Area']].groupby('Year').sum()
        df_owned_year.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_owned_year["Total Owned Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('amount of property area sold for the month of july for all the years (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_6)
        bar1.get_tk_widget().pack()
 

        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            query="select ORD_DATE from orders"
            cur.execute(query)
            row=list(cur.fetchall())
        except:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        temp_list=[]
        my_time=datetime.min.time()
        for i in range(0,len(row)):
            row[i]=list(row[i])
            row[i][0]=datetime.combine(row[i][0],my_time)
            temp_list.append(1)
        dataframe_orders =pd.DataFrame(row,columns=["Order Date"])
    
        dataframe_orders["number of deals"]=temp_list
        
        #print(dataframe_orders["Order Date"].min())
        #print(dataframe_orders["Order Date"].max())
        dataframe_orders=dataframe_orders.sort_values('Order Date')
        #print(dataframe_orders.sort_values('Order Date'))
        dataframe_orders=dataframe_orders.groupby('Order Date')["number of deals"].sum().reset_index()
        dataframe_orders=dataframe_orders.set_index('Order Date')
        #print(dataframe_orders)
        df_y = dataframe_orders['number of deals'].resample('MS').sum()
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,2750),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (database).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(15,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_y.plot(legend=True, ax=ax1,figsize=(15,6))
        ax1.set_title('Time series analysis report of the orders received')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
        
        years=df_dataset["Year"].tolist()
        for i in years:
            if type(i)==str:
                years.remove(i)
        temp=list(set(years))
        count=[]
        year=[]
        for i in temp:
            count.append(years.count(i))
            year.append(str(i))
            
        
        dataframe_orders_ds=pd.DataFrame(year,columns=["Year"])
        dataframe_orders_ds["number of deals"]=count
        
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,3300),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (dataset-Excel).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        dataframe_orders_ds=dataframe_orders_ds.groupby('Year')["number of deals"].sum().reset_index()
        dataframe_orders_ds=dataframe_orders_ds.set_index('Year')
        dataframe_orders_ds.plot(legend=True, ax=ax1,figsize=(6,6))
        ax1.set_title('Time series analysis report of the orders received (dataset)')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
        
        
        analystframe_9=Frame(my_canvas)
        my_canvas.create_window((600,3300),window=analystframe_9,anchor="nw")
        l = tk.Label(analystframe_9,width=40, text='City and the number of deals done for that city',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        City_bu=tk.Button(analystframe_9,text="click here")
        City_bu.pack()
        City_bu.bind("<Button-1>",showcitycounttable)
        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select OPENING_AMT,PAYMENT_AMT from customer"
            cur.execute(sql)
            list_amts=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        count=0
        for i in list_amts:
            if i[0]>=i[1]:
                count=count+1
        
        temp_count=len(list_amts)-count
        lab=["Opening Amount >= Payment Amount ","Payment Amount > Opening Amount"]
        per=[count,temp_count]
        analystframe_10=Frame(my_canvas)
        my_canvas.create_window((600,3400),window=analystframe_10,anchor="nw")
        l = tk.Label(analystframe_10,width=50, text='Percentage of Opening Amount >= Payment Amount:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        ax1.pie(per, radius=1, labels=lab,autopct='%0.2f%%', shadow=True,)
        pie1 = FigureCanvasTkAgg(figure1,analystframe_10)
        pie1.get_tk_widget().pack()
        
    elif select_year.get()=="2019":
        analystframe_1=Frame(my_canvas)
        my_canvas.create_window((20,100),window=analystframe_1,anchor="nw")
        l = tk.Label(analystframe_1,width=50, text='Total property area sold vs total property are leased in Sq-M only.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_dataset=pd.DataFrame()
        for f in ["Dataset.xlsx"]:
            data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
            df_dataset=df_dataset.append(data)
    
        
        
        sqm_property_2019=df_dataset.loc[df_dataset['Year'] == 2019]
       # print(sqm_property_2019)
        owned_area=sqm_property_2019.loc[sqm_property_2019["Tenure"]=="Owned"]
        leased_area=sqm_property_2019.loc[sqm_property_2019["Tenure"]=="Leased"]
        owned_area_HA=owned_area.loc[owned_area['UoM'] == 'HA']
        owned_area_SQM=owned_area.loc[owned_area['UoM'] == 'SQ-M']
        leased_area_HA=leased_area.loc[leased_area['UoM'] == 'HA']
        leased_area_SQM=leased_area.loc[leased_area['UoM'] == 'SQ-M']
        totalareaowned=0
        totalarealeased=0
        temp_HA=owned_area_HA["Area"].tolist()
        temp_SQM=owned_area_SQM["Area"].tolist()
        totalareaowned=(sum(temp_HA)*10000)+sum(temp_SQM)
        
        temp_HA=leased_area_HA["Area"].tolist()
        temp_SQM=leased_area_SQM["Area"].tolist()
        totalarealeased=(sum(temp_HA)*10000)+sum(temp_SQM)
         
        totalareaowned=round(totalareaowned,3)
        totalarealeased=round(totalarealeased,3)
        list_area_owned=[totalareaowned,"Owned"]
        list_area_leased=[totalarealeased,"Leased"]
        list_area=[list_area_owned,list_area_leased]
        df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])
        
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_count= df_count[['Area','Tenure']].groupby('Tenure').sum()
        df_count.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_count["Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total area Owned Vs Total area Leased in SQ-M')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_1)
        bar1.get_tk_widget().pack()
    
        ca_property=df_dataset.loc[df_dataset['Country'] == 'CA']
        
        ca_leased_property=ca_property.loc[ca_property['Tenure'] == 'Leased']
        ca_leased_property_HA=ca_leased_property.loc[ca_leased_property['UoM'] == 'HA']
        ca_leased_property_SQM=ca_leased_property.loc[ca_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        
        area_2019=round(area_2019,3)
        temp_2018_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        
        area_2018=round(area_2018,3)
        temp_2017_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        
        area_2017=round(area_2017,3)
        temp_ca=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        
        analystframe_2=Frame(my_canvas)
        my_canvas.create_window((600,750),window=analystframe_2,anchor="nw")
        l = tk.Label(analystframe_2,width=50, text='Year that got maximum leased area in CA countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_CA_area =pd.DataFrame(temp_ca,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_CA_area= df_CA_area[['Total Area','Year']].groupby('Year').sum()
        df_CA_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_CA_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in CA (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_2)
        bar1.get_tk_widget().pack()
        max_year_ca=str(max(temp_ca)[1])
        text1="Year that got maximum leased area in CA : "+max_year_ca
        analystframe_2_1=Frame(my_canvas)
        my_canvas.create_window((600,1250),window=analystframe_2_1,anchor="nw")
        l = tk.Label(analystframe_2_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        ws_property=df_dataset.loc[df_dataset['Country'] == 'WS']
    
        ws_leased_property=ws_property.loc[ws_property['Tenure'] == 'Leased']
    
        ws_leased_property_HA=ws_leased_property.loc[ws_leased_property['UoM'] == 'HA']
        ws_leased_property_SQM=ws_leased_property.loc[ws_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        area_2019=round(area_2019,3)
        temp_2018_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        area_2018=round(area_2018,3)
        temp_2017_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        area_2017=round(area_2017,3)
        temp_ws=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        analystframe_3=Frame(my_canvas)
        my_canvas.create_window((20,750),window=analystframe_3,anchor="nw")
        l = tk.Label(analystframe_3,width=50, text='Year that got maximum leased area in WS countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_WS_area =pd.DataFrame(temp_ws,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_WS_area= df_WS_area[['Total Area','Year']].groupby('Year').sum()
        df_WS_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_WS_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in WS (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_3)
        bar1.get_tk_widget().pack()
        max_year_ws=str(max(temp_ws)[1])
        text1="Year that got maximum leased area in WS : "+max_year_ws
        analystframe_3_1=Frame(my_canvas)
        my_canvas.create_window((20,1250),window=analystframe_3_1,anchor="nw")
        l = tk.Label(analystframe_3_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        #print(temp_ca)
        #print(temp_ws)
        find_max_year=[]
        for i in range(0,len(temp_ca)):
            total=temp_ca[i][0]+temp_ws[i][0]
            find_max_year.append([total,temp_ca[i][1]])
        max_year=str(max(find_max_year)[1])
        text1="Year that got maximum leased area in both CA and WS countries : "+max_year
        analystframe_3_2=Frame(my_canvas)
        my_canvas.create_window((80,1280),window=analystframe_3_2,anchor="nw")
        l = tk.Label(analystframe_3_2,width=80, text=text1,font=('arial', 12))
        l.pack()
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((10,1350),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=70, text='The Agent codes of all the agents who have got deals in ‘OWNED’ categories:',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        Agents_bu=tk.Button(analystframe_5,text="click here")
        Agents_bu.pack()
        Agents_bu.bind("<Button-1>",showagenttable)
        
        leasedproperty=df_dataset.loc[df_dataset['Tenure'] == 'Leased']
        chillwack_leasedproperty=leasedproperty.loc[leasedproperty['City'] == 'Chilliwack']
        chillwack_leasedproperty_2019=chillwack_leasedproperty.loc[chillwack_leasedproperty['Year'] == 2019]
        #print(chillwack_leasedproperty_2019)
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select AGENT_NAME from agents"
            cur.execute(sql)
            list_agents=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        chillwack_agents=chillwack_leasedproperty_2019["Agent"].tolist()
       # print(chillwack_agents)
        #print(list_agents)
        deals=[]
        max1=0
        for i in list_agents:
            name=""
            words = i[0].split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            count=chillwack_agents.count(name)
            #print(count)
            if count > max1:
                max1=count
                max_name=name
            temp=[name,count]
            deals.append(temp)
        analystframe_4=Frame(my_canvas)
        my_canvas.create_window((600,100),window=analystframe_4,anchor="nw")    
        l = tk.Label(analystframe_4,width=50, text='For the city of chillwack, agent hs got the maximum leased deals:-',fg="blue",font=('arial', 12))
        l.pack()
        temp_df=pd.DataFrame(deals,columns=['Agent Name','Deals'])
        figure3 = plt.Figure(figsize=(6,7), dpi=80)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(temp_df['Agent Name'],temp_df['Deals'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3,analystframe_4 ) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(["Leased Deals"]) 
        ax3.set_xlabel('Agent Name')
        ax3.set_xticklabels(temp_df['Agent Name'],rotation=45)
        ax3.set_title('No. of deals done by agents on leased form in city of Chilliwack')
        text1="agent which has got the maximum deals in leased form: "+max_name
        analystframe_4_1=Frame(my_canvas)
        my_canvas.create_window((600,680),window=analystframe_4_1,anchor="nw")
        l = tk.Label(analystframe_4_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals["Agent"].replace(dict, inplace=True)
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        agents=[]
        for i in listagents:
            if type(i)==str:
                agents.append(i)
        #print(agents)
        all_owneddeals=all_deals.loc[all_deals["Tenure"]=="Owned"]
        all_owneddeals_HA=all_owneddeals.loc[all_owneddeals['UoM'] == 'HA']
        all_owneddeals_SQM=all_owneddeals.loc[all_owneddeals['UoM'] == 'SQ-M']
        all_leaseddeals=all_deals.loc[all_deals["Tenure"]=="Leased"]
        all_leaseddeals_HA=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'HA']
        all_leaseddeals_SQM=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'SQ-M']
        
        agents_owned_area=[]
        agents_leased_area=[]
        for i in agents:
            temp_ha=(all_owneddeals_HA[(all_owneddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_owneddeals_SQM[(all_owneddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            
            totalarea=round(totalarea,3)
            agents_owned_area.append(totalarea)
        for i in agents:
            temp_ha=(all_leaseddeals_HA[(all_leaseddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_leaseddeals_SQM[(all_leaseddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            totalarea=round(totalarea,3)
            agents_leased_area.append(totalarea)
        agent_area=[] 
        find_max=[]
        for i in range(0,len(agents)):
            temp=[agents[i],agents_owned_area[i],agents_leased_area[i]]
            find_max.append([agents_owned_area[i]+agents_leased_area[i],agents[i]])
            agent_area.append(temp)
        #print(max(find_max))
        max_agent=max(find_max)[1]
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((20,1400),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=90, text='The performance of all agents based on the area leased and owned for the years 2017,2018 and 2019:-',fg="blue",font=('arial', 12))
        l.pack()
        df_agent_own_lease =pd.DataFrame(agent_area,columns=['Agent','Total Owned Area',"Total Leased Area"])
        #print(df_agent_own_lease)
        figure1 = Figure(figsize=(12,8), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_agent_own_lease = df_agent_own_lease [['Agent','Total Owned Area',"Total Leased Area"]].groupby('Agent').sum()
        df_agent_own_lease.plot(kind='bar', legend=True, ax=ax1,width=1)
        for i, v in enumerate(df_agent_own_lease["Total Owned Area"]):
            ax1.text(i- 0.75, v+3, str(v),color ="blue")
        for i, v in enumerate(df_agent_own_lease["Total Leased Area"]):
            ax1.text(i, v+3, str(v),color ="red")
        
        ax1.set_title('Performance of each agent for years 2017,18,19 (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_5)
        bar1.get_tk_widget().pack()
        text1="Agent who has been the best performer is "+max_agent
        analystframe_5_1=Frame(my_canvas)
        my_canvas.create_window((20,2100),window=analystframe_5_1,anchor="nw")
        l = tk.Label(analystframe_5_1,width=90, text=text1,font=('arial', 12))
        l.pack()
        
        
        owned_property=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_Jul_property=owned_property.loc[owned_property["Month"]=="JUL"]
        owned_Jul_property_HA=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'HA']
        owned_Jul_property_SQM=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'SQ-M']
        years=list(set(owned_Jul_property["Year"].tolist()))
        #print(years)
        total_area=[]
        for i in years:
            temp_ha=(owned_Jul_property_HA[(owned_Jul_property_HA.Year==i)].Area).tolist()
            temp_sqm=(owned_Jul_property_SQM[(owned_Jul_property_SQM.Year==i)].Area).tolist()
            area=(sum(temp_ha)*10000)+sum(temp_sqm)
            area=round(area,3)
            total_area.append(area)
        temp_list=[]
        add=0
        for i in range(0,len(years)):
            temp=[years[i],total_area[i]]
            add=add+total_area[i]
            temp_list.append(temp)
        temp_list.append(["Total",add])
        #print(temp_list)
        analystframe_6=Frame(my_canvas)
        my_canvas.create_window((20,2180),window=analystframe_6,anchor="nw")
        l = tk.Label(analystframe_6,width=50, text='Amount of property area sold for the month of july for all the years.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_owned_year =pd.DataFrame(temp_list,columns=['Year','Total Owned Area'])

        figure1 = Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_owned_year= df_owned_year[['Year','Total Owned Area']].groupby('Year').sum()
        df_owned_year.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_owned_year["Total Owned Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('amount of property area sold for the month of july for all the years (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_6)
        bar1.get_tk_widget().pack()

        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            query="select ORD_DATE from orders"
            cur.execute(query)
            row=list(cur.fetchall())
        except:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        temp_list=[]
        my_time=datetime.min.time()
        for i in range(0,len(row)):
            row[i]=list(row[i])
            row[i][0]=datetime.combine(row[i][0],my_time)
            temp_list.append(1)
        rand_date=[datetime.strptime("2017-10-1",'%Y-%m-%d')]
        row.append(rand_date)
        dataframe_orders =pd.DataFrame(row,columns=["Order Date"])
        temp_list.append(0)
        dataframe_orders["number of deals"]=temp_list
        
        
       # print(dataframe_orders)
        #print(dataframe_orders["Order Date"].min())
        #print(dataframe_orders["Order Date"].max())
        dataframe_orders=dataframe_orders.sort_values('Order Date')
        #print(dataframe_orders.sort_values('Order Date'))
        dataframe_orders=dataframe_orders.groupby('Order Date')["number of deals"].sum().reset_index()
        dataframe_orders=dataframe_orders.set_index('Order Date')
        #print(dataframe_orders)
        df_y = dataframe_orders['number of deals'].resample('MS').sum()
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,2750),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received.:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(15,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_y.plot(legend=True, ax=ax1,figsize=(15,6))
        ax1.set_title('Time series analysis report of the orders received')
        
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
    
        years=df_dataset["Year"].tolist()
        for i in years:
            if type(i)==str:
                years.remove(i)
        temp=list(set(years))
        count=[]
        year=[]
        for i in temp:
            count.append(years.count(i))
            year.append(str(i))
            
        
        dataframe_orders_ds=pd.DataFrame(year,columns=["Year"])
        dataframe_orders_ds["number of deals"]=count
        
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,3300),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (dataset-Excel).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        dataframe_orders_ds=dataframe_orders_ds.groupby('Year')["number of deals"].sum().reset_index()
        dataframe_orders_ds=dataframe_orders_ds.set_index('Year')
        dataframe_orders_ds.plot(legend=True, ax=ax1,figsize=(6,6))
        ax1.set_title('Time series analysis report of the orders received (dataset)')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
        
        analystframe_9=Frame(my_canvas)
        my_canvas.create_window((600,3300),window=analystframe_9,anchor="nw")
        l = tk.Label(analystframe_9,width=40, text='City and the number of deals done for that city',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        City_bu=tk.Button(analystframe_9,text="click here")
        City_bu.pack()
        City_bu.bind("<Button-1>",showcitycounttable)
        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select OPENING_AMT,PAYMENT_AMT from customer"
            cur.execute(sql)
            list_amts=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        count=0
        for i in list_amts:
            if i[0]>=i[1]:
                count=count+1
        
        temp_count=len(list_amts)-count
        lab=["Opening Amount >= Payment Amount ","Payment Amount > Opening Amount"]
        per=[count,temp_count]
        analystframe_10=Frame(my_canvas)
        my_canvas.create_window((600,3400),window=analystframe_10,anchor="nw")
        l = tk.Label(analystframe_10,width=50, text='Percentage of Opening Amount >= Payment Amount:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        ax1.pie(per, radius=1, labels=lab,autopct='%0.2f%%', shadow=True,)
        pie1 = FigureCanvasTkAgg(figure1,analystframe_10)
        pie1.get_tk_widget().pack()  
        
    elif select_year.get()=="2018":
        analystframe_1=Frame(my_canvas)
        my_canvas.create_window((20,100),window=analystframe_1,anchor="nw")
        l = tk.Label(analystframe_1,width=50, text='Total property area sold vs total property are leased in Sq-M only.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_dataset=pd.DataFrame()
        for f in ["Dataset.xlsx"]:
            data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
            df_dataset=df_dataset.append(data)
    
        sqm_property_2018=df_dataset.loc[df_dataset['Year'] == 2018]
        
        owned_area=sqm_property_2018.loc[sqm_property_2018["Tenure"]=="Owned"]
        leased_area=sqm_property_2018.loc[sqm_property_2018["Tenure"]=="Leased"]
        
        owned_area_HA=owned_area.loc[owned_area['UoM'] == 'HA']
        owned_area_SQM=owned_area.loc[owned_area['UoM'] == 'SQ-M']
        leased_area_HA=leased_area.loc[leased_area['UoM'] == 'HA']
        leased_area_SQM=leased_area.loc[leased_area['UoM'] == 'SQ-M']
        totalareaowned=0
        totalarealeased=0
        temp_HA=owned_area_HA["Area"].tolist()
        temp_SQM=owned_area_SQM["Area"].tolist()
        totalareaowned=(sum(temp_HA)*10000)+sum(temp_SQM)
        
        temp_HA=leased_area_HA["Area"].tolist()
        temp_SQM=leased_area_SQM["Area"].tolist()
        totalarealeased=(sum(temp_HA)*10000)+sum(temp_SQM)
         
        totalareaowned=round(totalareaowned,3)
        totalarealeased=round(totalarealeased,3)
        list_area_owned=[totalareaowned,"Owned"]
        list_area_leased=[totalarealeased,"Leased"]
        list_area=[list_area_owned,list_area_leased]
        df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])
        
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_count= df_count[['Area','Tenure']].groupby('Tenure').sum()
        df_count.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_count["Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total area Owned Vs Total area Leased in SQ-M')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_1)
        bar1.get_tk_widget().pack()
    
        ca_property=df_dataset.loc[df_dataset['Country'] == 'CA']
        
        ca_leased_property=ca_property.loc[ca_property['Tenure'] == 'Leased']
        ca_leased_property_HA=ca_leased_property.loc[ca_leased_property['UoM'] == 'HA']
        ca_leased_property_SQM=ca_leased_property.loc[ca_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        
        area_2019=round(area_2019,3)
        temp_2018_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        
        area_2018=round(area_2018,3)
        temp_2017_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        
        area_2017=round(area_2017,3)
        temp_ca=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        
        analystframe_2=Frame(my_canvas)
        my_canvas.create_window((600,750),window=analystframe_2,anchor="nw")
        l = tk.Label(analystframe_2,width=50, text='Year that got maximum leased area in CA countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_CA_area =pd.DataFrame(temp_ca,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_CA_area= df_CA_area[['Total Area','Year']].groupby('Year').sum()
        df_CA_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_CA_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in CA (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_2)
        bar1.get_tk_widget().pack()
        max_year_ca=str(max(temp_ca)[1])
        text1="Year that got maximum leased area in CA : "+max_year_ca
        analystframe_2_1=Frame(my_canvas)
        my_canvas.create_window((600,1250),window=analystframe_2_1,anchor="nw")
        l = tk.Label(analystframe_2_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        ws_property=df_dataset.loc[df_dataset['Country'] == 'WS']
    
        ws_leased_property=ws_property.loc[ws_property['Tenure'] == 'Leased']
    
        ws_leased_property_HA=ws_leased_property.loc[ws_leased_property['UoM'] == 'HA']
        ws_leased_property_SQM=ws_leased_property.loc[ws_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        area_2019=round(area_2019,3)
        temp_2018_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        area_2018=round(area_2018,3)
        temp_2017_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        area_2017=round(area_2017,3)
        temp_ws=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        analystframe_3=Frame(my_canvas)
        my_canvas.create_window((20,750),window=analystframe_3,anchor="nw")
        l = tk.Label(analystframe_3,width=50, text='Year that got maximum leased area in WS countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_WS_area =pd.DataFrame(temp_ws,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_WS_area= df_WS_area[['Total Area','Year']].groupby('Year').sum()
        df_WS_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_WS_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in WS (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_3)
        bar1.get_tk_widget().pack()
        max_year_ws=str(max(temp_ws)[1])
        text1="Year that got maximum leased area in WS : "+max_year_ws
        analystframe_3_1=Frame(my_canvas)
        my_canvas.create_window((20,1250),window=analystframe_3_1,anchor="nw")
        l = tk.Label(analystframe_3_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        #print(temp_ca)
        #print(temp_ws)
        find_max_year=[]
        for i in range(0,len(temp_ca)):
            total=temp_ca[i][0]+temp_ws[i][0]
            find_max_year.append([total,temp_ca[i][1]])
        max_year=str(max(find_max_year)[1])
        text1="Year that got maximum leased area in both CA and WS countries : "+max_year
        analystframe_3_2=Frame(my_canvas)
        my_canvas.create_window((80,1280),window=analystframe_3_2,anchor="nw")
        l = tk.Label(analystframe_3_2,width=80, text=text1,font=('arial', 12))
        l.pack()
        
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((10,1350),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=70, text='The Agent codes of all the agents who have got deals in ‘OWNED’ categories:',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        Agents_bu=tk.Button(analystframe_5,text="click here")
        Agents_bu.pack()
        Agents_bu.bind("<Button-1>",showagenttable)
        
        leasedproperty=df_dataset.loc[df_dataset['Tenure'] == 'Leased']
        chillwack_leasedproperty=leasedproperty.loc[leasedproperty['City'] == 'Chilliwack']
        chillwack_leasedproperty_2018=chillwack_leasedproperty.loc[chillwack_leasedproperty['Year'] == 2018]
        #print(chillwack_leasedproperty_2019)
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select AGENT_NAME from agents"
            cur.execute(sql)
            list_agents=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        chillwack_agents=chillwack_leasedproperty_2018["Agent"].tolist()
        #print(chillwack_agents)
        #print(list_agents)
        deals=[]
        max1=0
        for i in list_agents:
            name=""
            words = i[0].split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            count=chillwack_agents.count(name)
            #print(count)
            if count > max1:
                max1=count
                max_name=name
            temp=[name,count]
            deals.append(temp)
        analystframe_4=Frame(my_canvas)
        my_canvas.create_window((600,100),window=analystframe_4,anchor="nw")    
        l = tk.Label(analystframe_4,width=50, text='For the city of chillwack, agent hs got the maximum leased deals:-',fg="blue",font=('arial', 12))
        l.pack()
        temp_df=pd.DataFrame(deals,columns=['Agent Name','Deals'])
        figure3 = plt.Figure(figsize=(6,7), dpi=80)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(temp_df['Agent Name'],temp_df['Deals'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3,analystframe_4 ) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(["Leased Deals"]) 
        ax3.set_xlabel('Agent Name')
        ax3.set_xticklabels(temp_df['Agent Name'],rotation=45)
        ax3.set_title('No. of deals done by agents on leased form in city of Chilliwack')
        text1="agent which has got the maximum deals in leased form: "+max_name
        analystframe_4_1=Frame(my_canvas)
        my_canvas.create_window((600,680),window=analystframe_4_1,anchor="nw")
        l = tk.Label(analystframe_4_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals["Agent"].replace(dict, inplace=True)
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        agents=[]
        for i in listagents:
            if type(i)==str:
                agents.append(i)
        #print(agents)
        all_owneddeals=all_deals.loc[all_deals["Tenure"]=="Owned"]
        all_owneddeals_HA=all_owneddeals.loc[all_owneddeals['UoM'] == 'HA']
        all_owneddeals_SQM=all_owneddeals.loc[all_owneddeals['UoM'] == 'SQ-M']
        all_leaseddeals=all_deals.loc[all_deals["Tenure"]=="Leased"]
        all_leaseddeals_HA=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'HA']
        all_leaseddeals_SQM=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'SQ-M']
        
        agents_owned_area=[]
        agents_leased_area=[]
        for i in agents:
            temp_ha=(all_owneddeals_HA[(all_owneddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_owneddeals_SQM[(all_owneddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            
            totalarea=round(totalarea,3)
            agents_owned_area.append(totalarea)
        for i in agents:
            temp_ha=(all_leaseddeals_HA[(all_leaseddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_leaseddeals_SQM[(all_leaseddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            totalarea=round(totalarea,3)
            agents_leased_area.append(totalarea)
        agent_area=[] 
        find_max=[]
        for i in range(0,len(agents)):
            temp=[agents[i],agents_owned_area[i],agents_leased_area[i]]
            find_max.append([agents_owned_area[i]+agents_leased_area[i],agents[i]])
            agent_area.append(temp)
        #print(max(find_max))
        max_agent=max(find_max)[1]
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((20,1400),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=90, text='The performance of all agents based on the area leased and owned for the years 2017,2018 and 2019:-',fg="blue",font=('arial', 12))
        l.pack()
        df_agent_own_lease =pd.DataFrame(agent_area,columns=['Agent','Total Owned Area',"Total Leased Area"])
        #print(df_agent_own_lease)
        figure1 = Figure(figsize=(12,8), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_agent_own_lease = df_agent_own_lease [['Agent','Total Owned Area',"Total Leased Area"]].groupby('Agent').sum()
        df_agent_own_lease.plot(kind='bar', legend=True, ax=ax1,width=1)
        for i, v in enumerate(df_agent_own_lease["Total Owned Area"]):
            ax1.text(i- 0.75, v+3, str(v),color ="blue")
        for i, v in enumerate(df_agent_own_lease["Total Leased Area"]):
            ax1.text(i, v+3, str(v),color ="red")
        
        ax1.set_title('Performance of each agent for years 2017,18,19 (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_5)
        bar1.get_tk_widget().pack()
        text1="Agent who has been the best performer is "+max_agent
        analystframe_5_1=Frame(my_canvas)
        my_canvas.create_window((20,2100),window=analystframe_5_1,anchor="nw")
        l = tk.Label(analystframe_5_1,width=90, text=text1,font=('arial', 12))
        l.pack()
        
        
        owned_property=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_Jul_property=owned_property.loc[owned_property["Month"]=="JUL"]
        owned_Jul_property_HA=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'HA']
        owned_Jul_property_SQM=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'SQ-M']
        years=list(set(owned_Jul_property["Year"].tolist()))
        #print(years)
        total_area=[]
        for i in years:
            temp_ha=(owned_Jul_property_HA[(owned_Jul_property_HA.Year==i)].Area).tolist()
            temp_sqm=(owned_Jul_property_SQM[(owned_Jul_property_SQM.Year==i)].Area).tolist()
            area=(sum(temp_ha)*10000)+sum(temp_sqm)
            area=round(area,3)
            total_area.append(area)
        temp_list=[]
        add=0
        for i in range(0,len(years)):
            temp=[years[i],total_area[i]]
            add=add+total_area[i]
            temp_list.append(temp)
        temp_list.append(["Total",add])
        #print(temp_list)
        analystframe_6=Frame(my_canvas)
        my_canvas.create_window((20,2180),window=analystframe_6,anchor="nw")
        l = tk.Label(analystframe_6,width=50, text='Amount of property area sold for the month of july for all the years.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_owned_year =pd.DataFrame(temp_list,columns=['Year','Total Owned Area'])

        figure1 = Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_owned_year= df_owned_year[['Year','Total Owned Area']].groupby('Year').sum()
        df_owned_year.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_owned_year["Total Owned Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('amount of property area sold for the month of july for all the years (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_6)
        bar1.get_tk_widget().pack()

        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            query="select ORD_DATE from orders"
            cur.execute(query)
            row=list(cur.fetchall())
        except:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        temp_list=[]
        my_time=datetime.min.time()
        for i in range(0,len(row)):
            row[i]=list(row[i])
            row[i][0]=datetime.combine(row[i][0],my_time)
            temp_list.append(1)
        dataframe_orders =pd.DataFrame(row,columns=["Order Date"])
    
        dataframe_orders["number of deals"]=temp_list
        
        #print(dataframe_orders["Order Date"].min())
        #print(dataframe_orders["Order Date"].max())
        dataframe_orders=dataframe_orders.sort_values('Order Date')
        #print(dataframe_orders.sort_values('Order Date'))
        dataframe_orders=dataframe_orders.groupby('Order Date')["number of deals"].sum().reset_index()
        dataframe_orders=dataframe_orders.set_index('Order Date')
        #print(dataframe_orders)
        df_y = dataframe_orders['number of deals'].resample('MS').sum()
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,2750),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received.:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(15,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_y.plot(legend=True, ax=ax1,figsize=(15,6))
        ax1.set_title('Time series analysis report of the orders received')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()

        years=df_dataset["Year"].tolist()
        for i in years:
            if type(i)==str:
                years.remove(i)
        temp=list(set(years))
        count=[]
        year=[]
        for i in temp:
            count.append(years.count(i))
            year.append(str(i))
            
        
        dataframe_orders_ds=pd.DataFrame(year,columns=["Year"])
        dataframe_orders_ds["number of deals"]=count
        
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,3300),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (dataset-Excel).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        dataframe_orders_ds=dataframe_orders_ds.groupby('Year')["number of deals"].sum().reset_index()
        dataframe_orders_ds=dataframe_orders_ds.set_index('Year')
        dataframe_orders_ds.plot(legend=True, ax=ax1,figsize=(6,6))
        ax1.set_title('Time series analysis report of the orders received (dataset)')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()

        analystframe_9=Frame(my_canvas)
        my_canvas.create_window((600,3300),window=analystframe_9,anchor="nw")
        l = tk.Label(analystframe_9,width=40, text='City and the number of deals done for that city',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        City_bu=tk.Button(analystframe_9,text="click here")
        City_bu.pack()
        City_bu.bind("<Button-1>",showcitycounttable)

        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select OPENING_AMT,PAYMENT_AMT from customer"
            cur.execute(sql)
            list_amts=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        count=0
        for i in list_amts:
            if i[0]>=i[1]:
                count=count+1
        
        temp_count=len(list_amts)-count
        lab=["Opening Amount >= Payment Amount ","Payment Amount > Opening Amount"]
        per=[count,temp_count]
        analystframe_10=Frame(my_canvas)
        my_canvas.create_window((600,3400),window=analystframe_10,anchor="nw")
        l = tk.Label(analystframe_10,width=50, text='Percentage of Opening Amount >= Payment Amount:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        ax1.pie(per, radius=1, labels=lab,autopct='%0.2f%%', shadow=True,)
        pie1 = FigureCanvasTkAgg(figure1,analystframe_10)
        pie1.get_tk_widget().pack()

    elif select_year.get()=="2017":
        analystframe_1=Frame(my_canvas)
        my_canvas.create_window((20,100),window=analystframe_1,anchor="nw")
        l = tk.Label(analystframe_1,width=50, text='Total property area sold vs total property are leased in Sq-M only.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_dataset=pd.DataFrame()
        for f in ["Dataset.xlsx"]:
            data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
            df_dataset=df_dataset.append(data)
    
        sqm_property_2017=df_dataset.loc[df_dataset['Year'] == 2017]
        
        owned_area=sqm_property_2017.loc[sqm_property_2017["Tenure"]=="Owned"]
        leased_area=sqm_property_2017.loc[sqm_property_2017["Tenure"]=="Leased"]
        
        owned_area_HA=owned_area.loc[owned_area['UoM'] == 'HA']
        owned_area_SQM=owned_area.loc[owned_area['UoM'] == 'SQ-M']
        leased_area_HA=leased_area.loc[leased_area['UoM'] == 'HA']
        leased_area_SQM=leased_area.loc[leased_area['UoM'] == 'SQ-M']
        totalareaowned=0
        totalarealeased=0
        temp_HA=owned_area_HA["Area"].tolist()
        temp_SQM=owned_area_SQM["Area"].tolist()
        totalareaowned=(sum(temp_HA)*10000)+sum(temp_SQM)
        
        temp_HA=leased_area_HA["Area"].tolist()
        temp_SQM=leased_area_SQM["Area"].tolist()
        totalarealeased=(sum(temp_HA)*10000)+sum(temp_SQM)
         
        totalareaowned=round(totalareaowned,3)
        totalarealeased=round(totalarealeased,3)
        list_area_owned=[totalareaowned,"Owned"]
        list_area_leased=[totalarealeased,"Leased"]
        list_area=[list_area_owned,list_area_leased]
        df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])
        
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_count= df_count[['Area','Tenure']].groupby('Tenure').sum()
        df_count.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_count["Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total area Owned Vs Total area Leased in SQ-M')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_1)
        bar1.get_tk_widget().pack()
    
        ca_property=df_dataset.loc[df_dataset['Country'] == 'CA']
        
        ca_leased_property=ca_property.loc[ca_property['Tenure'] == 'Leased']
        ca_leased_property_HA=ca_leased_property.loc[ca_leased_property['UoM'] == 'HA']
        ca_leased_property_SQM=ca_leased_property.loc[ca_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        
        area_2019=round(area_2019,3)
        temp_2018_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        
        area_2018=round(area_2018,3)
        temp_2017_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        
        area_2017=round(area_2017,3)
        temp_ca=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        
        analystframe_2=Frame(my_canvas)
        my_canvas.create_window((600,750),window=analystframe_2,anchor="nw")
        l = tk.Label(analystframe_2,width=50, text='Year that got maximum leased area in CA countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_CA_area =pd.DataFrame(temp_ca,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_CA_area= df_CA_area[['Total Area','Year']].groupby('Year').sum()
        df_CA_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_CA_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in CA (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_2)
        bar1.get_tk_widget().pack()
        max_year_ca=str(max(temp_ca)[1])
        text1="Year that got maximum leased area in CA : "+max_year_ca
        analystframe_2_1=Frame(my_canvas)
        my_canvas.create_window((600,1250),window=analystframe_2_1,anchor="nw")
        l = tk.Label(analystframe_2_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        ws_property=df_dataset.loc[df_dataset['Country'] == 'WS']
    
        ws_leased_property=ws_property.loc[ws_property['Tenure'] == 'Leased']
    
        ws_leased_property_HA=ws_leased_property.loc[ws_leased_property['UoM'] == 'HA']
        ws_leased_property_SQM=ws_leased_property.loc[ws_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        area_2019=round(area_2019,3)
        temp_2018_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        area_2018=round(area_2018,3)
        temp_2017_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        area_2017=round(area_2017,3)
        temp_ws=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        analystframe_3=Frame(my_canvas)
        my_canvas.create_window((20,750),window=analystframe_3,anchor="nw")
        l = tk.Label(analystframe_3,width=50, text='Year that got maximum leased area in WS countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_WS_area =pd.DataFrame(temp_ws,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_WS_area= df_WS_area[['Total Area','Year']].groupby('Year').sum()
        df_WS_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_WS_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in WS (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_3)
        bar1.get_tk_widget().pack()
        max_year_ws=str(max(temp_ws)[1])
        text1="Year that got maximum leased area in WS : "+max_year_ws
        analystframe_3_1=Frame(my_canvas)
        my_canvas.create_window((20,1250),window=analystframe_3_1,anchor="nw")
        l = tk.Label(analystframe_3_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        #print(temp_ca)
        #print(temp_ws)
        find_max_year=[]
        for i in range(0,len(temp_ca)):
            total=temp_ca[i][0]+temp_ws[i][0]
            find_max_year.append([total,temp_ca[i][1]])
        max_year=str(max(find_max_year)[1])
        text1="Year that got maximum leased area in both CA and WS countries : "+max_year
        analystframe_3_2=Frame(my_canvas)
        my_canvas.create_window((80,1280),window=analystframe_3_2,anchor="nw")
        l = tk.Label(analystframe_3_2,width=80, text=text1,font=('arial', 12))
        l.pack()
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((10,1350),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=70, text='The Agent codes of all the agents who have got deals in ‘OWNED’ categories:',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        Agents_bu=tk.Button(analystframe_5,text="click here")
        Agents_bu.pack()
        Agents_bu.bind("<Button-1>",showagenttable)
        
        leasedproperty=df_dataset.loc[df_dataset['Tenure'] == 'Leased']
        chillwack_leasedproperty=leasedproperty.loc[leasedproperty['City'] == 'Chilliwack']
        chillwack_leasedproperty_2017=chillwack_leasedproperty.loc[chillwack_leasedproperty['Year'] == 2017]
        #print(chillwack_leasedproperty_2019)
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select AGENT_NAME from agents"
            cur.execute(sql)
            list_agents=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        chillwack_agents=chillwack_leasedproperty_2017["Agent"].tolist()
        #print(chillwack_agents)
        #print(list_agents)
        deals=[]
        max1=0
        max_name=''
        for i in list_agents:
            name=""
            words = i[0].split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            count=chillwack_agents.count(name)
            #print(count)
            if count > max1:
                max1=count
                max_name=name
            temp=[name,count]
            deals.append(temp)
        analystframe_4=Frame(my_canvas)
        my_canvas.create_window((600,100),window=analystframe_4,anchor="nw")    
        l = tk.Label(analystframe_4,width=50, text='For the city of chillwack, agent hs got the maximum leased deals:-',fg="blue",font=('arial', 12))
        l.pack()
        temp_df=pd.DataFrame(deals,columns=['Agent Name','Deals'])
        figure3 = plt.Figure(figsize=(6,7), dpi=80)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(temp_df['Agent Name'],temp_df['Deals'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3,analystframe_4 ) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(["Leased Deals"]) 
        ax3.set_xlabel('Agent Name')
        ax3.set_xticklabels(temp_df['Agent Name'],rotation=45)
        ax3.set_title('No. of deals done by agents on leased form in city of Chilliwack')
        text1="agent which has got the maximum deals in leased form: "+max_name
        analystframe_4_1=Frame(my_canvas)
        my_canvas.create_window((600,680),window=analystframe_4_1,anchor="nw")
        l = tk.Label(analystframe_4_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals["Agent"].replace(dict, inplace=True)
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        agents=[]
        for i in listagents:
            if type(i)==str:
                agents.append(i)
        #print(agents)
        all_owneddeals=all_deals.loc[all_deals["Tenure"]=="Owned"]
        all_owneddeals_HA=all_owneddeals.loc[all_owneddeals['UoM'] == 'HA']
        all_owneddeals_SQM=all_owneddeals.loc[all_owneddeals['UoM'] == 'SQ-M']
        all_leaseddeals=all_deals.loc[all_deals["Tenure"]=="Leased"]
        all_leaseddeals_HA=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'HA']
        all_leaseddeals_SQM=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'SQ-M']
        
        agents_owned_area=[]
        agents_leased_area=[]
        for i in agents:
            temp_ha=(all_owneddeals_HA[(all_owneddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_owneddeals_SQM[(all_owneddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            
            totalarea=round(totalarea,3)
            agents_owned_area.append(totalarea)
        for i in agents:
            temp_ha=(all_leaseddeals_HA[(all_leaseddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_leaseddeals_SQM[(all_leaseddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            totalarea=round(totalarea,3)
            agents_leased_area.append(totalarea)
        agent_area=[] 
        find_max=[]
        for i in range(0,len(agents)):
            temp=[agents[i],agents_owned_area[i],agents_leased_area[i]]
            find_max.append([agents_owned_area[i]+agents_leased_area[i],agents[i]])
            agent_area.append(temp)
        #print(max(find_max))
        max_agent=max(find_max)[1]
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((20,1400),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=90, text='The performance of all agents based on the area leased and owned for the years 2017,2018 and 2019:-',fg="blue",font=('arial', 12))
        l.pack()
        df_agent_own_lease =pd.DataFrame(agent_area,columns=['Agent','Total Owned Area',"Total Leased Area"])
        #print(df_agent_own_lease)
        figure1 = Figure(figsize=(12,8), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_agent_own_lease = df_agent_own_lease [['Agent','Total Owned Area',"Total Leased Area"]].groupby('Agent').sum()
        df_agent_own_lease.plot(kind='bar', legend=True, ax=ax1,width=1)
        for i, v in enumerate(df_agent_own_lease["Total Owned Area"]):
            ax1.text(i- 0.75, v+3, str(v),color ="blue")
        for i, v in enumerate(df_agent_own_lease["Total Leased Area"]):
            ax1.text(i, v+3, str(v),color ="red")
        
        ax1.set_title('Performance of each agent for years 2017,18,19 (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_5)
        bar1.get_tk_widget().pack()
        text1="Agent who has been the best performer is "+max_agent
        analystframe_5_1=Frame(my_canvas)
        my_canvas.create_window((20,2100),window=analystframe_5_1,anchor="nw")
        l = tk.Label(analystframe_5_1,width=90, text=text1,font=('arial', 12))
        l.pack()
        
        
        owned_property=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_Jul_property=owned_property.loc[owned_property["Month"]=="JUL"]
        owned_Jul_property_HA=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'HA']
        owned_Jul_property_SQM=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'SQ-M']
        years=list(set(owned_Jul_property["Year"].tolist()))
        #print(years)
        total_area=[]
        for i in years:
            temp_ha=(owned_Jul_property_HA[(owned_Jul_property_HA.Year==i)].Area).tolist()
            temp_sqm=(owned_Jul_property_SQM[(owned_Jul_property_SQM.Year==i)].Area).tolist()
            area=(sum(temp_ha)*10000)+sum(temp_sqm)
            area=round(area,3)
            total_area.append(area)
        temp_list=[]
        add=0
        for i in range(0,len(years)):
            temp=[years[i],total_area[i]]
            add=add+total_area[i]
            temp_list.append(temp)
        temp_list.append(["Total",add])
        #print(temp_list)
        analystframe_6=Frame(my_canvas)
        my_canvas.create_window((20,2180),window=analystframe_6,anchor="nw")
        l = tk.Label(analystframe_6,width=50, text='Amount of property area sold for the month of july for all the years.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_owned_year =pd.DataFrame(temp_list,columns=['Year','Total Owned Area'])

        figure1 = Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_owned_year= df_owned_year[['Year','Total Owned Area']].groupby('Year').sum()
        df_owned_year.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_owned_year["Total Owned Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('amount of property area sold for the month of july for all the years (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_6)
        bar1.get_tk_widget().pack()

        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            query="select ORD_DATE from orders"
            cur.execute(query)
            row=list(cur.fetchall())
        except:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        temp_list=[]
        my_time=datetime.min.time()
        for i in range(0,len(row)):
            row[i]=list(row[i])
            row[i][0]=datetime.combine(row[i][0],my_time)
            temp_list.append(1)
        dataframe_orders =pd.DataFrame(row,columns=["Order Date"])
    
        dataframe_orders["number of deals"]=temp_list
        
        #print(dataframe_orders["Order Date"].min())
        #print(dataframe_orders["Order Date"].max())
        dataframe_orders=dataframe_orders.sort_values('Order Date')
        #print(dataframe_orders.sort_values('Order Date'))
        dataframe_orders=dataframe_orders.groupby('Order Date')["number of deals"].sum().reset_index()
        dataframe_orders=dataframe_orders.set_index('Order Date')
        #print(dataframe_orders)
        df_y = dataframe_orders['number of deals'].resample('MS').sum()
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,2750),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received.:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(15,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_y.plot(legend=True, ax=ax1,figsize=(15,6))
        ax1.set_title('Time series analysis report of the orders received')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
        
        years=df_dataset["Year"].tolist()
        for i in years:
            if type(i)==str:
                years.remove(i)
        temp=list(set(years))
        count=[]
        year=[]
        for i in temp:
            count.append(years.count(i))
            year.append(str(i))
            
        
        dataframe_orders_ds=pd.DataFrame(year,columns=["Year"])
        dataframe_orders_ds["number of deals"]=count
        
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,3300),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (dataset-Excel).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        dataframe_orders_ds=dataframe_orders_ds.groupby('Year')["number of deals"].sum().reset_index()
        dataframe_orders_ds=dataframe_orders_ds.set_index('Year')
        dataframe_orders_ds.plot(legend=True, ax=ax1,figsize=(6,6))
        ax1.set_title('Time series analysis report of the orders received (dataset)')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()

        analystframe_9=Frame(my_canvas)
        my_canvas.create_window((600,3300),window=analystframe_9,anchor="nw")
        l = tk.Label(analystframe_9,width=40, text='City and the number of deals done for that city',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        City_bu=tk.Button(analystframe_9,text="click here")
        City_bu.pack()
        City_bu.bind("<Button-1>",showcitycounttable)

        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select OPENING_AMT,PAYMENT_AMT from customer"
            cur.execute(sql)
            list_amts=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        count=0
        for i in list_amts:
            if i[0]>=i[1]:
                count=count+1
        
        temp_count=len(list_amts)-count
        lab=["Opening Amount >= Payment Amount ","Payment Amount > Opening Amount"]
        per=[count,temp_count]
        analystframe_10=Frame(my_canvas)
        my_canvas.create_window((600,3400),window=analystframe_10,anchor="nw")
        l = tk.Label(analystframe_10,width=50, text='Percentage of Opening Amount >= Payment Amount:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        ax1.pie(per, radius=1, labels=lab,autopct='%0.2f%%', shadow=True,)
        pie1 = FigureCanvasTkAgg(figure1,analystframe_10)
        pie1.get_tk_widget().pack()

    elif select_year.get()=="2020":
        analystframe_1=Frame(my_canvas)
        my_canvas.create_window((20,100),window=analystframe_1,anchor="nw")
        l = tk.Label(analystframe_1,width=50, text='Total property area sold vs total property are leased in Sq-M only.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_dataset=pd.DataFrame()
        for f in ["Dataset.xlsx"]:
            data=pd.read_excel(f,"Page1_1",skiprows=8,usecols="A:C,F,H,I,J,L")
            df_dataset=df_dataset.append(data)
    
        sqm_property_2020=df_dataset.loc[df_dataset['Year'] == 2020]
        
        owned_area=sqm_property_2020.loc[sqm_property_2020["Tenure"]=="Owned"]
        leased_area=sqm_property_2020.loc[sqm_property_2020["Tenure"]=="Leased"]
        
        owned_area_HA=owned_area.loc[owned_area['UoM'] == 'HA']
        owned_area_SQM=owned_area.loc[owned_area['UoM'] == 'SQ-M']
        leased_area_HA=leased_area.loc[leased_area['UoM'] == 'HA']
        leased_area_SQM=leased_area.loc[leased_area['UoM'] == 'SQ-M']
        totalareaowned=0
        totalarealeased=0
        temp_HA=owned_area_HA["Area"].tolist()
        temp_SQM=owned_area_SQM["Area"].tolist()
        totalareaowned=(sum(temp_HA)*10000)+sum(temp_SQM)
        
        temp_HA=leased_area_HA["Area"].tolist()
        temp_SQM=leased_area_SQM["Area"].tolist()
        totalarealeased=(sum(temp_HA)*10000)+sum(temp_SQM)
         
        totalareaowned=round(totalareaowned,3)
        totalarealeased=round(totalarealeased,3)
        list_area_owned=[totalareaowned,"Owned"]
        list_area_leased=[totalarealeased,"Leased"]
        list_area=[list_area_owned,list_area_leased]
        df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])
        
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_count= df_count[['Area','Tenure']].groupby('Tenure').sum()
        df_count.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_count["Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total area Owned Vs Total area Leased in SQ-M')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_1)
        bar1.get_tk_widget().pack()
    
        ca_property=df_dataset.loc[df_dataset['Country'] == 'CA']
        
        ca_leased_property=ca_property.loc[ca_property['Tenure'] == 'Leased']
        ca_leased_property_HA=ca_leased_property.loc[ca_leased_property['UoM'] == 'HA']
        ca_leased_property_SQM=ca_leased_property.loc[ca_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        
        area_2019=round(area_2019,3)
        temp_2018_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        
        area_2018=round(area_2018,3)
        temp_2017_ha=(ca_leased_property_HA[(ca_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ca_leased_property_SQM[(ca_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        
        area_2017=round(area_2017,3)
        temp_ca=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        
        analystframe_2=Frame(my_canvas)
        my_canvas.create_window((600,750),window=analystframe_2,anchor="nw")
        l = tk.Label(analystframe_2,width=50, text='Year that got maximum leased area in CA countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_CA_area =pd.DataFrame(temp_ca,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_CA_area= df_CA_area[['Total Area','Year']].groupby('Year').sum()
        df_CA_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_CA_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in CA (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_2)
        bar1.get_tk_widget().pack()
        max_year_ca=str(max(temp_ca)[1])
        text1="Year that got maximum leased area in CA : "+max_year_ca
        analystframe_2_1=Frame(my_canvas)
        my_canvas.create_window((600,1250),window=analystframe_2_1,anchor="nw")
        l = tk.Label(analystframe_2_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        ws_property=df_dataset.loc[df_dataset['Country'] == 'WS']
    
        ws_leased_property=ws_property.loc[ws_property['Tenure'] == 'Leased']
    
        ws_leased_property_HA=ws_leased_property.loc[ws_leased_property['UoM'] == 'HA']
        ws_leased_property_SQM=ws_leased_property.loc[ws_leased_property['UoM'] == 'SQ-M']
        area_2019=0
        area_2018=0
        area_2017=0
        temp_2019_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2019)].Area).tolist()
        temp_2019_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2019)].Area).tolist()
        area_2019=(sum(temp_2019_ha)*10000)+sum(temp_2019_sqm)
        area_2019=round(area_2019,3)
        temp_2018_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2018)].Area).tolist()
        temp_2018_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2018)].Area).tolist()
        area_2018=(sum(temp_2018_ha)*10000)+sum(temp_2018_sqm)
        area_2018=round(area_2018,3)
        temp_2017_ha=(ws_leased_property_HA[(ws_leased_property_HA.Year==2017)].Area).tolist()
        temp_2017_sqm=(ws_leased_property_SQM[(ws_leased_property_SQM.Year==2017)].Area).tolist()
        area_2017=(sum(temp_2017_ha)*10000)+sum(temp_2017_sqm)
        area_2017=round(area_2017,3)
        temp_ws=[[area_2019,2019],[area_2018,2018],[area_2017,2017]]
        
        analystframe_3=Frame(my_canvas)
        my_canvas.create_window((20,750),window=analystframe_3,anchor="nw")
        l = tk.Label(analystframe_3,width=50, text='Year that got maximum leased area in WS countries. :-',fg="blue",font=('arial', 12))
        l.pack()
        df_WS_area =pd.DataFrame(temp_ws,columns=['Total Area','Year'])
        figure1 = Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_WS_area= df_WS_area[['Total Area','Year']].groupby('Year').sum()
        df_WS_area.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_WS_area["Total Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('Total leased area per year in WS (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_3)
        bar1.get_tk_widget().pack()
        max_year_ws=str(max(temp_ws)[1])
        text1="Year that got maximum leased area in WS : "+max_year_ws
        analystframe_3_1=Frame(my_canvas)
        my_canvas.create_window((20,1250),window=analystframe_3_1,anchor="nw")
        l = tk.Label(analystframe_3_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        
        #print(temp_ca)
        #print(temp_ws)
        find_max_year=[]
        for i in range(0,len(temp_ca)):
            total=temp_ca[i][0]+temp_ws[i][0]
            find_max_year.append([total,temp_ca[i][1]])
        max_year=str(max(find_max_year)[1])
        text1="Year that got maximum leased area in both CA and WS countries : "+max_year
        analystframe_3_2=Frame(my_canvas)
        my_canvas.create_window((80,1280),window=analystframe_3_2,anchor="nw")
        l = tk.Label(analystframe_3_2,width=80, text=text1,font=('arial', 12))
        l.pack()
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((10,1350),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=70, text='The Agent codes of all the agents who have got deals in ‘OWNED’ categories:',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        Agents_bu=tk.Button(analystframe_5,text="click here")
        Agents_bu.pack()
        Agents_bu.bind("<Button-1>",showagenttable)
        
        leasedproperty=df_dataset.loc[df_dataset['Tenure'] == 'Leased']
        chillwack_leasedproperty=leasedproperty.loc[leasedproperty['City'] == 'Chilliwack']
        chillwack_leasedproperty_2020=chillwack_leasedproperty.loc[chillwack_leasedproperty['Year'] == 2020]
        #print(chillwack_leasedproperty_2019)
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select AGENT_NAME from agents"
            cur.execute(sql)
            list_agents=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        chillwack_agents=chillwack_leasedproperty_2020["Agent"].tolist()
        #print(chillwack_agents)
        #print(list_agents)
        deals=[]
        max1=0
        max_name=''
        for i in list_agents:
            name=""
            words = i[0].split()
            for j in words:
                if j.isalpha():
                    name=name+" "+j
            name=name.lstrip()
            count=chillwack_agents.count(name)
            #print(count)
            if count > max1:
                max1=count
                max_name=name
            temp=[name,count]
            deals.append(temp)
        analystframe_4=Frame(my_canvas)
        my_canvas.create_window((600,100),window=analystframe_4,anchor="nw")    
        l = tk.Label(analystframe_4,width=50, text='For the city of chillwack, agent hs got the maximum leased deals:-',fg="blue",font=('arial', 12))
        l.pack()
        temp_df=pd.DataFrame(deals,columns=['Agent Name','Deals'])
        figure3 = plt.Figure(figsize=(6,7), dpi=80)
        ax3 = figure3.add_subplot(111)
        ax3.scatter(temp_df['Agent Name'],temp_df['Deals'], color = 'g')
        scatter3 = FigureCanvasTkAgg(figure3,analystframe_4 ) 
        scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        ax3.legend(["Leased Deals"]) 
        ax3.set_xlabel('Agent Name')
        ax3.set_xticklabels(temp_df['Agent Name'],rotation=45)
        ax3.set_title('No. of deals done by agents on leased form in city of Chilliwack')
        text1="agent which has got the maximum deals in leased form: "+max_name
        analystframe_4_1=Frame(my_canvas)
        my_canvas.create_window((600,680),window=analystframe_4_1,anchor="nw")
        l = tk.Label(analystframe_4_1,width=50, text=text1,font=('arial', 12))
        l.pack()
        all_deals=df_dataset[df_dataset.Year !=2020]
        
        
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        dict={}
        for i in listagents:
            if type(i)==str:
                name=""
                words = i.split()
                for j in words:
                    if j.isalpha():
                        name=name+" "+j
                name=name.lstrip()
                dict.update({i:name})
            
        all_deals["Agent"].replace(dict, inplace=True)
        listagents=all_deals["Agent"].tolist()
        #print(listagents)
        listagents=list(set(listagents))
        agents=[]
        for i in listagents:
            if type(i)==str:
                agents.append(i)
        #print(agents)
        all_owneddeals=all_deals.loc[all_deals["Tenure"]=="Owned"]
        all_owneddeals_HA=all_owneddeals.loc[all_owneddeals['UoM'] == 'HA']
        all_owneddeals_SQM=all_owneddeals.loc[all_owneddeals['UoM'] == 'SQ-M']
        all_leaseddeals=all_deals.loc[all_deals["Tenure"]=="Leased"]
        all_leaseddeals_HA=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'HA']
        all_leaseddeals_SQM=all_leaseddeals.loc[all_leaseddeals['UoM'] == 'SQ-M']
        
        agents_owned_area=[]
        agents_leased_area=[]
        for i in agents:
            temp_ha=(all_owneddeals_HA[(all_owneddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_owneddeals_SQM[(all_owneddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            
            totalarea=round(totalarea,3)
            agents_owned_area.append(totalarea)
        for i in agents:
            temp_ha=(all_leaseddeals_HA[(all_leaseddeals_HA.Agent==i)].Area).tolist()
            temp_sqm=(all_leaseddeals_SQM[(all_leaseddeals_SQM.Agent==i)].Area).tolist()
            totalarea=(sum(temp_ha)*10000)+sum(temp_sqm)
            totalarea=round(totalarea,3)
            agents_leased_area.append(totalarea)
        agent_area=[] 
        find_max=[]
        for i in range(0,len(agents)):
            temp=[agents[i],agents_owned_area[i],agents_leased_area[i]]
            find_max.append([agents_owned_area[i]+agents_leased_area[i],agents[i]])
            agent_area.append(temp)
        #print(max(find_max))
        max_agent=max(find_max)[1]
        analystframe_5=Frame(my_canvas)
        my_canvas.create_window((20,1400),window=analystframe_5,anchor="nw")
        l = tk.Label(analystframe_5,width=90, text='The performance of all agents based on the area leased and owned for the years 2017,2018 and 2019:-',fg="blue",font=('arial', 12))
        l.pack()
        df_agent_own_lease =pd.DataFrame(agent_area,columns=['Agent','Total Owned Area',"Total Leased Area"])
        #print(df_agent_own_lease)
        figure1 = Figure(figsize=(12,8), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_agent_own_lease = df_agent_own_lease [['Agent','Total Owned Area',"Total Leased Area"]].groupby('Agent').sum()
        df_agent_own_lease.plot(kind='bar', legend=True, ax=ax1,width=1)
        for i, v in enumerate(df_agent_own_lease["Total Owned Area"]):
            ax1.text(i- 0.75, v+3, str(v),color ="blue")
        for i, v in enumerate(df_agent_own_lease["Total Leased Area"]):
            ax1.text(i, v+3, str(v),color ="red")
        
        ax1.set_title('Performance of each agent for years 2017,18,19 (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_5)
        bar1.get_tk_widget().pack()
        text1="Agent who has been the best performer is "+max_agent
        analystframe_5_1=Frame(my_canvas)
        my_canvas.create_window((20,2100),window=analystframe_5_1,anchor="nw")
        l = tk.Label(analystframe_5_1,width=90, text=text1,font=('arial', 12))
        l.pack()
        
        
        owned_property=df_dataset.loc[df_dataset["Tenure"]=="Owned"]
        owned_Jul_property=owned_property.loc[owned_property["Month"]=="JUL"]
        owned_Jul_property_HA=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'HA']
        owned_Jul_property_SQM=owned_Jul_property.loc[owned_Jul_property['UoM'] == 'SQ-M']
        years=list(set(owned_Jul_property["Year"].tolist()))
        #print(years)
        total_area=[]
        for i in years:
            temp_ha=(owned_Jul_property_HA[(owned_Jul_property_HA.Year==i)].Area).tolist()
            temp_sqm=(owned_Jul_property_SQM[(owned_Jul_property_SQM.Year==i)].Area).tolist()
            area=(sum(temp_ha)*10000)+sum(temp_sqm)
            area=round(area,3)
            total_area.append(area)
        temp_list=[]
        add=0
        for i in range(0,len(years)):
            temp=[years[i],total_area[i]]
            add=add+total_area[i]
            temp_list.append(temp)
        temp_list.append(["Total",add])
        #print(temp_list)
        analystframe_6=Frame(my_canvas)
        my_canvas.create_window((20,2180),window=analystframe_6,anchor="nw")
        l = tk.Label(analystframe_6,width=50, text='Amount of property area sold for the month of july for all the years.:-',fg="blue",font=('arial', 12))
        l.pack()
        df_owned_year =pd.DataFrame(temp_list,columns=['Year','Total Owned Area'])

        figure1 = Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_owned_year= df_owned_year[['Year','Total Owned Area']].groupby('Year').sum()
        df_owned_year.plot(kind='bar', legend=True, ax=ax1)
        for i, v in enumerate(df_owned_year["Total Owned Area"]):
            ax1.text(i- 0.25, v+3, str(v))
        ax1.set_title('amount of property area sold for the month of july for all the years (in SQ-M)')
        bar1 = FigureCanvasTkAgg(figure1,analystframe_6)
        bar1.get_tk_widget().pack()


        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            query="select ORD_DATE from orders"
            cur.execute(query)
            row=list(cur.fetchall())
        except:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        temp_list=[]
        my_time=datetime.min.time()
        for i in range(0,len(row)):
            row[i]=list(row[i])
            row[i][0]=datetime.combine(row[i][0],my_time)
            temp_list.append(1)
        dataframe_orders =pd.DataFrame(row,columns=["Order Date"])
    
        dataframe_orders["number of deals"]=temp_list
        
        #print(dataframe_orders["Order Date"].min())
        #print(dataframe_orders["Order Date"].max())
        dataframe_orders=dataframe_orders.sort_values('Order Date')
        #print(dataframe_orders.sort_values('Order Date'))
        dataframe_orders=dataframe_orders.groupby('Order Date')["number of deals"].sum().reset_index()
        dataframe_orders=dataframe_orders.set_index('Order Date')
        #print(dataframe_orders)
        df_y = dataframe_orders['number of deals'].resample('MS').sum()
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,2750),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received.:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(15,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        df_y.plot(legend=True, ax=ax1,figsize=(15,6))
        ax1.set_title('Time series analysis report of the orders received')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()

        years=df_dataset["Year"].tolist()
        for i in years:
            if type(i)==str:
                years.remove(i)
        temp=list(set(years))
        count=[]
        year=[]
        for i in temp:
            count.append(years.count(i))
            year.append(str(i))
            
        
        dataframe_orders_ds=pd.DataFrame(year,columns=["Year"])
        dataframe_orders_ds["number of deals"]=count
        
        analystframe_7=Frame(my_canvas)
        my_canvas.create_window((20,3300),window=analystframe_7,anchor="nw")
        l = tk.Label(analystframe_7,width=50, text='time series analysis report of the orders received (dataset-Excel).:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(6,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        dataframe_orders_ds=dataframe_orders_ds.groupby('Year')["number of deals"].sum().reset_index()
        dataframe_orders_ds=dataframe_orders_ds.set_index('Year')
        dataframe_orders_ds.plot(legend=True, ax=ax1,figsize=(6,6))
        ax1.set_title('Time series analysis report of the orders received (dataset)')
        line1 = FigureCanvasTkAgg(figure1,analystframe_7)
        line1.get_tk_widget().pack()
        
        analystframe_9=Frame(my_canvas)
        my_canvas.create_window((600,3300),window=analystframe_9,anchor="nw")
        l = tk.Label(analystframe_9,width=40, text='City and the number of deals done for that city',fg="blue",font=('arial', 12))
        l.pack(side=LEFT)
        City_bu=tk.Button(analystframe_9,text="click here")
        City_bu.pack()
        City_bu.bind("<Button-1>",showcitycounttable)
        
        try:
            conn = pymysql.connect(user="root", password="", host="localhost", database="sales")
            cur = conn.cursor()
            sql="select OPENING_AMT,PAYMENT_AMT from customer"
            cur.execute(sql)
            list_amts=list(cur.fetchall())
        except Exception as e:
            print(e)
            tm.showerror("Show" ,"Failed to make connection")
        count=0
        for i in list_amts:
            if i[0]>=i[1]:
                count=count+1
        
        temp_count=len(list_amts)-count
        lab=["Opening Amount >= Payment Amount ","Payment Amount > Opening Amount"]
        per=[count,temp_count]
        analystframe_10=Frame(my_canvas)
        my_canvas.create_window((600,3400),window=analystframe_10,anchor="nw")
        l = tk.Label(analystframe_10,width=50, text='Percentage of Opening Amount >= Payment Amount:-',fg="blue",font=('arial', 12))
        l.pack()
        figure1 =Figure(figsize=(7,6), dpi=80)
        ax1 = figure1.add_subplot(111)
        ax1.pie(per, radius=1, labels=lab,autopct='%0.2f%%', shadow=True,)
        pie1 = FigureCanvasTkAgg(figure1,analystframe_10)
        pie1.get_tk_widget().pack()
        
def analyst(event):
    analystindow=Toplevel()
    analystindow.title("ANALYST")
    analystindow.geometry('{}x{}'.format(1200, 700))
    global my_canvas
    analyst_mainframe=Frame(analystindow)
    analyst_mainframe.pack(fill=BOTH,expand=1)
    my_canvas=Canvas(analyst_mainframe)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    my_scrollbar=Scrollbar(analyst_mainframe,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>' , lambda e :my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    analystframe=Frame(my_canvas)
    my_canvas.create_window((550,40),window=analystframe,anchor="nw")
    analystframe_0=Frame(analystframe)
    analystframe_0.pack()
    global select_year
    select_year=StringVar()
    Label(analystframe_0, text='Select year:', anchor='w').grid(row=0, column=0 ,padx=5, pady=5, sticky="w")
    choices =["ALL","2020","2019","2018","2017"]
    Combobox(analystframe_0 , width=5, values = choices ,textvariable = select_year ).grid(row=0, column=1, padx=5, pady=5)
    Button(analystframe_0, text="search",command=make_graph).grid(row=0,column=3,padx=5)    
    analystindow.mainloop()

img_employee=ImageTk.PhotoImage(PIL.Image.open("employee.PNG"))
bu1=tk.Button(root,image=img_employee)
bu1.place(x=30,y=180)
bu1.bind("<Button-1>",employee)
img_analyst=ImageTk.PhotoImage(PIL.Image.open("analyst.PNG"))
bu2=tk.Button(root,image=img_analyst)
bu2.place(x=450,y=180)
bu2.bind("<Button-1>",analyst)
root.mainloop()
