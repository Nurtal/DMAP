
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def trash():
    """Playing with the concept of Bayesian network""" 

    # Définir la structure du réseau
    model = BayesianNetwork([('F', 'C'), ('C', 'T')])

    # Définir les CPTs
    cpd_f = TabularCPD(variable='F', variable_card=2, values=[[0.3], [0.7]])
    cpd_c = TabularCPD(variable='C', variable_card=2, 
                       values=[[0.1, 0.5], [0.9, 0.5]],
                       evidence=['F'], evidence_card=[2])
    cpd_t = TabularCPD(variable='T', variable_card=2, 
                       values=[[0.4, 0.2], [0.6, 0.8]],
                       evidence=['C'], evidence_card=[2])

    # Ajouter les CPTs au modèle
    model.add_cpds(cpd_f, cpd_c, cpd_t)

    # Vérifier la validité du modèle
    assert model.check_model()

    # Inférence avec Variable Elimination
    inference = VariableElimination(model)

    # Par exemple, calculer P(T = Oui | F = Oui)
    result = inference.query(variables=['T'], evidence={'F': 1})



def shtrmp_model():
    """

    ---------
    | Fever |
    ---------
    |
    |     ----
    |_____|B1|
          ----
            |
            |    -----
            |____|F22|
            |    -----
            |    -----
            |____|F35|       
                 -----
    """

    # Define structure
    model = BayesianNetwork([
        ('B1', 'Fever'),
        ('F22', 'B1'),
        ('F35', 'B1')
    ])

    # Probability tables
    cpd_f22 = TabularCPD(variable='F22', variable_card=2, values=[[0.5], [0.5]])
    cpd_f35 = TabularCPD(variable='F35', variable_card=2, values=[[0.3], [0.7]])
    cpd_b = TabularCPD(variable='B1', variable_card=2, 
                        values=[[1, 1, 1, 0],  
                                [0, 0, 0, 1]], 
                        evidence=['F22', 'F35'], 
                        evidence_card=[2, 2])
    cpd_fever = TabularCPD(
                variable='Fever',
                variable_card=2,
                values=[[0.8, 0.1], [0.2, 0.9]],
                evidence=['B1'], evidence_card=[2]
            )

    # Ajouter les CPTs au modèle
    model.add_cpds(cpd_f22, cpd_f35, cpd_b, cpd_fever)

    # Vérifier la validité du modèle
    assert model.check_model()

    # Inférence avec Variable Elimination
    inference = VariableElimination(model)

    result = inference.query(variables=['Fever'], evidence={'F35': 1, 'F22':0})

    print(result)
    

    


if __name__ == "__main__":

    # trash()
    shtrmp_model()


    
