import sqlite3 as sql
from random import shuffle


passMaster = 'admin'

#SAIR/FECHAR
def close():
    input('press enter')

#LIMPAR TERMINAL
def clear():
    print('\n\n' * 150)

#CONFIRMAÇÃO DA SENHA
def logPass(getPass):
    if getPass == passMaster:
        return True
    else:
        return False

#ADICIONANDO SENHAS COM NOME NO BANCO DE DADOS
def addValuePass (namePass, passPass):
    banc = sql.connect('pass.db')
    passBanc = banc.cursor()
    #passBanc.execute("CREATE TABLE password (name text, password_ text)")
    passBanc.execute("SELECT * FROM password")  
    passBanc.execute("INSERT INTO password VALUES('{}', '{}')".format(namePass,passPass))
    banc.commit()
    banc.close()

#EXCLUINDO SENHAS DO BANCO DE DADOS
def delValuePass (check, nameDelPass):
    if check == True:
        banc = sql.connect('pass.db')
        passBanc = banc.cursor()
        passBanc.execute("SELECT * FROM password")  
        passBanc.execute("DELETE from password WHERE name = '{}'".format(nameDelPass))
        banc.commit()
        banc.close()
    else:
        input('operação cancelada, senha incorreta')
        close()

login = input('Enter de Password.:')

#INICIALIZAÇÃO DO PROGRAMA
if logPass(login) == True:
    while True:
        clear()
        #INTERFACE DO PROGRAMA 
        menu = input(
            f'\n|****************************| \n'
            f'|  -SimplePasswordManager-   | \n'
            f'|  rp : -register password-  | \n'
            f'|  sp : -show passwords-     | \n'
            f'|  dp : -delete password-    | \n'
            f'|  ex : -exit for looping-   | \n'
            f'|  gp : -generate password-  | \n'
            f'|     ------ info ------     | \n'
            f'|****************************| \n...:'
            ).upper()
        #OPÇÃO PARA SAIR DO PROGRAMA
        if menu == 'EX':
            print('going out...')
            break
        #OPÇÃO PARA REGISTRAR UMA SENHA
        elif menu == 'RP':
            passName = input('enter name pass .:')
            passPass = input('enter password .:')
            addValuePass(passName, passPass)
        #OPÇÃO PARA MOSTRAR SENHAS
        elif menu == 'SP':
            banc = sql.connect('pass.db')
            passBanc = banc.cursor()
            passBanc.execute("SELECT* FROM password")
            contpass = passBanc.fetchall()
            for x in range(0, len(contpass)):
                print('----->', x , ' ', contpass[x])
            banc.commit()
            banc.close()
            close()
        #OPÇÃO PARA DELETAR SENHAS 
        elif menu == 'DP':
            loginDel = input('enter masterPass .:')
            if logPass(loginDel) == True:
                nameDeletePass = input('enter the password name to delete .:')
                delValuePass(True,nameDeletePass)
            else:
                delValuePass(False,None)  
        #OPÇÃO PARA GERAR SENHAS
        elif menu == 'GP':
            print('generated password level 8/10\n')
            letters = ["a", "e", "i", "o", "u",
                    "b", "c", "d", "f", "g", "h",
	                "j", "k", "l", "m", "n", "p",
	                "q", "r", "s", "t", "v", "w",
	                "x", "y", "z", "0", "1", "2",
                    "3", "4", "5", "6", "7", "8",
                    "9", "ç", "ã", "A", "B", "C"]
            #ORGANIZANDO SENHA
            shuffle(letters)
            geratePass = letters[0:13]
            for x in geratePass:
                print(x, end='')
            #SALVANDO SENHA
            passGerate = str(''.join(geratePass))
            savepass = input('\n\nsave password? [Y/n] .:').upper()

            #SALVA A SENHA
            if savepass == 'Y':
                namepassGerate = input('enter the generated password name .:')
                addValuePass(namepassGerate, passGerate)
            elif savepass == 'N':
                continue
            print('\n')
            close()
        #OPÇÃO PARA MOSTRAR INFORMAÇÕES SOBRE O PROGRAMA
        elif  menu == 'INFO':
            print( 
            '  dev_create: Pedro Henrique Quadros Pirralha\n'
            '  nameProduct: SimplePasswordManager\n'
            '  version: 0.0.3 / No Color in terminal\n'
            '  não comercializado, sem estrutura de qualidade e segurança')
            close()
        #CASO ERRE O COMANDO ESSA MENSSAGEM IRA APARECER
        else:
            print('digite uma opção valida')
            close()

#CASO ERRE A SENHA ESSA MENSSAGEM IRA APARECER 
else:
    print('\n--senha errada, reinicie o programa para tentar novamente--')
print('\nend')
