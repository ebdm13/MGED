from tkinter import *
from selenium import webdriver
import time


def run():
    pass_mark = []
    general_pass_mark = 0
    coef = []
    username = username_entry.get()
    password = password_entry.get()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path="Package/chromedriver.exe", chrome_options=options)
    driver.get("https://www.ecoledirecte.com/Eleves/4124/Notes")
    user_bar = driver.find_element_by_id("username")
    passwd_bar = driver.find_element_by_id("password")
    user_bar.send_keys(username)
    passwd_bar.send_keys(password)
    driver.find_element_by_id("connexion").click()
    time.sleep(10)
    driver.find_element_by_id("btn-encart-moyennes").click()
    time.sleep(3)
    all_mark = driver.find_elements_by_class_name("moyenneeleve")
    all_coef = driver.find_elements_by_class_name('coef')
    coef_liste = []

    for mark in all_mark:
        pass_mark.append(mark.text)

    for coef in all_coef:
        coef_liste.append(coef.text)

    del pass_mark[0]
    del coef_liste[0]

    while '' in pass_mark:
        for i in pass_mark:
            if i == '':
                counter = pass_mark.index(i)
                del pass_mark[counter]
                del coef_liste[counter]

    pass_mark = [float(i.replace(",", ".")) for i in pass_mark]
    coef_liste = [int(i) for i in coef_liste]

    v1 = 0
    v2 = 0

    for i in pass_mark:
        counter = pass_mark.index(i)
        v1 += pass_mark[counter] * coef_liste[counter]
        v2 += coef_liste[counter]

    general_pass_mark = v1 / v2
    return general_pass_mark


window = Tk()
window.title("Moyenne Générale école directe")
window.geometry("720x480")
window.iconbitmap("Package/logo.ico")
window.config(background='#1076EA')

frame = Frame(window, bg='#1076EA')


def run_and_calculate():
    m_general = run()
    moyenne_title = Label(frame, text=("votre moyenne générale est: \n" + str(m_general)), font=("Calibri", 20),
                          bg="#1076EA",
                          fg="white")
    moyenne_title.pack()


label_title = Label(window, text="Calculez Votre Moyenne général d'Ecole Directe !", font=("Calibri", 25), bg="#1076EA",
                    fg="white")
label_title.pack()

connection_title = Label(frame, text="connectez-vous ici !", font=("Calibri", 25), bg="#1076EA",
                         fg="white")
connection_title.pack(padx=120)

username_entry = Entry(frame, text="username", width=40, font=("Calibri", 20))
password_entry = Entry(frame, text="password", width=40, font=("Calibri", 20), show='•')

username_entry.pack(padx=40, pady=10, ipady=5)
password_entry.pack(padx=40, pady=10, ipady=5)

run_button = Button(frame, text="Run", font=("Calibri", 25), bg="white", fg="#1076EA", command=run_and_calculate)
run_button.pack(ipadx=30, ipady=10, pady=30)

frame.pack(expand=YES)

# afficher la fenettre
window.mainloop()
