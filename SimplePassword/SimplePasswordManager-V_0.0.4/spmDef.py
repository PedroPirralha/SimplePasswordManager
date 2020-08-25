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
        banc = sql.connect('spm.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")
    except:
        passBanc.execute("CREATE TABLE password (name text, password_ text)")

#ADICIONANDO SENHAS COM NOME NO BANCO DE DADOS
def addValuePass (namePass, passPass):
    banc = sql.connect('spm.db')
    passBanc = banc.cursor()
    passBanc.execute("SELECT * FROM password")  
    passBanc.execute("INSERT INTO password VALUES('{}', '{}')".format(namePass,passPass))
    banc.commit()
    banc.close()

#EXCLUINDO SENHAS DO BANCO DE DADOS
def delValuePass (check, nameDelPass):
    if check == True:
        banc = sql.connect('spm.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")  
        passBanc.execute("DELETE from password WHERE name = '{}'".format(nameDelPass))
        banc.commit()
        banc.close()
    else:
        print('operação cancelada, senha incorreta --> ',end='')
        close()

color = {'red':'\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'cyan' : '\033[36m',
    'magenta' : '\033[35m',
    'yellow' : '\033[33m',
    'black' : '\033[30m',
    'white' : '\033[37m',
    'clear' : '\033[0;0m',
    'bold' : '\033[1m',
    'reverse' : '\033[2m',
    'black-b' : '\033[40m', #-b from background
    'red-b' : '\033[41m',
    'green-b' : '\033[42m',
    'yellow-b' : '\033[43m',
    'blue-b' : '\033[44m',
    'magenta-b' : '\033[45m',
    'cyan-b' : '\033[46m',
    'white-b' : '\033[47m' 
    }
red = color['red'] 
green = color['green']
bold = color['bold']
yellowB = color['yellow']
cyan = color['cyan']
blue = color['blue']
reverse = color['reverse']
cl = color['clear']
def interfaceMenu():
    menu = input(
                f'\n{blue}|****************************|{cl} \n'
                f'{blue}| {green} -SimplePasswordManager-   {blue}|{cl} \n'
                f'{blue}| {red} rp :{cyan} -register password-  {blue}|{cl} \n'
                f'{blue}| {red} sp :{cyan} -show passwords-     {blue}|{cl} \n'
                f'{blue}| {red} dp :{cyan} -delete password-    {blue}|{cl} \n'
                f'{blue}| {red} ex :{cyan} -exit for looping-   {blue}|{cl} \n'
                f'{blue}| {red} gp :{cyan} -generate password-  {blue}|{cl} \n'
                f'{blue}| {red} - - - - - - - --->{green} +more+ {blue}|{cl} \n'
                f'{blue}| {green}    ------ info ------     {blue}|{cl} \n'
                f'{blue}|****************************|{cl} \n...:'
                ).upper()
    return menu

def interfaceMenuMore():
    MenuMore = input(
        f'\n{cyan}|=*=*=*=*=*=*=*=*=*=*=*=*=*=|{cl}\n'
        f'{cyan}|{red}       More Options        {cyan}|{cl} \n'
        f'{cyan}|{green}   dd: {blue}delete database     {cyan}|{cl} \n'
        f'{cyan}|{yellowB} <<<< {cl}{red}press enter to {cl}{yellowB}>>>>> {cl}{cyan}|{cl} \n'
        f'{cyan}|{yellowB} <<<< {cl}{red}return to menu {cl}{yellowB}>>>>> {cl}{cyan}|{cl} \n'
        f'{cyan}|=*=*=*=*=*=*=*=*=*=*=*=*=*=|{cl}\n'
          ).upper()

    return MenuMore
