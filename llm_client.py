from langchain_community.llms import Ollama

def llm_ask(prompt, model="phi3"):
    """
    Perform analysis using langchain ollama llm model.
    Args:
        prompt (str): The prompt for analysis.
        model (str): The model to use for analysis. Defaults to "phi3".
    Returns:
        str: The analysis result.
    """
    # Get response from ph3 model
    ollama = Ollama(base_url='http://localhost:11434', model=model)
    print("Calling Prompt: {prompt} with model: {model}".format(prompt=prompt, model=model))
    print("Please be patient, LLM call may take a while...")
    analysis_result = ollama.invoke(prompt)
    return analysis_result