import pymysql

#Database connection from Python
db = pymysql.connect("localhost","root","","INVENTORY_MANAGEMENT" )
cursor = db.cursor()



cursor.execute("DROP TABLE IF EXISTS PERSON")
cursor.execute("DROP TABLE IF EXISTS WAREHOUSE")
cursor.execute("DROP TABLE IF EXISTS PRODUCTS")
cursor.execute("DROP TABLE IF EXISTS SHIPS")
cursor.execute("DROP TABLE IF EXISTS PORTS")
cursor.execute("DROP TABLE IF EXISTS DATE_TIME")


#Creation of WAREHOUSE table
sql_warehouse="""CREATE TABLE WAREHOUSE(
    W_SOURCE_ID INT,
    W_DESTINATION_ID INT,
    SOURCE CHAR(20) NOT NULL,
    DESTINATION CHAR(20) NOT NULL,
    PRIMARY KEY (W_SOURCE_ID,W_DESTINATION_ID))"""

cursor.execute(sql_warehouse)


#Creation of PORTS table
sql_ports="""CREATE TABLE PORTS(
    PORT_ID INT PRIMARY KEY,
    PORT_NAME CHAR(20) NOT NULL,
    WHICH_SOURCE_ID INT REFERENCES WAREHOUSE(W_SOURCE_ID),
    WHICH_DESTINATION_ID INT REFERENCES WAREHOUSE(W_DESTINATION_ID))"""

cursor.execute(sql_ports)


#Creation of SHIPS table
sql_ships="""CREATE TABLE SHIPS(
   SHIP_ID INT PRIMARY KEY,
   SHIP_NAME CHAR(20) NOT NULL,
   IN_PORT_ID INT REFERENCES PORTS(PORT_ID)
    )"""

cursor.execute(sql_ships)


#Creation of PRODUCTS table
sql_products="""CREATE TABLE PRODUCTS(
    PRODUCT_ID INT PRIMARY KEY,
    PRODUCT_NAME CHAR(20) NOT NULL,
    IN_SHIP_ID INT REFERENCES SHIPS(SHIP_ID))"""

cursor.execute(sql_products)



#Creation of PERSON table
sql_person = """CREATE TABLE PERSON(
   PERSON_ID INT PRIMARY KEY,
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20) NOT NULL,
   PHONE_NUMBER LONG NOT NULL,
   EMAIL_ID CHAR(20),
   PROD_ID INT REFERENCES PRODUCTS(PRODUCT_ID))"""


  # DEPARTURE_DATE1 REFERENCES DATE_TIME(DEPARTURE_DATE) ,
  # DEPARTURE_TIME1 REFERENCES DATE_TIME(DEAPRTURE_TIME),
  # DELIVERY_DATE1 REFERENCES DATE_TIME(DELIVERY_DATE),
  # DELIVERY_TIME1 REFERENCES DATE_TIME(DELIVERY_TIME)
  # PRIMARY KEY(DEPARTURE_DATE,DEPARTURE_TIME,DELIVERY_DATE,DELIVERY_TIME))"""
cursor.execute(sql_person)



#Creation of DATE_TIME table
sql_datetime="""CREATE TABLE DATE_TIME(
   DEPARTURE_DATE DATE ,
   DEPARTURE_TIME TIME , 
   DELIVERY_DATE DATE ,
   DELIVERY_TIME TIME,
    PER_ID INT REFERENCES PERSON(PERSON_ID))"""


cursor.execute(sql_datetime)



#Insertion of values into WAREHOUSE table
sql_warehouse1="""INSERT INTO WAREHOUSE VALUES(101,201,'SOURCE1','DESTINATION1')"""
cursor.execute(sql_warehouse1)
sql_warehouse2="""INSERT INTO WAREHOUSE VALUES(102,202,'SOURCE2','DESTINATION2')"""
cursor.execute(sql_warehouse2)
sql_warehouse3="""INSERT INTO WAREHOUSE VALUES(103,203,'SOURCE3','DESTINATION3')"""
cursor.execute(sql_warehouse3)
sql_warehouse4="""INSERT INTO WAREHOUSE VALUES(104,204,'SOURCE4','DESTINATION4')"""
cursor.execute(sql_warehouse4)
sql_warehouse5="""INSERT INTO WAREHOUSE VALUES(105,205,'SOURCE5','DESTINATION5')"""
cursor.execute(sql_warehouse5)
sql_warehouse6="""INSERT INTO WAREHOUSE VALUES(106,206,'SOURCE6','DESTINATION6')"""
cursor.execute(sql_warehouse6)
sql_warehouse7="""INSERT INTO WAREHOUSE VALUES(107,207,'SOURCE7','DESTINATION7')"""
cursor.execute(sql_warehouse7)
sql_warehouse8="""INSERT INTO WAREHOUSE VALUES(108,208,'SOURCE8','DESTINATION8')"""
cursor.execute(sql_warehouse8)
sql_warehouse9="""INSERT INTO WAREHOUSE VALUES(109,209,'SOURCE9','DESTINATION9')"""
cursor.execute(sql_warehouse9)
sql_warehouse10="""INSERT INTO WAREHOUSE VALUES(110,210,'SOURCE10','DESTINATION10')"""
cursor.execute(sql_warehouse10)
sql_warehouse11="""INSERT INTO WAREHOUSE VALUES(111,211,'SOURCE11','DESTINATION11')"""
cursor.execute(sql_warehouse11)
sql_warehouse12="""INSERT INTO WAREHOUSE VALUES(112,212,'SOURCE12','DESTINATION12')"""
cursor.execute(sql_warehouse12)
sql_warehouse13="""INSERT INTO WAREHOUSE VALUES(113,213,'SOURCE13','DESTINATION13')"""
cursor.execute(sql_warehouse13)
sql_warehouse14="""INSERT INTO WAREHOUSE VALUES(114,214,'SOURCE14','DESTINATION14')"""
cursor.execute(sql_warehouse14)
sql_warehouse15="""INSERT INTO WAREHOUSE VALUES(115,215,'SOURCE15','DESTINATION15')"""
cursor.execute(sql_warehouse15)


#Insertion of values into PORTS table
sql_ports1="""INSERT INTO PORTS VALUES(11,'PORT1',101,201)"""
cursor.execute(sql_ports1)
sql_ports2="""INSERT INTO PORTS VALUES(12,'PORT2',102,201)"""
cursor.execute(sql_ports2)
sql_ports3="""INSERT INTO PORTS VALUES(13,'PORT3',101,203)"""
cursor.execute(sql_ports3)
sql_ports4="""INSERT INTO PORTS VALUES(14,'PORT4',104,204)"""
cursor.execute(sql_ports4)
sql_ports5="""INSERT INTO PORTS VALUES(15,'PORT5',105,205)"""
cursor.execute(sql_ports5)
sql_ports6="""INSERT INTO PORTS VALUES(16,'PORT6',106,206)"""
cursor.execute(sql_ports6)
sql_ports7="""INSERT INTO PORTS VALUES(17,'PORT7',107,207)"""
cursor.execute(sql_ports7)
sql_ports8="""INSERT INTO PORTS VALUES(18,'PORT8',108,208)"""
cursor.execute(sql_ports8)
sql_ports9="""INSERT INTO PORTS VALUES(19,'PORT9',109,209)"""
cursor.execute(sql_ports9)
sql_ports10="""INSERT INTO PORTS VALUES(20,'PORT10',110,210)"""
cursor.execute(sql_ports10)
sql_ports11="""INSERT INTO PORTS VALUES(21,'PORT11',111,211)"""
cursor.execute(sql_ports11)
sql_ports12="""INSERT INTO PORTS VALUES(22,'PORT12',112,212)"""
cursor.execute(sql_ports12)
sql_ports13="""INSERT INTO PORTS VALUES(23,'PORT13',113,213)"""
cursor.execute(sql_ports13)
sql_ports14="""INSERT INTO PORTS VALUES(24,'PORT14',114,214)"""
cursor.execute(sql_ports14)
sql_ports15="""INSERT INTO PORTS VALUES(25,'PORT15',115,215)"""
cursor.execute(sql_ports15)


#Insertion of values into SHIPS table
sql_ships1="""INSERT INTO SHIPS VALUES(601,'SHIP1',11)"""
cursor.execute(sql_ships1)
sql_ships2="""INSERT INTO SHIPS VALUES(602,'SHIP2',12)"""
cursor.execute(sql_ships2)
sql_ships3="""INSERT INTO SHIPS VALUES(603,'SHIP3',13)"""
cursor.execute(sql_ships3)
sql_ships4="""INSERT INTO SHIPS VALUES(604,'SHIP4',14)"""
cursor.execute(sql_ships4)
sql_ships5="""INSERT INTO SHIPS VALUES(605,'SHIP5',15)"""
cursor.execute(sql_ships5)
sql_ships6="""INSERT INTO SHIPS VALUES(606,'SHIP6',16)"""
cursor.execute(sql_ships6)
sql_ships7="""INSERT INTO SHIPS VALUES(607,'SHIP7',17)"""
cursor.execute(sql_ships7)
sql_ships8="""INSERT INTO SHIPS VALUES(608,'SHIP8',18)"""
cursor.execute(sql_ships8)
sql_ships9="""INSERT INTO SHIPS VALUES(609,'SHIP9',19)"""
cursor.execute(sql_ships9)
sql_ships10="""INSERT INTO SHIPS VALUES(610,'SHIP10',20)"""
cursor.execute(sql_ships10)
sql_ships11="""INSERT INTO SHIPS VALUES(611,'SHIP11',21)"""
cursor.execute(sql_ships11)
sql_ships12="""INSERT INTO SHIPS VALUES(612,'SHIP12',22)"""
cursor.execute(sql_ships12)
sql_ships13="""INSERT INTO SHIPS VALUES(613,'SHIP13',23)"""
cursor.execute(sql_ships13)
sql_ships14="""INSERT INTO SHIPS VALUES(614,'SHIP14',24)"""
cursor.execute(sql_ships14)
sql_ships15="""INSERT INTO SHIPS VALUES(615,'SHIP15',25)"""
cursor.execute(sql_ships15)



#Insertion of values into PRODUCTS table
sql_products1="""INSERT INTO PRODUCTS VALUES(1001,'PRODUCT1',601)"""
cursor.execute(sql_products1)
sql_products2="""INSERT INTO PRODUCTS VALUES(1002,'PRODUCT2',601)"""
cursor.execute(sql_products2)
sql_products3="""INSERT INTO PRODUCTS VALUES(1003,'PRODUCT3',601)"""
cursor.execute(sql_products3)
sql_products4="""INSERT INTO PRODUCTS VALUES(1004,'PRODUCT4',604)"""
cursor.execute(sql_products4)
sql_products5="""INSERT INTO PRODUCTS VALUES(1005,'PRODUCT5',605)"""
cursor.execute(sql_products5)
sql_products6="""INSERT INTO PRODUCTS VALUES(1006,'PRODUCT6',606)"""
cursor.execute(sql_products6)
sql_products7="""INSERT INTO PRODUCTS VALUES(1007,'PRODUCT7',607)"""
cursor.execute(sql_products7)
sql_products8="""INSERT INTO PRODUCTS VALUES(1008,'PRODUCT8',608)"""
cursor.execute(sql_products8)
sql_products9="""INSERT INTO PRODUCTS VALUES(1009,'PRODUCT9',609)"""
cursor.execute(sql_products9)
sql_products10="""INSERT INTO PRODUCTS VALUES(1010,'PRODUCT10',610)"""
cursor.execute(sql_products10)
sql_products11="""INSERT INTO PRODUCTS VALUES(1011,'PRODUCT11',611)"""
cursor.execute(sql_products11)
sql_products12="""INSERT INTO PRODUCTS VALUES(1012,'PRODUCT12',612)"""
cursor.execute(sql_products12)
sql_products13="""INSERT INTO PRODUCTS VALUES(1013,'PRODUCT13',613)"""
cursor.execute(sql_products13)
sql_products14="""INSERT INTO PRODUCTS VALUES(1014,'PRODUCT14',614)"""
cursor.execute(sql_products14)
sql_products15="""INSERT INTO PRODUCTS VALUES(1015,'PRODUCT15',615)"""
cursor.execute(sql_products15)

db.commit()

#Insertion of values into PERSON table
sql_person1="""INSERT INTO PERSON VALUES(10001,'SON','GOKU',9000000001,'abc1@gmail.com',1001)"""
cursor.execute(sql_person1)
sql_person2="""INSERT INTO PERSON VALUES(10002,'SON','GOHAN',9000000002,'abc2@gmail.com',1002)"""
cursor.execute(sql_person2)
sql_person3="""INSERT INTO PERSON VALUES(10003,'SON','GOTEN',9000000003,'abc3@gmail.com',1003)"""
cursor.execute(sql_person3)
sql_person4="""INSERT INTO PERSON VALUES(10004,'FUTURE','TRUNKS',9000000004,'abc4@gmail.com',1004)"""
cursor.execute(sql_person4)
sql_person5="""INSERT INTO PERSON VALUES(10005,'BRUCE','WAYNE',9000000005,'abc5@gmail.com',1005)"""
cursor.execute(sql_person5)
sql_person6="""INSERT INTO PERSON VALUES(10006,'CLARK','KENT',9000000006,'abc6@gmail.com',1006)"""
cursor.execute(sql_person6)
sql_person7="""INSERT INTO PERSON VALUES(10007,'BARRY','ALLEN',9000000007,'abc7@gmail.com',1007)"""
cursor.execute(sql_person7)
sql_person8="""INSERT INTO PERSON VALUES(10008,'NARUTO','NAMIKAZE',9000000008,'abc8@gmail.com',1008)"""
cursor.execute(sql_person8)
sql_person9="""INSERT INTO PERSON VALUES(10009,'HARRY','POTTER',9000000009,'abc9@gmail.com',1009)"""
cursor.execute(sql_person9)
sql_person10="""INSERT INTO PERSON VALUES(10010,'SIRIUS','BLACK',9000000010,'abc10@gmail.com',1010)"""
cursor.execute(sql_person10)
sql_person11="""INSERT INTO PERSON VALUES(10011,'LIGHT','YAGAMI',9000000011,'abc11@gmail.com',1011)"""
cursor.execute(sql_person11)
sql_person12="""INSERT INTO PERSON VALUES(10012,'SHIKAMARU','NARA',9000000012,'abc12@gmail.com',1012)"""
cursor.execute(sql_person12)
sql_person13="""INSERT INTO PERSON VALUES(10013,'MADARA','UCHIHA',9000000013,'abc13@gmail.com',1013)"""
cursor.execute(sql_person13)
sql_person14="""INSERT INTO PERSON VALUES(10014,'HANZO','HASASHI',9000000014,'abc14@gmail.com',1014)"""
cursor.execute(sql_person14)
sql_person15="""INSERT INTO PERSON VALUES(10015,'LIU','KANG',9000000015,'abc15@gmail.com',1015)"""
cursor.execute(sql_person15)

db.commit()

#Insertion of values into DATE_TIME table
sql_datetime1="""INSERT INTO DATE_TIME VALUES('2017-01-10','10:00:00','2017-02-11','16:00:00',10000)"""
cursor.execute(sql_datetime1)
sql_datetime2="""INSERT INTO DATE_TIME VALUES('2017-01-15','11:00:00','2017-03-11','17:00:00',10001)"""
cursor.execute(sql_datetime2)
sql_datetime3="""INSERT INTO DATE_TIME VALUES('2017-03-10','06:00:00','2017-04-12','18:00:00',10003)"""
cursor.execute(sql_datetime3)
sql_datetime4="""INSERT INTO DATE_TIME VALUES('2017-01-30','10:30:00','2017-02-20','15:00:00',10004)"""
cursor.execute(sql_datetime4)
sql_datetime5="""INSERT INTO DATE_TIME VALUES('2017-04-10','10:45:00','2017-05-11','16:00:00',10005)"""
cursor.execute(sql_datetime5)
sql_datetime6="""INSERT INTO DATE_TIME VALUES('2017-04-21','14:50:00','2017-05-09','07:00:00',10006)"""
cursor.execute(sql_datetime6)
sql_datetime7="""INSERT INTO DATE_TIME VALUES('2017-11-12','11:00:00','2017-12-11','16:30:00',10007)"""
cursor.execute(sql_datetime7)
sql_datetime8="""INSERT INTO DATE_TIME VALUES('2017-10-14','09:00:00','2018-02-11','17:10:00',10008)"""
cursor.execute(sql_datetime8)
sql_datetime9="""INSERT INTO DATE_TIME VALUES('2017-02-08','08:00:00','2017-04-11','16:30:00',10009)"""
cursor.execute(sql_datetime9)
sql_datetime10="""INSERT INTO DATE_TIME VALUES('2017-03-09','07:00:00','2017-06-11','16:00:00',10010)"""
cursor.execute(sql_datetime10)
sql_datetime11="""INSERT INTO DATE_TIME VALUES('2017-04-11','10:00:00','2017-09-11','01:00:00',10011)"""
cursor.execute(sql_datetime11)
sql_datetime12="""INSERT INTO DATE_TIME VALUES('2017-06-10','10:00:00','2017-07-11','14:00:00',10012)"""
cursor.execute(sql_datetime12)
sql_datetime13="""INSERT INTO DATE_TIME VALUES('2017-04-20','10:00:00','2017-06-11','13:00:00',10013)"""
cursor.execute(sql_datetime13)
sql_datetime14="""INSERT INTO DATE_TIME VALUES('2017-07-10','10:00:00','2017-10-30','12:00:00',10014)"""
cursor.execute(sql_datetime14)
sql_datetime15="""INSERT INTO DATE_TIME VALUES('2017-09-10','10:00:00','2018-01-20','11:00:00',10015)"""
cursor.execute(sql_datetime15)

db.commit()

while(1):
    print "Enter"
    print "1.INSERT"
    print "2.SEARCH"
    print "3.DELETE"
    print "4.DISPLAY"
    print "5.UPDATE"
    print "6.EXIT"
    option=input("Select the option")
    type(option)
    if option==1:
        print "Select the table"
        print "1.WAREHOUSE"
        print "2.PORTS"
        print "3.SHIPS"
        print "4.PRODUCTS"
        print "5.PERSON"
        print "6.DATE_TIME"
        option_table=input("Select the table to insert the values")
        type(option_table)
        if option_table==1:

             cursor.execute("INSERT INTO WAREHOUSE VALUES (%s, %s, %s, %s)",
                     (raw_input("W_SOURCE_ID: "), raw_input("W_DESTINATION_ID: "),
                      raw_input("SOURCE: "), raw_input("DESTINATION: ") ))


        if option_table==2:
            cursor.execute("INSERT INTO PORTS VALUES (%s, %s, %s)",
                           (raw_input("PORT_ID: "), raw_input("PORT_NAME: "),
                   raw_input("WHICH_SOURCE_ID: "),raw_input("WHICH_DESTINATION_ID:")))


        if option_table==3:
            cursor.execute("INSERT INTO SHIPS VALUES (%s, %s, %s)",
                           (raw_input("SHIP_ID: "), raw_input("SHIP_NAME: "),
                            raw_input("IN_PORT_ID: ") ))


        if option_table==4:

            cursor.execute("INSERT INTO PRODUCTS VALUES (%s, %s, %s)",
                           (raw_input("PRODUCT_ID: "), raw_input("PRODUCT_NAME: "),
                            raw_input("IN_SHIP_ID: ")))


        if option_table==5:
            cursor.execute("INSERT INTO PERSON VALUES (%s, %s, %s, %s,%s,%s)",
                           (raw_input("PERSON_ID: "), raw_input("FIRST_NAME: "),
                            raw_input("LAST_NAME: "), raw_input("PHONE_NUMBER: "),
                             raw_input("EMAIL_ID"),raw_input("PROD_ID")))


        if option_table==6:
            cursor.execute("INSERT INTO DATE_TIME VALUES (%s, %s, %s, %s,%s)",
                           (raw_input("DEPARTURE_DATE: "), raw_input("DEPARTURE_TIME: "),
                            raw_input("DELIVERY_DATE: "), raw_input("DELIVERY_TIME: "),
                            raw_input("PER_ID")))

    elif option==2:
        print "SELECT THE TABLE"
        print "1.WAREHOUSE"
        print "2.PORTS"
        print "3.SHIPS"
        print "4.PRODUCTS"
        print "5.PERSON"
        print "6.DATE_TIME"

        option_search = input("Select the table to obtain the row")
        type(option_search)


        if option_search==1:
            while (1):
                op_search_value = raw_input("Enter the W_SOURCE_ID to get the row")
                try:
                    op_search_value = int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM WAREHOUSE WHERE W_SOURCE_ID=%s", (op_search_value))
                    row_search = cursor.fetchone()
                    if row_search is not None:
                        print row_search
                        break
                    else:
                        print  "Enter the SOURCE_ID which exists in db"
                except:
                    print "Invalid option"



        if option_search==2:
            while (1):
                op_search_value = raw_input("Enter the PORT_ID to get the row")
                try:
                    op_search_value = int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM PORTS WHERE PORT_ID=%s", (op_search_value))
                    row_search = cursor.fetchone()
                    if row_search is not None:
                        print row_search
                        break
                    else:
                        print  "Enter the PORT_ID which exists in db"
                except:
                    print "Invalid option"



        if option_search==3:
             while(1):
                op_search_value=input("Enter the SHIP_ID to get the row")
                try:
                    op_search_value=int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM SHIPS WHERE SHIP_ID=%s",(op_search_value))
                    row_search=cursor.fetchone()
                    if row_search is not None:
                        print row_search
                        break
                    else:
                       print  "Enter the SHIP_ID which exists in db"
                except:
                     print "Invalid option"





        if option_search==4:
             while(1):
                op_search_value=raw_input("Enter the PRODUCT_ID to get the row")
                try:
                    op_search_value=int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=%s",(op_search_value))
                    row_search=cursor.fetchone()
                    if row_search is not None:
                       print row_search
                       break
                    else:
                       print  "Enter the PRODUCT_ID which exists in db"
                except:
                     print "Invalid option"



        if option_search==5:
            while (1):
                op_search_value = raw_input("Enter the PERSON_ID to get the row")
                try:
                    op_search_value = int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM PERSON WHERE PERSON_ID=%s", (op_search_value))
                    row_search = cursor.fetchone()
                    if row_search is not None:
                        print row_search
                        break
                    else:
                        print  "Enter the PERSON_ID which exists in db"
                except:
                    print "Invalid option"



        if option_search==6:
            while (1):
                op_search_value = raw_input("Enter the PER_ID to get the row")
                try:
                    op_search_value = int(op_search_value)
                    type(op_search_value)
                    cursor.execute("SELECT * FROM DATE_TIME WHERE PER_ID=%s", (op_search_value))
                    row_search = cursor.fetchone()
                    if row_search is not None:
                        print row_search
                        break
                    else:
                        print  "Enter the PER_ID which exists in db"
                except:
                    print "Invalid option"





    elif option==3:
        print "SELECT THE TABLE"
        print "1.WAREHOUSE"
        print "2.PORTS"
        print "3.SHIPS"
        print "4.PRODUCTS"
        print "5.PERSON"
        print "6.DATE_TIME"
        op_delete = input("Enter the table to get the row deleted")
        type(op_delete)

        if op_delete == 1:
            while(1):
                  op_delete_value=raw_input("Enter the W_SOURCE_ID to delete the row")
                  try:
                        op_delete_value = int(op_delete_value)
                        type(op_delete_value)

                        print op_delete_value

                        cursor.execute("SELECT * FROM WAREHOUSE WHERE W_SOURCE_ID=%s", (op_delete_value))

                        row_delete = cursor.fetchone()
                        print row_delete
                        if row_delete is not None:
                            print "ROW EXISTS"
                            cursor.execute("DELETE FROM WAREHOUSE WHERE W_SOURCE_ID=%s", (op_delete_value))
                            print "The row containg the given W_SOURCE_ID is deleted"
                            print "The remaining contents of the table"
                            db.commit()
                            cursor.execute("SELECT * FROM WAREHOUSE")
                            row_val = cursor.fetchone()
                            while row_val is not None:
                                print row_val
                                row_val = cursor.fetchone()

                            break
                        else:
                            print  "Enter the W_SOURCE_ID which exists in db"

                  except :
                        print "Invalid option"


        if op_delete == 2:
            while (1):
                op_delete_value = raw_input("Enter the PORT_ID to delete the row")
                try:
                    op_delete_value = int(op_delete_value)
                    type(op_delete_value)

                    print op_delete_value

                    cursor.execute("SELECT * FROM PORTS WHERE PORT_ID=%s", (op_delete_value))

                    row_delete = cursor.fetchone()
                    print row_delete
                    if row_delete is not None:
                        print "ROW EXISTS"
                        cursor.execute("DELETE FROM PORTS WHERE PORT_ID=%s", (op_delete_value))
                        print "The row containg the given PORT_ID is deleted"
                        print "The remaining contents of the table"
                        db.commit()
                        cursor.execute("SELECT * FROM PORTS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PORT_ID which exists in db"

                except:
                    print "Invalid option"

        if op_delete == 3:
            while (1):
                op_delete_value = raw_input("Enter the SHIP_ID to delete the row")
                try:
                    op_delete_value = int(op_delete_value)
                    type(op_delete_value)

                    print op_delete_value

                    cursor.execute("SELECT * FROM SHIPS WHERE SHIP_ID=%s", (op_delete_value))

                    row_delete = cursor.fetchone()
                    print row_delete
                    if row_delete is not None:
                        print "ROW EXISTS"
                        cursor.execute("DELETE FROM SHIPS WHERE SHIP_ID=%s", (op_delete_value))
                        print "The row containg the given SHIP_ID is deleted"
                        print "The remaining contents of the table"
                        db.commit()
                        cursor.execute("SELECT * FROM SHIPS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the SHIP_ID which exists in db"

                except:
                    print "Invalid option"

        if op_delete == 4:
            while (1):
                op_delete_value = raw_input("Enter the PRODUCT_ID to delete the row")
                try:
                    op_delete_value = int(op_delete_value)
                    type(op_delete_value)

                    print op_delete_value

                    cursor.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=%s", (op_delete_value))

                    row_delete = cursor.fetchone()
                    print row_delete
                    if row_delete is not None:
                        print "ROW EXISTS"
                        cursor.execute("DELETE FROM PRODUCTS WHERE PRODUCT_ID=%s", (op_delete_value))
                        print "The row containg the given W_SOURCE_ID is deleted"
                        print "The remaining contents of the table"
                        db.commit()
                        cursor.execute("SELECT * FROM PRODUCTS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PRODUCT_ID which exists in db"

                except:
                    print "Invalid option"

        if op_delete == 5:
            while (1):
                op_delete_value = raw_input("Enter the PERSON_ID to delete the row")
                try:
                    op_delete_value = int(op_delete_value)
                    type(op_delete_value)

                    print op_delete_value

                    cursor.execute("SELECT * FROM PERSON WHERE PERSON_ID=%s", (op_delete_value))

                    row_delete = cursor.fetchone()
                    print row_delete
                    if row_delete is not None:
                        print "ROW EXISTS"
                        cursor.execute("DELETE FROM PERSON WHERE PERSON_ID=%s", (op_delete_value))
                        print "The row containg the given W_SOURCE_ID is deleted"
                        print "The remaining contents of the table"
                        db.commit()
                        cursor.execute("SELECT * FROM PERSON")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PERSON_ID which exists in db"

                except:
                    print "Invalid option"

        if op_delete == 6:
            while (1):
                op_delete_value = raw_input("Enter the PER_ID to delete the row")
                try:
                    op_delete_value = int(op_delete_value)
                    type(op_delete_value)

                    print op_delete_value

                    cursor.execute("SELECT * FROM DATE_TIME WHERE PER_ID=%s", (op_delete_value))

                    row_delete = cursor.fetchone()
                    print row_delete
                    if row_delete is not None:
                        print "ROW EXISTS"
                        cursor.execute("DELETE FROM DATE_TIME WHERE PER_ID=%s", (op_delete_value))
                        print "The row containg the given PER_ID is deleted"
                        print "The remaining contents of the table"
                        db.commit()
                        cursor.execute("SELECT * FROM DATE_TIME")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PER_ID which exists in db"

                except:
                    print "Invalid option"

    elif option==4:
         print "SELECT THE TABLE"
         print "1.WAREHOUSE"
         print "2.PORTS"
         print "3.SHIPS"
         print "4.PRODUCTS"
         print "5.PERSON"
         print "6.DATE_TIME"
         option_display=input("Enter the option_display")
         type(option_display)


         if option_display==1:

            print "Executing the query to fetch all rows\n"
            cursor.execute("""SELECT * FROM WAREHOUSE""")
            row=cursor.fetchone()
            #print cursor.fetchall()
            while row is not None:
              print row
              row=cursor.fetchone()


         if option_display==2:

             print "Executing the query to fetch all rows\n"
             cursor.execute("""SELECT * FROM PORTS""")
             row = cursor.fetchone()
             # print cursor.fetchall()
             while row is not None:
                print row
                row = cursor.fetchone()


         if option_display==3:

             print "Executing the query to fetch all rows\n"
             cursor.execute("""SELECT * FROM SHIPS""")
             row = cursor.fetchone()
             # print cursor.fetchall()
             while row is not None:
                print row
                row = cursor.fetchone()


         if option_display==4:

             print "Executing the query to fetch all rows\n"
             cursor.execute("""SELECT * FROM PRODUCTS""")
             row = cursor.fetchone()
             # print cursor.fetchall()
             while row is not None:
                print row
                row = cursor.fetchone()


         if option_display==5:

             print "Executing the query to fetch all rows\n"
             cursor.execute("""SELECT * FROM PERSON""")
             row = cursor.fetchone()
             # print cursor.fetchall()
             while row is not None:
                print row
                row = cursor.fetchone()


         if option_display==6:

             print "Executing the query to fetch all rows\n"
             cursor.execute("""SELECT * FROM DATE_TIME""")
             row = cursor.fetchone()
             # print cursor.fetchall()
             while row is not None:
                print row
                row = cursor.fetchone()

         db.commit()

    elif option==5:
        print "SELECT THE TABLE"
        print "1.WAREHOUSE"
        print "2.PORTS"
        print "3.SHIPS"
        print "4.PRODUCTS"
        print "5.PERSON"
        print "6.DATE_TIME"
        op_update = input("Enter the table to get the row updated")
        type(op_update)

        if op_update == 1:
            while (1):
                op_update_id = raw_input("Enter the W_SOURCE_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_source=raw_input("Enter the SOURCE name")
                    type(op_update_source)
                    op_update_dest=raw_input("Enter the DESTINATION name")
                    type(op_update_dest)
                    cursor.execute("SELECT * FROM WAREHOUSE WHERE W_SOURCE_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE WAREHOUSE SET SOURCE=%s,DESTINATION=%s WHERE W_SOURCE_ID=%s", (op_update_source,op_update_dest,op_update_id))
                        print "The row containg the given W_SOURCE_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM WAREHOUSE")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the W_SOURCE_ID which exists in db"

                except:
                    print "Invalid option"

        elif op_update==2:
            while (1):
                op_update_id = raw_input("Enter the PORT_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_port=raw_input("Enter the PORT name")
                    type(op_update_port)
                    cursor.execute("SELECT * FROM PORTS WHERE PORT_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE PORTS SET =%s WHERE PORT_ID=%s", (op_update_port,op_update_id))
                        print "The row containg the given PORT_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM PORTS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PORT_ID which exists in db"

                except:
                    print "Invalid option"


        elif op_update==3:
            while (1):
                op_update_id = raw_input("Enter the SHIP_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_ship=raw_input("Enter the SHIP name")
                    type(op_update_ship)
                    cursor.execute("SELECT * FROM SHIPS WHERE SHIP_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE WAREHOUSE SET SHIP=%s WHERE W_SOURCE_ID=%s", (op_update_ship,op_update_id))
                        print "The row containg the given SHIP_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM SHIPS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the SHIP_ID which exists in db"

                except:
                    print "Invalid option"

        elif op_update==4:
            while (1):
                op_update_id = raw_input("Enter the PRODUCT_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_product=raw_input("Enter the PRODUCT name")
                    type(op_update_product)
                    cursor.execute("SELECT * FROM PRODUCTS WHERE PRODUCT_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE PRODUCTS SET PRODUCT_NAME=%s WHERE PRODUCT_ID=%s", (op_update_product,op_update_id))
                        print "The row containg the given PRODUCT_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM PRODUCTS")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PRODUCT_ID which exists in db"

                except:
                    print "Invalid option"



        elif op_update==5:
            while (1):
                op_update_id = raw_input("Enter the PERSON_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_first=raw_input("Enter the First name")
                    type(op_update_first)
                    op_update_last=raw_input("Enter the Last name")
                    type(op_update_last)
                    op_update_phone=raw_input("Enter the Phone number")
                    type(op_update_phone)
                   # op_update_phone=long(op_update_phone)
                    op_update_email=raw_input("Enter the Mail id")
                    type(op_update_email)
                    cursor.execute("SELECT * FROM PERSON WHERE PERSON_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE PERSON SET FIRST_NAME=%s,LAST_NAME=%s,PHONE_NUMBER=%s,EMAIL_ID=%s WHERE PERSON_ID=%s", (op_update_first,op_update_last,op_update_phone,op_update_email,op_update_id))
                        print "The row containg the given PERSON_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM PERSON")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PERSON_ID which exists in db"

                except Exception,e:
                    print e
                    print "Invalid option"


        elif op_update==6:
            while (1):
                op_update_id = raw_input("Enter the PER_ID to update")
                try:
                    op_update_id = int(op_update_id)
                    type(op_update_id)
                    print op_update_id
                    op_update_dedate=raw_input("Enter the Departure Date")
                    type(op_update_dedate)
                    op_update_detime=raw_input("Enter the Destination Time")
                    type(op_update_detime)
                    op_update_ddate = raw_input("Enter the Delivery Date")
                    type(op_update_ddate)
                    op_update_dtime=raw_input("Enter the Delivery Time")
                    type(op_update_dtime)
                    cursor.execute("SELECT * FROM DATE_TIME WHERE PER_ID=%s", (op_update_id))
                    row_update = cursor.fetchone()
                    print row_update
                    if row_update is not None:
                        print "ROW EXISTS"
                        cursor.execute("UPDATE DATE_TIME SET DEPARTURE_DATE=%s,DEPARTURE_TIME=%s,DELIVERY_DATE=%s,DELIVERY_TIME=%s WHERE PER_ID=%s", (op_update_dedate,op_update_detime,op_update_ddate,op_update_dtime,op_update_id))
                        print "The row containg the given PER_ID is updated"
                        print "The contents of the table after update"
                        db.commit()
                        cursor.execute("SELECT * FROM DATE_TIME")
                        row_val = cursor.fetchone()
                        while row_val is not None:
                            print row_val
                            row_val = cursor.fetchone()

                        break
                    else:
                        print  "Enter the PER_ID which exists in db"

                except:
                    print "Invalid option"



    elif option==6:
        db.commit()
        db.close()
        exit()



    db.commit()

sql_test="""SELECT SOURCE FROM WAREHOUSE WHERE W_SOURCE_ID=113"""
cursor.execute(sql_test)
print cursor.fetchall()
  #   print "Executing the query to fetch all rows\n"
 #   cursor.execute("""SELECT * FROM PERSON""")
 #   row=cursor.fetchone()
   #print cursor.fetchall()
 #   while row is not None:
 #      print row
 #      row=cursor.fetchone()
db.commit()
db.close()

