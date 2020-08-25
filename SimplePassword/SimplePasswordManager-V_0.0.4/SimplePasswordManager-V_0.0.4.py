import sqlite3 as sql
from random import shuffle
import spmDef
import os
#-------cores--------
red = spmDef.color['red'] 
green = spmDef.color['green']
bold = spmDef.color['bold']
yellowB = spmDef.color['yellow-b']
cyan = spmDef.color['cyan']
blue = spmDef.color['blue']
reverse = spmDef.color['reverse']
cl = spmDef.color['clear']

passMaster = '1'


login = input('Enter de Password.:')

#INICIALIZAÇÃO DO PROGRAMA
if spmDef.logPass(login) == True:
    while True:
        spmDef.AcessBanc()
        os.system('cls') #clear
        os.system('cls') #clear
        #INTERFACE DO PROGRAMA 
        menu = spmDef.interfaceMenu()
        more = ['MORE','+']

        #OPÇÃO PARA SAIR DO PROGRAMA
        if menu == 'EX':
            print("going out...\nthanks per use me :) ")
            break
        #OPÇÃO PARA REGISTRAR UMA SENHA
        elif menu == 'RP':
            passName = input('enter name pass .:')
            passPass = input('enter password .:')
            spmDef.addValuePass(passName, passPass)
            spmDef.close()
        #OPÇÃO PARA MOSTRAR SENHAS
        elif menu == 'SP':
            banc = sql.connect('spm.db')
            passBanc = banc.cursor()
            passBanc.execute("SELECT* FROM password")
            contpass = passBanc.fetchall()
            for x in range(0, len(contpass)):
                print('----->', x , ' ', contpass[x])
            banc.commit()
            banc.close()
            spmDef.close()
        #OPÇÃO PARA DELETAR SENHAS 
        elif menu == 'DP':
            loginDel = input('enter masterPass .:')
            if spmDef.logPass(loginDel) == True:
                nameDeletePass = input('enter the password name to delete .:')
                spmDef.delValuePass(True,nameDeletePass)
                spmDef.close()
            else:
                spmDef.delValuePass(False,None)  
                spmDef.close()

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
                spmDef.addValuePass(namepassGerate, passGerate)
                spmDef.close()

            elif savepass == 'N':
                continue
            print('\n')
        #OPÇÃO PARA MOSTRAR INFORMAÇÕES SOBRE O PROGRAMA
        elif  menu == 'INFO':
            print( 
            '  dev_create: Pedro Henrique Quadros Pirralha\n'
            '  nameProduct: SimplePasswordManager\n'
            '  version: 0.0.4 \n'
            '  não comercializado, sem estrutura de qualidade e segurança')
            spmDef.close()
                #INTERFACE MenuMore
        elif menu in more :
            os.system('cls')
             
            moreMenu = spmDef.interfaceMenuMore()#INTERFACE MenuMore VIA TERMINAL

            if moreMenu == 'DD':
                confirmation = input('sure you want to delete the database [Y/n] ..: ').upper()
                if confirmation == 'Y':
                    passMaster = input('enter PassMaster ..:')

                    if spmDef.logPass(passMaster) == True:
                        os.remove("spm.db")
                        print('database has been removed')
                        spmDef.close()
                    else:
                        print('password not deleted ')
                        spmDef.close()
            else:
                print('your database has not been deleted')
                spmDef.close()

        #CASO ERRE O COMANDO ESSA MENSSAGEM IRA APARECER
        else:
            print('digite uma opção valida')


 
#CASO ERRE A SENHA ESSA MENSSAGEM IRA APARECER 
else:
    print('\n--senha errada, reinicie o programa para tentar novamente--')
print('\nend')
