# spmDef-nc = SimplePasswordManager def no color

import sqlite3 as sql
#SAIR/FECHAR
def close():
    input('press enter')

#CONFIRMAÇÃO DA SENHA
passMaster = '1'
def logPass(getPass):
    if getPass == passMaster:
        return True
    else:
        return False

#Acessando e criando tabelas no banco de dados
def AcessBanc():
    try:
        banc = sql.connect('spmNC.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")
    except:
        passBanc.execute("CREATE TABLE password (name text, password_ text)")

#ADICIONANDO SENHAS COM NOME NO BANCO DE DADOS
def addValuePass (namePass, passPass):
    banc = sql.connect('spmNC.db')
    passBanc = banc.cursor()
    passBanc.execute("SELECT * FROM password")  
    passBanc.execute("INSERT INTO password VALUES('{}', '{}')".format(namePass,passPass))
    banc.commit()
    banc.close()

#EXCLUINDO SENHAS DO BANCO DE DADOS
def delValuePass (check, nameDelPass):
    if check == True:
        banc = sql.connect('spmNC.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")  
        passBanc.execute("DELETE from password WHERE name = '{}'".format(nameDelPass))
        banc.commit()
        banc.close()
    else:
        print('operação cancelada, senha incorreta --> ',end='')
        close()

#interface do sistema / interface via terminal / interface Menu - Principal
def interfaceMenu():
    Menu = input(
    f'\n|=*=*=*=*=*=*=*=*=*=*=*=*=*=*| \n'
    f'|  -SimplePasswordManager-   | \n'
    f'|  rp : -register password-  | \n'
    f'|  sp : -show passwords-     | \n'
    f'|  dp : -delete password-    | \n'
    f'|  gp : -generate password-  | \n'
    f'|  ex : -exit for looping-   | \n'
    f'|     ------ info ------     | \n'
    f'| - - - - - - - - --> +more+ | \n'
    f'|=*=*=*=*=*=*=*=*=*=*=*=*=*=*| \n...:'
    ).upper()
    return Menu

# Interface do sistema/ interface via terminal / interface MenuMore
def interfaceMenuMore():
    MenuMore = input(
      f'\n|=*=*=*=*=*=*=*=*=*=*=*=*=*=*| \n'
        f'|- - - --->   More option    | \n'
        f'| dd : -delete database-     | \n'
        f'|<<<<<< press enter to >>>>>>| \n'
        f'|<<<<<< return to menu >>>>>>| \n'
        f'|=*=*=*=*=*=*=*=*=*=*=*=*=*=*| \n...:'
        ).upper()

    return MenuMore
