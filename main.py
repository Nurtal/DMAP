import pandas as pd
import build
import parse




if __name__ == "__main__":

    # 1 TODO. reformulate text

    # 2 TODO extract sentences
    sentence_list = [
        'B1 depend on F35',
        'B1 depend on F22',
        'Fever is induced by B1'
    ]

    # 3 TODO assign values
    node_to_values = {
        'F22':[[0.5], [0.5]],
        'F35':[[0.3], [0.7]],
        'B1':[[1, 1, 1, 0],[0, 0, 0, 1]],
        'Fever':[[0.8, 0.1], [0.2, 0.9]],
    }

    #------------------#
    # 4 PARSE SENTENCE #
    #------------------#
    
    ## 4.1 extract nodes name
    node_list = parse.extract_node_name(sentence_list)
    
    ## 4.2 extract node dependencies
    node_to_dependencies = parse.extract_dependencies(node_list, sentence_list)

    ## 4.3 Build nodes and links
    links = parse.build_links(node_to_dependencies)
    nodes = parse.build_nodes(node_to_dependencies, node_to_values)

    #-----------------#
    # 5 BUILD NETWORK #
    #-----------------#

    ## 5.1 build network
    build.build_network(nodes, links)
