# ================= Author = AdiYaksa.
# This python database tool project is still being worked on.
# You can continue this project to help complete this project
# This source code is free and you can use it to modify it or other,
# And you can upload it to github or join this project collaboration
# To speed up the project database tool.
# ================= Thanks You For Using My Project.


# ! Dont Forget Pip Install This !
# pip install mysql-connector-python
# pip install art
import mysql.connector
from mysql.connector import Error
import os
import time
from art import *
import sys

arow = "-"*50

# Def Database
def db():
        try:
    # Database set up connect to host
    # ================= Database Connect Setup.
            db = mysql.connector.connect(
                # Host
                host = "localhost",
                # Username
                username  ="root",
                # Password
                password = "",
                # Database
                database = "user_py"
            )
   # ===================== Def Main.
            def main():
                os.system("cls")
                name = input("\n[INFORMATION] Input your name: ")
                if name == "":
                   print("[REQUIRED] Input your name!")
                   time.sleep(0.9)
                   os.system("cls")
                   connected()
                else: 
                 def done():
                    cursor = db.cursor()
                    os.system("cls")
                    print("\n")
                    print(arow)
                    tprint("Database Tool",font="bulbhead")
                    print(arow)
                    time.sleep(1)
                    mysql = db.get_server_info()
                    host = db.server_host
                    port = db.server_port
                    database = db.database
                    print("Mysql Version: ",mysql)
                    print("Host: ",host)
                    print("Port: ",port)    
                    print("Use Database: ", database)
                    print("Halo, Hola, Hai, Helo",name)
                    print(arow)
                    time.sleep(1)
                    menu = input("\n[DATABASE TOOL PYTHON]\n[a].Show Databases\n[b].Show Tables\n[c].Select Tables\n[d].Desc Tables\n[e].Change Database\n[f].Input Tables\nSelect Menu: ")
                    if menu == 'a':
                        os.system("cls")
                        show = "show databases"
                        cursor.execute(show)
                        result_show = cursor.fetchall()
                        print("\n")
                        print(arow)
                        print("Show Databases: ")
                        print(arow)
                        for i in result_show:
                            print(i[0])
                        print(arow)
                        print("Done Result Database")
                        print(arow)
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                    elif menu == 'b':
                        os.system("cls")
                        show1 = "show tables"
                        cursor.execute(show1)
                        print("\n")
                        print(arow)
                        print("Show Tables: ")
                        print(arow)
                        show_tables = cursor.fetchall()
                        for lk in show_tables:
                            print(lk[0])
                        print(arow)
                        print("Done Result Tables")
                        print(arow)
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                    elif menu == 'c':
                        os.system("cls")
                        print("\n[INFORMATION] You can show tables in menu")
                        select_from = input("[DATABASE] Input name tables for show: ")
                        delete = "select * from "+ select_from +""
                        cursor.execute(delete)
                        select_from_result = cursor.fetchall()
                        print("\n")
                        print(arow)
                        print("Show From Tables: ")
                        print(arow)
                        for asd in select_from_result:
                                print(asd)
                        print(arow)
                        print("Done Result From")
                        print(arow)
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                    elif menu == 'd':
                        os.system("cls")
                        select_from = input("\n[DATABASE] Input name tables for desc: ")
                        delete = "desc "+ select_from +""
                        cursor.execute(delete)
                        select_from_result = cursor.fetchall()
                        print("\n")
                        print(arow)
                        print("Show From Tables: ")
                        print(arow)
                        for asd in select_from_result:
                                print(asd)
                        print(arow)
                        print("Done Result From")
                        print(arow)
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                    elif menu == 'e':
                        os.system("cls")
                        database = input("\n[INFORMATION] Input name database for change db: ")
                        change_db = "use "+ database +""
                        cursor.execute(change_db)
                        print("[INFORMATION] Done change database")
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                    elif menu == 'f':
                        os.system("cls")
                        input_db = input("\n[INFORMATION] Want insert table?: ")
                        username_input = input("[INFORMATION] Input data username: ") # you can change for values
                        password_input = input("[INFORMATION] Input data password: ") # you can change for values
                        select_01 = "insert into "+ input_db +"(username, password) values('"+ username_input +"', '"+ password_input +"') " # change username and password
                        # to desc database you
                        # execute
                        cursor.execute(select_01)
                        print("[INFORMATION] Done input database.")
                        ulang = input("[INFORMATION] Want back to menu? [y/n]: ")
                        if ulang == 'y':
                            done()
                        else:
                            print("Bayy Thanks For Using Me (:")
                            time.sleep(1.5)
                            sys.exit()
                done()      
            
            def connected():
              if db.is_connected():
                     main()    
  
            connected()            
  # ===================== Except Error.
        except Error as e:
            print("\nMysql / Database Error: ", e)
            ulang = input("[INFORMATION] Want back to try restart? [y/n]: ")
            if ulang == 'y':
                     connected()
            else:
                print("Bayy Thanks For Using Me (:")
                time.sleep(1.5)
                sys.exit()
                   


db()

# ====================== This project is not yet fully completed, 
# it is still in the development of the database tool.
# ===================== My Github: adiyaksabackend
