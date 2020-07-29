import os
import sqlite3 as sql

passMaster = 'admin'

def logPass(getPass):
    if getPass == passMaster:
        return True
    else:
        return False
def addValuePass (namePass, passPass):

    banc = sql.connect('/home/pedro/Documentos/Projetos_Programação/Projetos Abertos/python-projects/SimplePassword/pass.db')
    passBanc = banc.cursor()
    #passBanc.execute("CREATE TABLE password (name text, password_ text)")
    passBanc.execute("SELECT * FROM password")  
    passBanc.execute("INSERT INTO password VALUES('{}', '{}')".format(namePass,passPass))
    banc.commit()
    banc.close()
def delValuePass (check, nameDelPass):
    if check == True:
        banc = sql.connect('/home/pedro/Documentos/Projetos_Programação/Projetos Abertos/python-projects/SimplePassword/pass.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")  
        passBanc.execute("DELETE from password WHERE name = '{}'".format(nameDelPass))
        banc.commit()
        banc.close()
    else:
        input('operação cancelada, senha incorreta\npress enter')
login = input('Enter de Password.:')

if logPass(login) == True:

    while True:

        os.system('clear')
        menu = input('\n************************** \n'
                        '* SimplePasswordManager  * \n'
                        '* rp : register password * \n'
                        '* qp : query passowrd    * \n'
                        '* dp : delete password   * \n'
                        '* ex : exit for looping  * \n'
                        '*    ----- info -----    * \n'
                        '************************** \n'
                        '...:').upper()
        
        if menu == 'EX':
            print('going out...')
            break
        elif menu == 'RP':
            passName = input('enter name pass .:')
            passPass = input('enter password .:')
            addValuePass(passName, passPass)
        elif menu == 'QP':
            banc = sql.connect('/home/pedro/Documentos/Projetos_Programação/Projetos Abertos/python-projects/SimplePassword/pass.db')
            passBanc = banc.cursor()
            passBanc.execute("SELECT* FROM password")
            contpass = passBanc.fetchall()

            for x in range(0, len(contpass)):
                print('----->', x , ' ', contpass[x])

            banc.commit()
            banc.close()
            input('press enter to exit')
        elif menu == 'DP':
            loginDel = input('enter masterPass .:')
            if logPass(loginDel) == True:
                nameDeletePass = input('enter the password name to delete .:')
                delValuePass(True,nameDeletePass)
            else:
                delValuePass(False,None)  
        elif  menu == 'INFO':
            print( 
            '  dev_create: Pedro Henrique Quadros Pirralha\n'
            '  nameProduct: SimplePasswordManager\n'
            '  version: 0.0.1 \n'
            '  não comercializado, sem estrutura de qualidade e segurança')
            input('\npress enter')
        else:
            print('digite uma opção valida')
            input('press enter')
else:
    print('\n--senha errada, reinicie o programa para tentar novamente--')
print('\nend')
