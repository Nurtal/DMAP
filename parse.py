"""
Notes:

    treat dependencies as 2 type:

    X depends on Y (i.e is impacted)
    X impact Y
    
"""

import re



def clean_sentence(sentence:str) -> str:
    """Clean a sentence by removing 'trash' words

    Args:
        - sentence (string) : the sentence to clean

    Returns:
        - (string) : the cleaned sentence

    DevNotes:
        - might want to load trash words from a file instead of setting up a list within the function
    """
    # parameters
    trash_words = [
        ' is ',
        ' are ',
        ' on ',
        ' by '
    ]

    clean_sentence = sentence
    for t in trash_words:
        clean_sentence = clean_sentence.replace(t, ' ')

    return clean_sentence


def extract_node_name(sentence_list:list) -> list:
    """Extract list of nodes from sentence_list

    Args:
        - sentence_list (list) : list of sentences (str) to parse
    
    Returns:
        - (list) : list of extracted node names (str)
    
    """

    # parameters
    connection_words = [
        ' depend ',
        ' involve ',
        ' induced '
    ]

    node_list = []
    for s in sentence_list:

        # clean sentence
        s_clean = clean_sentence(s)

        for t in connection_words:
            s_clean = s_clean.replace(t, ' ')

        # extract nodes
        a = s_clean.split(' ')
        for n in a:
            if n not in node_list:
                node_list.append(n)

    # return list of extracted nodes
    return node_list
        #


def extract_dependencies(node_list:str, sentence_list:str)->dict:
    """Extract dependencies between nodes

    Args:
        - node_list (list) : list of node names (str)
        - sentence_list (list) : list of sentences (str) 

    Returns:
        - (dict) : node (str) to dependant nodes (list)

    DevNotes:
        - for now detection foculs on 'left' component
    """
    
    # parameters
    connection_words_left = [
        ' depend ',
        ' impacted ',
        ' induced ',
    ]
    connection_words_right = [
        ' impact ',
        ' induce ',
    ]

    node_to_dependencies = {}
    for n in node_list:
        for s in sentence_list:
            s_clean = clean_sentence(s)
            a = s_clean.split(' ')
            if n in a:
               
                # Look on the left part of the sentence for dependecies
                for t in connection_words_left:
                    s_parsed = s_clean.split(t)
                    if len(s_parsed) == 2:

                        if s_parsed[0] == n:
                            if n not in node_to_dependencies:
                                node_to_dependencies[n] = []
                                if s_parsed[1] in node_list:
                                    node_to_dependencies[n].append(s_parsed[1])
                            else:
                                if s_parsed[1] in node_list:
                                    node_to_dependencies[n].append(s_parsed[1])

    # return node to dependencies
    return node_to_dependencies
            
            
def build_links(node_to_dependencies):
    """ """

    links = []
    for n in node_to_dependencies:
        source_list = node_to_dependencies[n]
        for source in source_list:
            l = (source, n)
            if l not in links:
                links.append(l)
    return links



def build_nodes(node_to_dependencies, node_to_values):
    """
       
    
    """

    nodes = []
    for n in node_to_values:

        # compure evidence
        if n in node_to_dependencies:
            evidence = node_to_dependencies[n]
            evidence_card = []
            for x in node_to_dependencies[n]:
                evidence_card.append(len(node_to_values[x]))
        else:
            evidence = None
            evidence_card = None

        # craft node
        node = {
            'name':n,
            'variable_card':len(node_to_values[n]),
            'values':node_to_values[n],
            'evidence':evidence,
            'evidence_card':evidence_card
        }

        # update node list
        nodes.append(node)

    # return a node list
    return nodes


if __name__ == "__main__":


    # TEST SETUP
    # params
    sentence_list = [
        'B1 depend on F35',
        'B1 depend on F22',
        'Fever is induced by B1'
    ]
    node_to_values = {
        'F22':[[0.5], [0.5]],
        'F35':[[0.3], [0.7]],
        'B1':[[1, 1, 1, 0],[0, 0, 0, 1]],
        'Fever':[[0.8, 0.1], [0.2, 0.9]],
    }
    
    # run functions
    node_list = extract_node_name(sentence_list)
    node_to_dependencies = extract_dependencies(node_list, sentence_list)
    links = build_links(node_to_dependencies)
    nodes = build_nodes(node_to_dependencies, node_to_values)


    
