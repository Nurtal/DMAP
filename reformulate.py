
from langchain_community.llms import Ollama

def reformulate(text):
    """


    output attendu pour le test :
    
    sentence_list = [
        'B1 depend on F35',
        'B1 depend on F22',
        'Fever is induced by B1'
    ]
    
    """


    llm = Ollama(model="llama3:70b")
    
    # stage 1
    prompt = f"""

    [INSTRUCTION] : Parse the following text into atomic statements that capture all the relationships described. The output should be a list of very simple sentences, where each sentence describes only one relationship. return results as a list   
    [TEXTE] : {text}

    [OUTPUT]: 
    """
    answer = llm.invoke(prompt)

    print(answer)
    print("-"*42)

    return answer



if __name__ == "__main__":

    text = """Fever is a main symptoms of the disease, it rely on the activation of B1 factor. F22 and F35 are responsible for the activation of B1."""

    log_file = open("llm_llama3_70b.log", 'w')
    for x in range(10):
        llm_output = reformulate(text)
        log_file.write(f"{llm_output}\n")
        log_file.write(f"---------------------------------\n")
    log_file.close()

    
