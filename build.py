
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx





def build_network(nodes, links):
    """ """
   
    # Define structure
    model = BayesianNetwork(links)

    # Build probability tables
    for n in nodes:

        # craft cpd
        if n['evidence'] and n['evidence_card']:
            cpd = TabularCPD(
                variable = n['name'],
                variable_card = n['variable_card'],
                values = n['values'],
                evidence=n['evidence'], 
                evidence_card=n['evidence_card']
            )
        else:
            cpd = TabularCPD(
                variable = n['name'],
                variable_card = n['variable_card'],
                values = n['values']
            )

        # add cpd to model
        model.add_cpds(cpd)

    # Vérifier la validité du modèle
    assert model.check_model()

    # Inférence avec Variable Elimination
    inference = VariableElimination(model)

    result = inference.query(variables=['Fever'], evidence={'F35': 1, 'F22':1})
    print(result)

        


            



if __name__ == "__main__":


    nodes = [
        {
            'name':'F22',
            'variable_card':2,
            'values':[[0.5], [0.5]],
            'evidence':None,
            'evidence_card':None    
        },
        {
            'name':'F35',
            'variable_card':2,
            'values':[[0.3], [0.7]],
            'evidence':None,
            'evidence_card':None    
        },
        {
            'name':'B1',
            'variable_card':2,
            'values':[[1, 1, 1, 0],[0, 0, 0, 1]],
            'evidence':['F22', 'F35'],
            'evidence_card':[2,2]    
        },
        {
            'name':'Fever',
            'variable_card':2,
            'values':[[0.8, 0.1], [0.2, 0.9]],
            'evidence':['B1'],
            'evidence_card':[2]
        }
        
    ]

    links = [
        ('B1', 'Fever'),
        ('F22', 'B1'),
        ('F35', 'B1')
    ]

    build_network(nodes, links)

