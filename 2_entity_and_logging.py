#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares
"""
import spacy
import logging

# Configurando o logging
logging.basicConfig(level=logging.INFO)

class EntityRecognizer:
    """
    Classe para reconhecimento de entidades usando a biblioteca Spacy.
    """
    def __init__(self):
        """
        Inicializa a classe com o texto a ser analisado.
        """
        self.nlp = spacy.load('pt_core_news_sm')

    def recognize(self, text):
        """
        Reconhece as entidades no texto.
        """
        doc = self.nlp(text)

        entities ={}
        # Verifica se existem entidades no texto
        if doc.ents:
            logging.info('Entidades encontradas:')
            for ent in doc.ents:
                entities[ent.text] = ent.label_
               
        else:
            logging.info('Nenhuma entidade encontrada.')
            print("O texto não contém Entidades 🤗!")

        return entities


if __name__== "__main__":
    # Exemplo de uso:
    recognizer = EntityRecognizer()
    text = 'A Karina é cientista de dados!'
    entidades =  recognizer.recognize(text)
    print(entidades)