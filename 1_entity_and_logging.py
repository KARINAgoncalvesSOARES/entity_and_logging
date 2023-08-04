#!/usr/bin/env python3

"""
Data Scientist Jr.: Karina Gonçalves Soares
"""
import spacy
import logging

# Configuração do logging:
#logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # 🤗
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def extract_entities(text):
    logging.info("Iniciando a extração de entidades")
    
    # Carregar o modelo pré treinado do SpaCy para o idioma português:
    nlp = spacy.load("pt_core_news_sm") # python -m spacy download pt_core_news_sm #INSTALAR
    
    # Processar o texto com o modelo pré-treinado;
    doc = nlp(text)
    
    # Extrair e logar as entidades encontradas
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
        logging.debug(f"Entidade encontrada: {ent.text} - Tipo: {ent.label_}")
    
    logging.info("Extração de entidades concluída")
    return entities



if __name__ == "__main__":
    text = "A Apple Inc. foi fundada por Steve Jobs e Steve Wozniak em 1976."
    extracted_entities = extract_entities(text)
    print("Entidades extraídas:", extracted_entities)