# This Tkinter App is coded by nonsogospel(Oguchukwu Gospel)
# A Mini Tkinter Registration Form App
# Just trying to playing with some cool things
from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image, ImageTk

# Defining the main Window
windowmain = Tk()
windowmain.geometry("1280x1024")
windowmain.title("Mini Registration Form App Using Tkinter")

# Defining like the logo at the top
imageheader = Image.open("justimages/blank_avatar.png")
photoheader = ImageTk.PhotoImage(imageheader)
lab = Label(image=photoheader)
lab.pack()

# Defining the Nav Bar Menu
menu = Menu(windowmain)
windowmain.config(menu=menu)



# Defining the various textboxes for Labels
lname = StringVar()
fname = StringVar()
uname = StringVar()
dob = StringVar()
country = StringVar()
gender = StringVar()
password1 = StringVar()
password2 = StringVar()
username_s = StringVar()
password_s = StringVar()

# Defining the functions for the buttons
def signUp():
    last_name = lname.get()
    first_name = fname.get()
    user_name = uname.get()
    date_birth = dob.get()
    your_country = country.get()
    your_gender = gender.get()
    password_first = password1.get()
    password_second = password2.get()
    if password_first == password_second:
        conn = sqlite3.connect("Register.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS User (LName TEXT, FName TEXT, UName TEXT, DOB TEXT, Country TEXT, Gender TEXT, Passworda TEXT, Passwordb TEXT)')
            cursor.execute('INSERT INTO User(LName,FName,UName,DOB,Country,Gender,Passworda,Passwordb) VALUES(?,?,?,?,?,?,?,?)', (last_name, first_name, user_name, date_birth, your_country, your_gender, password_first,password_second))
            conn.commit()
            # cursor.execute("SELECT * FROM User WHERE DOB=?",(date_birth,))
            # rows = cursor.fetchone()
            # if rows:
            #   print("Exists")
            
            # else:
            #   print("Failed")


    else:
        tkinter.messagebox.showinfo("Error", "Passwords does not match")

    logIn()

def logIn():
    loginwindow = Tk()
    loginwindow.title("WELCOME TO THE LOGIN SCREEN")
    loginwindow.geometry("1366x768")
    label0a = Label(loginwindow, text="LOGIN", width=20, font=("Bookman Old Style", 23, "bold"), fg="black")
    label0a.pack()

    entry01a = Entry(loginwindow, textvar=username_s)
    entry01a.insert(0, 'USERNAME')
    entry01a.place(x=577, y=155, width=190, height=40)

    entry02a = Entry(loginwindow, textvar=password_s)
    entry02a.insert(0, 'PASSWORD')
    entry02a.place(x=576, y=230, width=190, height=40)

    login_btn2 = Button(loginwindow, text="LOG IN", width=54, bg="green", fg="white", command=success)
    login_btn2.place(x=467, y=300)



def success():
  user_name = uname.get()
  conn = sqlite3.connect("Register.db")
  with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User WHERE UName=?",(user_name,))
    rows = cursor.fetchone()
    if rows:
      successwindow = Tk()
      successwindow.title("LOGIN SUCCESSFUL")
      successwindow.geometry("1366x768")
    else:
      tkinter.messagebox.showinfo("Error", "Invalid Credentials")
  # x = 100
  # if x == 0:
  #   print('WELCOME')
  # else:
  #   exit()










def exitWindow():
    exit()

def about():
    tkinter.messagebox.showinfo("A Mini Registration App", "Created by nonsogospel")



# Declaring the Nav Bar Menu Now
dropmenu1 = Menu(menu)
menu.add_cascade(label="File", menu=dropmenu1)
dropmenu1.add_command(label="Exit", command=exitWindow)

dropmenu2 = Menu(menu)
menu.add_cascade(label="View", menu=dropmenu2)
dropmenu2.add_command(label="About", command=about)



# Top text
label00 = Label(windowmain, text="REGISTRATION FORM", width=20, font=("Bookman Old Style", 23, "bold"), fg="black")
label00.pack()

labelwarning = Label(windowmain, text="Ensure you fill all fields corrrectly", font=("Georgia", 9, "italic"))
labelwarning.pack()

# Last Name Field
label01 = Label(windowmain, text="Last Name :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label01.place(x=440, y=150)
entry01 = Entry(windowmain, textvar=lname)
entry01.place(x=750, y=155)

# First Name Field
label02 = Label(windowmain, text="First Name :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label02.place(x=440, y=200)
entry02 = Entry(windowmain, textvar=fname)
entry02.place(x=750, y=205)

# Create user Name
label03 = Label(windowmain, text="Create Username :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label03.place(x=460, y=250)
entry03 = Entry(windowmain, textvar=uname)
entry03.place(x=750, y=257)

# Date of Birth
label04 = Label(windowmain, text="Date of Birth :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label04.place(x=440, y=300)
entry04 = Entry(windowmain, textvar=dob)
entry04.place(x=750, y=306)

# Country
label05 = Label(windowmain, text="Country :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label05.place(x=420, y=350)

# Gender
label06 = Label(windowmain, text="Gender :", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label06.place(x=410, y=400)

# Create password
label07 = Label(windowmain, text="Enter a password: ", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label07.place(x=450, y=450)
entry07 = Entry(windowmain, textvar=password1, show="*")
entry07.place(x=750, y=453)


# Reenter password
label08 = Label(windowmain, text="Re-enter password: ", width=20, font=("MoolBoran", 19, "bold"), fg="black")
label08.place(x=460, y=500)
entry08 = Entry(windowmain, textvar=password2, show="*")
entry08.place(x=750, y=505)

# Defining the Country Dropdown
countrydrop = ['Afghanistan',
               'Albania',
               'Algeria',
               'Andorra',
               'Angola',
               'Antigua & Deps',
               'Argentina',
               'Armenia',
               'Australia',
               'Austria',
               'Azerbaijan',
               'Bahamas',
               'Bahrain',
               'Bangladesh',
               'Barbados',
               'Belarus',
               'Belgium',
               'Belize',
               'Benin',
               'Bhutan',
               'Bolivia',
               'Bosnia Herzegovina',
               'Botswana',
               'Brazil',
               'Brunei',
               'Bulgaria',
               'Burkina',
               'Burundi',
               'Cambodia',
               'Cameroon',
               'Canada',
               'Cape Verde',
               'Central African Rep',
               'Chad',
               'Chile',
               'China',
               'Colombia',
               'Comoros',
               'Congo',
               'Congo {Democratic Rep}',
               'Costa Rica',
               'Croatia',
               'Cuba',
               'Cyprus',
               'Czech Republic',
               'Denmark',
               'Djibouti',
               'Dominica',
               'Dominican Republic',
               'East Timor',
               'Ecuador',
               'Egypt',
               'El Salvador',
               'Equatorial Guinea',
               'Eritrea',
               'Estonia',
               'Ethiopia',
               'Fiji',
               'Finland',
               'France',
               'Gabon',
               'Gambia',
               'Georgia',
               'Germany',
               'Ghana',
               'Greece',
               'Grenada',
               'Guatemala',
               'Guinea',
               'Guinea-Bissau',
               'Guyana',
               'Haiti',
               'Honduras',
               'Hungary',
               'Iceland',
               'India',
               'Indonesia',
               'Iran',
               'Iraq',
               'Ireland {Republic}',
               'Israel',
               'Italy',
               'Ivory Coast',
               'Jamaica',
               'Japan',
               'Jordan',
               'Kazakhstan',
               'Kenya',
               'Kiribati',
               'Korea North',
               'Korea South',
               'Kosovo',
               'Kuwait',
               'Kyrgyzstan',
               'Laos',
               'Latvia',
               'Lebanon',
               'Lesotho',
               'Liberia',
               'Libya',
               'Liechtenstein',
               'Lithuania',
               'Luxembourg',
               'Macedonia',
               'Madagascar',
               'Malawi',
               'Malaysia',
               'Maldives',
               'Mali',
               'Malta',
               'Marshall Islands',
               'Mauritania',
               'Mauritius',
               'Mexico',
               'Micronesia',
               'Moldova',
               'Monaco',
               'Mongolia',
               'Montenegro',
               'Morocco',
               'Mozambique',
               'Myanmar, {Burma}',
               'Namibia',
               'Nauru',
               'Nepal',
               'Netherlands',
               'New Zealand',
               'Nicaragua',
               'Niger',
               'Nigeria',
               'Norway',
               'Oman',
               'Pakistan',
               'Palau',
               'Panama',
               'Papua New Guinea',
               'Paraguay',
               'Peru',
               'Philippines',
               'Poland',
               'Portugal',
               'Qatar',
               'Romania',
               'Russian Federation',
               'Rwanda',
               'St Kitts & Nevis',
               'St Lucia',
               'Saint Vincent & the Grenadines',
               'Samoa',
               'San Marino',
               'Sao Tome & Principe',
               'Saudi Arabia',
               'Senegal',
               'Serbia',
               'Seychelles',
               'Sierra Leone',
               'Singapore',
               'Slovakia',
               'Slovenia',
               'Solomon Islands',
               'Somalia',
               'South Africa',
               'South Sudan',
               'Spain',
               'Sri Lanka',
               'Sudan',
               'Suriname',
               'Swaziland',
               'Sweden',
               'Switzerland',
               'Syria',
               'Taiwan',
               'Tajikistan',
               'Tanzania',
               'Thailand',
               'Togo',
               'Tonga',
               'Trinidad & Tobago',
               'Tunisia',
               'Turkey',
               'Turkmenistan',
               'Tuvalu',
               'Uganda',
               'Ukraine',
               'United Arab Emirates',
               'United Kingdom',
               'United States',
               'Uruguay',
               'Uzbekistan',
               'Vanuatu',
               'Vatican City',
               'Venezuela',
               'Vietnam',
               'Yemen',
               'Zambia',
               'Zimbabwe']
dropcountry = OptionMenu(windowmain, country, *countrydrop)
country.set("select country")
dropcountry.config(width=16)
dropcountry.place(x=750, y=347)

# Defining the button for the Gender Field
rad1 = Radiobutton(windowmain, text="Male", variable="gender", value="Male")
rad1.place(x=750, y=403)
rad2 = Radiobutton(windowmain, text="Female", variable="gender", value="Female")
rad2.place(x=810, y=403)

# Defining the buttons
signup_btn = Button(windowmain, text="Register", width=12, bg="green", fg="white", command=signUp)
signup_btn.place(x=500, y=550)
windowmain.bind("<Return>", signUp)

login_btn = Button(windowmain, text="Log In", width=12, bg="green", fg="white", command=logIn)
login_btn.place(x=700, y=550)

exit_btn = Button(windowmain, text="Exit", width=12, bg="brown", fg="white", command=exitWindow)
exit_btn.place(x=600, y=610)


windowmain.mainloop()
