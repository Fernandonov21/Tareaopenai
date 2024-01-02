from dotenv import load_dotenv
from ec.llm.servicio.logica import logicaServicios
if __name__ == '__main__':
    load_dotenv('secrets/.env')
    print(logicaServicios().invoke('2013'))


