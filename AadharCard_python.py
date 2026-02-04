# This is a Project of Data Storage & generation  of Aadhar Number.
# Data is stored in MySQl database and we can export our data in a Text file.

# In this project we imported `pymysql` and `randon` library.
# At first we created a database named `AadharCard`, a  table named `Data` in it, and used it.
# Then we provided two options to the user.
# 1. To axcess their Aadhar data by entering their Aadhar Number.
# 2. To create a new Aadhar Card by entering their details.
# In both the options we provided an option to export their data in a text file.
# In option 2 we generated a unique 12-digit Aadhar Number for the user.
# Finally we closed the database connection.
# --------  IMPORTING LIBRARIES  -------
import pymysql
import random

# --------  CREATING DATABASE AND TABLE  --------
db = pymysql.connect(host = 'localhost' , port = 3306,
                     user = 'root',
                     password = 'Galaxy1234')

cur = db.cursor()
cur.execute("create database if not exists AadharCard;")
print("Database AadharCard created successfully.")

cur.execute("use AadharCard;")
cur.execute("""create table if not exists Data(`Serial No.` integer auto_increment primary key,`Aadhar Number` varchar(12) not null unique,Name varchar(30) not null,`Father's Name` varchar(30) not null, `Mobile Number` varchar(10) not null , Email varchar(30) ,State enum("Jammu and Kashmir","Ladakh","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Delhi","Lakshadweep","Puducherry","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal") not null, City varchar(30) not null, Location varchar(60) not null, `Pin Code` integer(6) not null);""")
print("Table created successfully.")
# cur.execute(""" alter table data add column Gender enum("Male" , "Female");""")
# print("Gender Column added.")
# cur.execute("""alter table data modify Gender enum("Male" ,"Female") after `Father's Name`;""")
# print("Table successfully modified.")


print(" ** This is a project ** \n")
print("      Welcome to Aadhar      \n")
# --------  OPTIONS  --------
while True:
    a = int(input("1. Do you want to axcess your Aadhar data (press 1) \n 2.Do you want to create a Aadhar Card (press 2) \n Enter your Choice : "))

    if a in(1,2):
        break
    else:
        print("ERROR : \n Invalid Input \n 1 = To axcess Aadhar Card. \n 2 = To create Aadhar Card. \n  ")


# --------  FUNCTION TO EXPORT AADHAR DATA TO TEXT FILE  --------
def export_aadhar_to_text_file():
    while True:
            ques = input("Do you want the data in text file\n 1. Yes \n2.No \n Enter Your choice : ")
            if ques in ("Yes","yes","y","1"):
                with open("Aadhar_data.txt","w") as file:
                    file.write(" ----- AADHAR DATA -----\n")
                    file.write(f"Aadhar Number : {record[1]} \n")
                    file.write(f"Name  : {record[2]} \n")
                    file.write(f"Father's Name  : {record[3]} \n")
                    file.write(f"Gender : {record[4]} \n")
                    file.write(f"Mobile Number : {record[5]} \n")
                    file.write(f" Email Address : {record[6]} \n")
                    file.write(f" State : {record[7]} \n")
                    file.write(f"City  : {record[8]} \n")
                    file.write(f"Location  : {record[9]} \n")
                    file.write(f"Pin Code  : {record[10]} \n")
                    file.close()
                print("Text file created.\nThanks For Visiting.")
                break
            elif ques in ("No", "no", "n", "2"):
                print("Thanks For Visiting.")
                break
            else:
                print("Invalid Input.")


# --------  OPTION 1      TO AXCESS THE DATA  --------
if a ==1:
    while True:
        aa = input("Enter your Aadhar Card Number : ")

        if aa.isdigit() and len(aa) ==12:
            break
        else:
            print("Enter your correct Aadhar Number")
        if len(aa) !=12:
            print(f"Your Aadhar number carries {len(aa)}-digits not 12-digits.")

    cur.execute("""Select * from Data where `Aadhar Number` = %s""", (aa,))
    record = cur.fetchone()
    # print(f"record = {record}")
    if record:
        print("\n Aadhar Data Found :")
        print(record)

        export_aadhar_to_text_file()

    else:
        print(" \n ERROR :  \n Aadhar Data Not Found. \n")

    # print(f"a = {a}")
    # print(f"aa = {aa}")




# --------  OPTION 2      TO CREATE THE AADHAR CARD  --------

elif a ==2:
    # --------  FUNCTION TO GENERATE UNIQUE AADHAR NUMBER  --------
    def generate_aadhar():
        while True:
            first_digit = random.randint(1,9)
            remaining = "".join(str(random.randint(0,9)) for _ in range(11))
            concatinate = str(first_digit) + remaining

            cur.execute("""select 1 from data where `Aadhar Number` = %s""",(concatinate,))
            if cur.fetchone() is None:
                return concatinate
    aadhar = generate_aadhar()
    # print(aadhar)

# --------  TAKING USER'S DATA AS INPUT  --------
    data = {
        "Aadhar Number" : aadhar,
        "Name" : input("Enter Your Name : "),
        "Father's Name" : input("Enter Your Father's Name : "),
        "Gender" : input("Enter your Gender : "),
        "Mobile Number" : int(input("Enter Your Mobile Number : ")),
        "Email" : input("Enter Your Email : "),
        "State" : input("Enter your State's Name : "),
        "City" : input("Enter Your City Name : "),
        "Location" : input("Enter Your Home Address : "),
        "Pin Code" : int(input("Enter Your Pin Code : "))
    }
    print(data.values())
# --------  CONFIRMATION AND INSERTING DATA INTO TABLE  --------
    confirm = input("Are you sure wants to Submit your data (1. Yes, 2. No)\n Enter your choice : ").lower()
    if(confirm in("yes", "y", "1")):
        cur.execute("""insert into Data(`Aadhar Number`,Name,`Father's Name`, `Gender`, `Mobile Number`,Email, State, City, Location, `Pin Code`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",tuple(data.values()))
        db.commit()
        print("\n Aadhar Card created successfully.")
        print(f"Aadhar Number  =  {data["Aadhar Number"]}")

        cur.execute("""Select * from Data where `Aadhar Number` = %s""", (aadhar,))
        record = cur.fetchone()
        # print(f"record = {record}")
        if record:
            print("\n Aadhar Data Found :")
            print(record)

            # Export the Aadhar data to a text file
            export_aadhar_to_text_file()
            db.close()
    elif(confirm in("no", "n", "2")):
        print("No")
    else:
        print("Invalid Input. ")