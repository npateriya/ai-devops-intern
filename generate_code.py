from llm_client import llm_ask
from langchain_core.prompts import PromptTemplate


# Create function that will take user input and generate code based on the input.
# First paramter takes user input on what sample code generation.
# Also second optional filename to save the generated code.
# The function will genrate code by calling calling llm_ask function from llm_client.py

def get_user_input():
    sample_code_inputs = [
       "create ansible playbook to ping all hosts in the inventory file",
       "create a python script to list all files in a directory",
       "create a dockerfile to build a flask application",
       "create a terraform script to provision an AWS EC2 instance",
       "create an ansible playbook to install and configure Nginx",
       "create a bash script to backup a MySQL database",
       "create a docker-compose file to deploy a multi-container application",
       "create a terraform script to create an S3 bucket",
       "create an ansible playbook to deploy a web application",
       "create python script using Meraki SDK to list all network in organization", # Small models may generate incorrect code 
    ]

    # Prompt the user to choose from the sample code inputs or enter a custom input
    print("Choose from the following sample code inputs:")
    for i, code_input in enumerate(sample_code_inputs):
        print(f"{i+1}. {code_input}")
    print("Or press enter to provide a custom input.")

    # Get user input
    user_choice = input("Enter your choice: ")

    # Process user input
    if user_choice.isdigit() and int(user_choice) in range(1, len(sample_code_inputs) + 1):
        selected_input = sample_code_inputs[int(user_choice) - 1]
    else:
        selected_input = input("Enter your custom input: ")
    
    return selected_input

def generate_code(filename=None):
    input = get_user_input()
    # Generate a prompt that will ask the analysis model to analyze the command
    prompt_template = PromptTemplate.from_template(
        """\n Generate sample code for user request: `{input}`. 
        Ensure output compiles and executable code only, if any description they should be in respective programming language comments only.
        Do not assume any API or SDK function call, ensure code uses only accrurate and valid API and SDK function calls.
        """
    )
    final_prompt = prompt_template.format(input=input)
    # Generate code using llm_ask function from llm_client.py
    code = llm_ask(final_prompt)
    
    # Save the generated code to a file if filename is provided
    if filename:
        with open(filename, 'w') as file:
            file.write(code)
    else:
        print("\n### Generated Code ###\n")
        print("Note: The generated code may require some modifications to work correctly or it may even hallucinate some code. Please review the generated code before using it.")
        print(code)
    
    return code

