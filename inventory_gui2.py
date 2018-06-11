from Tkinter import *
from PIL import Image
import pymysql
import pymysql.cursors
import PIL.ImageTk

global inventory_form, display, cancel, modify
global user_name, password, search_param
global product_id, product_name, ship_id, ship_name, container_id, delivery_date, order_date, place_of_delivery, port_id, port_name, from_address, destination, modi_contact_info, pid_of_mod, pid_of_del

def raise_frame(frame):
    frame.tkraise()

db = pymysql.connect("localhost", "root", "", "INVENTORY_MANAGEMENT")
cursor = db.cursor()

def check_credentials():
    name = e1.get()
    password = e2.get()
    if (name == "munna") & (password == "password"):
        print("successfully established connection")
        raise_frame(inventory_form)
        window.destroy()
    else:
        print("wrong credentials")
        return


def enter_into_db():
    #  text.delete('1.0', END)
    product_id = id.get()
    product_name = prod_name.get()
    ship_id = shipid.get()
    container_id = cont_id.get()
    delivery_date = deli_date.get()
    order_date = orde_date.get()
    port_id = port_identiti.get()
    port_name = port_na.get()
    from_address = source_address.get()
    destination = dest_add.get()

    sql_products="""INSERT INTO `PRODUCTS`(`PRODUCT_ID`,`PRODUCT_NAME`) VALUES('"""+product_id+""""','"""+product_name+""""')"""
    cursor.execute(sql_products)

    sql_ships1 = """INSERT INTO `SHIPS` (`SHIP_ID`, `SHIP_NAME`) VALUES ('""" + ship_id + """"','FARGO')"""
    cursor.execute(sql_ships1)

    sql_products="""INSERT INTO `DATE_TIME`(`DEPARTURE_DATE`,`DELIVERY_DATE`) VALUES('"""+order_date+""""','"""+delivery_date+""""')"""
    cursor.execute(sql_products)

    sql_warehouse = """INSERT INTO `PORTS` (`PORT_ID`, `PORT_NAME`) VALUES ('""" + port_id+ """"','"""+ port_name+""""')"""
    cursor.execute(sql_warehouse)

    sql_warehouse = """INSERT INTO `WAREHOUSE` (`SOURCE`, `DESTINATION`) VALUES ('""" + from_address + """"','"""+destination+""""')"""
    cursor.execute(sql_warehouse)

    db.commit()

    text.insert(END, product_id)
    text.insert(END, "\n")
    text.insert(INSERT, product_name)
    text.insert(END, "\n")
    text.insert(END, ship_id)
    text.insert(END, "\n")
    text.insert(END, container_id)
    text.insert(END, "\n")
    text.insert(END, delivery_date)
    text.insert(END, "\n")
    text.insert(END, order_date)
    text.insert(END, "\n")
    text.insert(END, port_id)
    text.insert(END, "\n")
    text.insert(END, port_name)
    text.insert(END, "\n")
    text.insert(END, from_address)
    text.insert(END, "\n")
    text.insert(END, destination)
    text.insert(END, "\n")
    id.delete(0, END)
    prod_name.delete(0, END)
    shipid.delete(0, END)
    cont_id.delete(0, END)
    deli_date.delete(0, END)
    orde_date.delete(0, END)
    port_identiti.delete(0, END)
    port_na.delete(0, END)
    source_address.delete(0, END)
    dest_add.delete(0, END)


def search():
    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `WAREHOUSE` WHERE `W_SOURCE_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()

    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `PORTS` WHERE `PORT_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()

    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `SHIPS` WHERE `SHIP_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()

    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `PRODUCTS` WHERE `PRODUCT_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()

    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `PERSON` WHERE `PERSON_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()

    search_param = take_id.get()
    print (search_param)
    sql = """SELECT * FROM `DATE_TIME` WHERE `PER_ID` LIKE '""" + search_param + """'"""
    cursor.execute(sql)
    r = cursor.fetchall()
    search_results.insert(END, r)
    db.commit()


def modifico():

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod1 = """UPDATE `PRODUCTS` SET PRODUCT_NAME='"""+modi_contact_info+"""'WHERE PRODUCT_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod1)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod2 = """UPDATE `PORTS` SET PORT_NAME='"""+modi_contact_info+"""'WHERE PORT_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod2)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod3 = """UPDATE `SHIPS` SET SHIP_NAME='"""+modi_contact_info+"""'WHERE SHIP_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod3)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod4 = """UPDATE `PERSON` SET PERSON_NAME='"""+modi_contact_info+"""'WHERE PERSON_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod4)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod = """UPDATE `DATE_TIME` SET DELIVERY_DATE='"""+modi_contact_info+"""'WHERE PER_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()

    pid_of_mod = pi.get()
    modi_contact_info = c.get()
    sql_update_prod = """UPDATE `WAREHOUSE` SET DESTINATION='"""+modi_contact_info+"""'WHERE W_DESTINATION_ID=""""'""" + pid_of_mod+"""'"""
    cursor.execute(sql_update_prod)
    db.commit()
    c.delete(0, END)
    pi.delete(0, END)
    db.commit()


def del_order():
    pid_of_del1 = o.get()
    print (pid_of_del1)
    sql_delete_1 = """DELETE FROM `PRODUCTS` WHERE `PRODUCT_ID` LIKE '""" + pid_of_del1 + """'"""
    cursor.execute(sql_delete_1)
    db.commit()

    pid_of_del2 = o.get()
    print (pid_of_del2)
    sql_delete_2 = """DELETE FROM `SHIPS` WHERE `SHIP_ID` LIKE'""" + pid_of_del2 + """'"""
    cursor.execute(sql_delete_2)
    db.commit()

    pid_of_del3 = o.get()
    print (pid_of_del3)
    sql_delete_3 = """DELETE FROM `PERSON` WHERE `PERSON_ID` LIKE '""" + pid_of_del3 + """'"""
    cursor.execute(sql_delete_3)
    db.commit()

    pid_of_del4 = o.get()
    print (pid_of_del4)
    sql_delete_4= """DELETE FROM `WAREHOUSE` WHERE `W_SOURCE_ID` LIKE '""" + pid_of_del4 + """'"""
    cursor.execute(sql_delete_4)
    db.commit()

    pid_of_del5 = o.get()
    print (pid_of_del5)
    sql_delete_5= """DELETE FROM `PORTS` WHERE `PORT_ID` LIKE '""" + pid_of_del5 + """'"""
    cursor.execute(sql_delete_5)
    db.commit()

    pid_of_del6 = o.get()
    print (pid_of_del6)
    sql_delete_6= """DELETE FROM `DATE_TIME` WHERE `PER_ID` LIKE '""" + pid_of_del6 + """'"""
    cursor.execute(sql_delete_6)
    db.commit()


root = Tk()
root.title("Fargo")
im = Image.open('/home/pennywise/ship3.jpg')
# im=im.resize((1100,1100),Image.ANTIALIAS)
tkimage = PIL.ImageTk.PhotoImage(im)
myvar = Label(root, image=tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
myvar.image = tkimage
# root.minsize(800,380)
root.resizable(0, 0)

# button=Button(root,text="lets start",command=lambda:raise_frame(window),fg="blue",bg="white")
# button.grid(row=1,column=200)

inventory_form = Frame(root)
inventory_form.grid(row=0, column=0)
heading2 = Label(inventory_form, text="FORM")
heading2.grid(row=0, column=0)
im6 = Image.open('/home/pennywise/ship4.jpg')
im6 = im6.resize((1200, 610), Image.ANTIALIAS)
tkimage6 = PIL.ImageTk.PhotoImage(im6)
myvar6 = Label(inventory_form, image=tkimage6)
myvar6.place(x=0, y=0, relwidth=1, relheight=1)
myvar6.image = tkimage6

display = Frame(root)
labella = Label(display, text="DISPLAY")
labella.grid(row=0, column=0)
display.configure(background='aqua')
im5 = Image.open('/home/pennywise/ship5.jpg')
im5 = im5.resize((1200, 600), Image.ANTIALIAS)
tkimage5 = PIL.ImageTk.PhotoImage(im5)
myvar5 = Label(display, image=tkimage5)
myvar5.place(x=0, y=0, relwidth=1, relheight=1)
myvar5.image = tkimage5

modify = Frame(root)
modif_label = Label(modify, text="modifications")
modif_label.grid(row=0, column=0)
modify.configure(background='aqua')
im4 = Image.open('/home/pennywise/ship6.jpg')
im4 = im4.resize((1200, 600), Image.ANTIALIAS)
tkimage4 = PIL.ImageTk.PhotoImage(im4)
myvar4 = Label(modify, image=tkimage4)
myvar4.place(x=0, y=0, relwidth=1, relheight=1)
myvar4.image = tkimage4

cancel = Frame(root)
cancel_label = Label(cancel, text="order cancellation")
cancel_label.grid(row=0, column=0)
cancel.configure(background='aqua')
im3 = Image.open('/home/pennywise/ship7.jpg')
im3 = im3.resize((1200, 600), Image.ANTIALIAS)
tkimage3 = PIL.ImageTk.PhotoImage(im3)
myvar3 = Label(cancel, image=tkimage3)
myvar3.place(x=0, y=0, relwidth=1, relheight=1)
myvar3.image = tkimage3

window = Frame(root, bg='white')
heading = Label(window, text="LOGIN PAGE")
heading.grid(row=0, column=0)
window.rowconfigure('all', minsize=200)
window.columnconfigure('all', minsize=200)
im2 = Image.open('/home/pennywise/ship1.jpg')
im2 = im2.resize((1200, 610), Image.ANTIALIAS)
tkimage2 = PIL.ImageTk.PhotoImage(im2)
myvar2 = Label(window, image=tkimage2)
myvar2.place(x=0, y=0, relwidth=1, relheight=1)
myvar2.image = tkimage2

for frame in cancel, modify, display, inventory_form, window:
    frame.grid(row=0, column=0, sticky='news')

pid = Label(inventory_form, text="product id", fg="blue", bg="white")
pid.grid(row=3, column=0)
id = Entry(inventory_form)
id.grid(row=3, column=1)
pname = Label(inventory_form, text="product name", fg="blue", bg="white")
pname.grid(row=5, column=0)
prod_name = Entry(inventory_form)
prod_name.grid(row=5, column=1)
ship_identification_number = Label(inventory_form, text="ship id", fg="blue", bg="white")
ship_identification_number.grid(row=7)
shipid = Entry(inventory_form)
shipid.grid(row=7, column=1)
container_identification = Label(inventory_form, text="container id", fg="blue", bg="white")
container_identification.grid(row=9)
cont_id = Entry(inventory_form)
cont_id.grid(row=9, column=1)
del_date = Label(inventory_form, text="delivery date", fg="blue", bg="white")
del_date.grid(row=11)
deli_date = Entry(inventory_form)
deli_date.grid(row=11, column=1)
ord_date = Label(inventory_form, text="order date", fg="blue", bg="white")
ord_date.grid(row=13)
orde_date = Entry(inventory_form)
orde_date.grid(row=13, column=1)
port_ident = Label(inventory_form, text="port_id", fg="blue", bg="white")
port_ident.grid(row=15)
port_identiti = Entry(inventory_form)
port_identiti.grid(row=15, column=1)
port_nam = Label(inventory_form, text="Port name", fg="blue", bg="white")
port_nam.grid(row=17)
port_na = Entry(inventory_form)
port_na.grid(row=17, column=1)
source_add = Label(inventory_form, text="From Address", fg="blue", bg="white")
source_add.grid(row=19)
source_address = Entry(inventory_form)
source_address.grid(row=19, column=1)
dest_address = Label(inventory_form, text="Destination Address", fg="blue", bg="white")
dest_address.grid(row=21)
dest_add = Entry(inventory_form)
dest_add.grid(row=21, column=1)
text = Text(inventory_form, height=20, width=50)
text.grid(row=26, column=1)

submit = Button(inventory_form, text="SUBMIT", command=enter_into_db)
submit.grid(row=25, column=0)

prod_id = Button(display, text="search", command=search, fg="blue", bg="white")
prod_id.grid(row=1, column=4)
p_name = Label(display, text="product id/name", fg="blue", bg="white")
p_name.grid(row=1, column=0)
take_id = Entry(display)
take_id.grid(row=1, column=3)
search_results = Text(display)
search_results.grid(row=25, column=3)

p = Label(modify, text="product id", fg="blue", bg="white")
p.grid(row=1, column=1)
pi = Entry(modify)
pi.grid(row=1, column=2)
contact_id = Label(modify, text="contact info", fg="blue", bg="white")
contact_id.grid(row=2, column=1)
c = Entry(modify)
c.grid(row=2, column=2)
submit2 = Button(modify, text="submit", command=modifico, fg="blue", bg="white")
submit2.grid(row=3, column=1)

order_id = Label(cancel, text="product id", fg="blue", bg="white")
order_id.grid(row=2, column=0)
o = Entry(cancel)
o.grid(row=2, column=1)
cancel_submit = Button(cancel, text="submit", command=del_order, fg="blue", bg="white")
cancel_submit.grid(row=2, column=2)
tbox = Text(cancel, height=1, width=40)
tbox.grid(row=125)

User_name = Label(window, text="User_name", fg="blue", bg="white")
User_name.grid(row=710, column=320)
e1 = Entry(window)
e1.grid(row=710, column=321)
user_password = Label(window, text="user_password", fg="blue", bg="white")
user_password.grid(row=716, column=320)
e2 = Entry(window)
e2.grid(row=716, column=321)
login = Button(window, text="login", command=check_credentials, fg="blue", bg="white")
login.grid(row=720, column=321)
# next=Button(window,text="form",command=lambda:raise_frame(inventory_form),fg="blue",bg="white")
# next.grid(row=720,column=311)

next = Button(cancel, text="form", command=lambda: raise_frame(inventory_form), fg="blue", bg="white")
next.grid(row=2, column=250)
next2 = Button(cancel, text="display", command=lambda: raise_frame(display), fg="blue", bg="white")
next2.grid(row=3, column=250)
to_modify = Button(cancel, text="modify", command=lambda: raise_frame(modify), fg="blue", bg="white")
to_modify.grid(row=4, column=250)

next = Button(modify, text="form", command=lambda: raise_frame(inventory_form), fg="blue", bg="white")
next.grid(row=1, column=250)
next2 = Button(modify, text="display", command=lambda: raise_frame(display), fg="blue", bg="white")
next2.grid(row=2, column=250)
to_delete = Button(modify, text="cancellation", command=lambda: raise_frame(cancel), fg="blue", bg="white")
to_delete.grid(row=3, column=250)

next = Button(display, text="form", command=lambda: raise_frame(inventory_form), fg="blue", bg="white")
next.grid(row=21, column=250)
to_delete = Button(display, text="cancellation", command=lambda: raise_frame(cancel), fg="blue", bg="white")
to_delete.grid(row=22, column=250)
to_modify = Button(display, text="modify", command=lambda: raise_frame(modify), fg="blue", bg="white")
to_modify.grid(row=23, column=250)

next2 = Button(inventory_form, text="display", command=lambda: raise_frame(display), fg="blue", bg="white")
next2.grid(row=2, column=250)
to_delete = Button(inventory_form, text="cancellation", command=lambda: raise_frame(cancel), fg="blue", bg="white")
to_delete.grid(row=3, column=250)
to_modify = Button(inventory_form, text="modify", command=lambda: raise_frame(modify), fg="blue", bg="white")
to_modify.grid(row=4, column=250)

root.mainloop()