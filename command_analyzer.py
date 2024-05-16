import subprocess
from langchain_core.prompts import PromptTemplate
from llm_client import llm_ask

def execute_command(command):
    """
    Executes a shell command and returns the output.
    Args:
        command (str): The shell command to execute.
    Returns:
        str: The output of the command.
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def analyze_command():
    """
    Analyzes a Unix command based on user input and returns the analysis result.

    Returns:
        The analysis result of the command.
    """
    # Get the command and user query from the user

    sample_commands = {
        "df -h": "What is the disk space usage on the system?",
        "top -l 1 -n 5 -o mem": "Which processes are using the most resources?",
        "ls -l": "What are the files in the current directory?",
        "curl -I https://www.google.com/": "Display its output in table format"
    }
    print ("Analyze command executes the input command and returns the analysis result for as question asked.")
    print ("The sample commands are:\n")
    for i, (command, query) in enumerate(sample_commands.items()):
        print(f"{i+1}. {command}, {query}")

    choice = input("\nEnter the number corresponding to the command you want to execute (or press Enter to enter a new command): ")

    if choice:
        index = int(choice) - 1
        if index >= 0 and index < len(sample_commands):
            command = list(sample_commands.keys())[index]
            user_query = list(sample_commands.values())[index]
        else:
            print("Invalid choice. Exiting...")
            return
    else:
        command = input("Enter the Unix command: ")
        user_query = input("What do you want to know about the command output: ")

    command_output = execute_command(command)
    #print(command_output)
    
    # Generate a prompt that will ask the analysis model to analyze the command
    prompt_template = PromptTemplate.from_template(
        """\nUser has executed this Unix command: `{command}`.
        User wants to know: '{user_query}'.
        Provide output in bulleted summary if user does not explcitly specify output format.
        The output of the command is: \n\n {command_output}
        """
    )
    final_prompt = prompt_template.format(command=command, user_query=user_query, command_output=command_output)

    # Get the analysis result from the LLM model
    command_analysis = llm_ask(final_prompt,model="phi3")
    return command_analysis