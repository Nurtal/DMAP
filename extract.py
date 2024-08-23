import spacy
import pandas as pd
import matplotlib.pyplot as plt


def extract_simple_relation(sentence):
    """ """

    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the sentence
    doc = nlp(sentence)
    
    # Initialize variables to store results
    relations_dict = {}
    
    # Iterate over tokens to find subjects, objects, and verbs
    for token in doc:
        if token.dep_ == "nsubj":  # Subject
            subject = token.text
            if subject not in relations_dict:
                relations_dict[subject] = []
            for child in token.head.children:
                if child.dep_ == "dobj":  # Direct object
                    relation = token.head.text  # Verb (relation)
                    relations_dict[subject].append({"elt": child.text, "relation": relation})
                # Handling conjunctions (like "and" in "dog and duck")
                if child.dep_ == "conj":
                    relations_dict[subject].append({"elt": child.text, "relation": relation})
    
    return relations_dict

 

def extract_entities_and_relationships(sentence, nlp):
    # Run the NER pipeline
    results = nlp(sentence)

    # Initialize a dictionary to store entities and relationships
    relations_dict = {}
    
    # Initialize variables to store entities and relationships
    entities = {}
    current_entity = None

    # Process the results
    for entity in results:
        entity_text = sentence[entity['start']:entity['end']]
        entity_label = entity['entity']
        
        # Store the entities with their labels
        if entity_label not in entities:
            entities[entity_label] = []
        entities[entity_label].append(entity_text)
        
        # If we find a gene or drug, add it to the dictionary
        if entity_label == "B-GENE" or entity_label == "B-CHEMICAL":
            current_entity = entity_text

        # Assuming the relation is described by the surrounding text, we might need to make more complex rules here
        if current_entity:
            if entity_label == "B-DISEASE":
                if current_entity not in relations_dict:
                    relations_dict[current_entity] = []
                relations_dict[current_entity].append({"elt": entity_text, "relation": "associated_with"})
                current_entity = None  # Reset current_entity for the next set of relations

    return relations_dict






if __name__ == "__main__":


    # sentence_list = list(pd.read_csv('data/toy.csv')['SENTENCE'])
    # for sentence in sentence_list:
    #     result = extract_simple_relation(sentence)
    #     print(sentence)
    #     print(result)
    #     print("-"*45)



    from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

    # Load the tokenizer and model for PubMedBERT
    model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    # Initialize the NER pipeline
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    # Example sentence
    sentence = "BRCA1 is a gene involved in the repair of DNA double-strand breaks, commonly mutated in breast cancer."

    # Extract entities and relationships
    relations_dict = extract_entities_and_relationships(sentence, nlp)

    # Display the results
    print(relations_dict)




    



