def line(tam=60):
    print('--'*tam)
def leiaInt(numero):
    ok= False 
    valor=0 
    while True:
        try:
            n= int(input(numero))
        except(ValueError,TypeError):
            print('ERRO!O tipo de dado está errado.')
        except KeyboardInterrupt:
            print('ERRO!O usuário não informou os dados.')
            return 0
        else:
            valor=n
            ok=True
        if ok:
            break 
    return valor


def hea(txt, tam=42):
    line(tam)
    print(txt.center(42))
    line(tam)

def menu(lista):
    hea('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    line()
    opc= leiaInt('Sua opção: ')
    return opc

def arquivoExiste(nome):
    try:
        a= open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a= open(nome, 'wt+')
        a.close()
    except:
        print('File not created error!')
    else:
        print(f'File {nome} created successfully!')

def lerArquivo(nome):
    try:
        a= open(nome, 'rt')
    except:
        print('Read file error!')
    else:
        hea('CHARACTER INFORMATION')
        for linha in a:
            dado= linha.split(';')
            dado[1]= dado[1].replace('\n','')
            print(f'Name:{dado[0]:<30} Class:{dado[1]:>3}')
    finally:
        a.close()

def cadastrar(nome, n='Unknown', c= 'Human'):
    try:
        a= open(nome, 'at')
    except:
        print('File opening error!')
    else:
        try:
            a.write(f'{n};{c}\n')
        except:
            print('error writing data!')
        else:
            print(f'New {n} added!')
            a.close()

def conq(nome, conquest):
    try:
        a= open(nome, 'at')
    except:
        print('File opening error!')
    else:
        try:
            a.write(f'Conquest: {conquest}')
        except:
            print('error writing data!')
        else:
            print('New conquest added!')
            a.close()