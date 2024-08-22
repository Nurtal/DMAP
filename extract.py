import spacy




def run():
    """ """

    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # The sentence to process
    sentence = "fever is a biological process induced by pathway B"

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Extract relations based on dependency parsing
    relations = []
    for token in doc:
        if token.dep_ == "prep" and token.head.pos_ == "NOUN":
            # Relation: (subject, relationship, object)
            subject = [t.text for t in token.head.lefts if t.dep_ == "nsubj"]
            obj = [t.text for t in token.subtree if t.dep_ == "pobj"]
            if subject and obj:
                relations.append((subject[0], token.text, " ".join(obj)))

    # Display results
    print("Entities:")
    for ent in entities:
        print(ent)

    print("\nRelations:")
    for rel in relations:
        print(rel)




if __name__ == "__main__":

    run()

    nlp = spacy.load("en_core_web_sm")

    # The sentence to process
    sentence = "fever is a biological process induced by pathway B"

    # Process the sentence with spaCy
    doc = nlp(sentence)

    # Display token information for debugging
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, DEP: {token.dep_}, ENT_TYPE: {token.ent_type_}")
