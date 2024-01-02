import os
from openai import OpenAI
from ec.llm.constantes.const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT


class logicaServicios:

    def __init__(self):
        self.__modelo = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__cliente = OpenAI()
        self.__prompt ='convert {number} to binary'


    def __parametros(self, prompt):
        return CLEAN_TEXT(self.__cliente.completions.create(
            model=self.__modelo,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invoke(self, number: int) ->str:
        peticion = self.__prompt.format(number=number)
        return self.__parametros(peticion)
