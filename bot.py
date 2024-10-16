from botcity.maestro import *
from faker import Faker

from FormContato import FormContato
from FormLogin import FormLogin

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def autenticar(form_login: FormLogin, qtd: range):
    fake = Faker()
    
    for _ in qtd:
        nome = fake.name()
        senha = fake.password()
        
        form_login.formulario_login()
        form_login.nome()
        form_login.senha()
        form_login.enviar()
        

def adicionar_contato(form_contato: FormContato, qtd: range):
    fake = Faker()
    
    for _ in qtd:
        nome = fake.name()
        email = fake.email()
        tel = fake.phone_number()
        
        form_contato.formularios_contato()
        form_contato.nome()
        form_contato.email()
        form_contato.telefone()
        form_contato.enviar()


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    
    try:
        contato = FormContato()
        login = FormLogin()
    
        autenticar(login, range(10))
        adicionar_contato(contato, range(10))
        
    except Exception as e:
            print(f"Error: {e}")
    
    finally:
        # if contato:
        #     contato.bot.stop_browser()
        # if login:
        #     login.bot.stop_browser()
        pass


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
