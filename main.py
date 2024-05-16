from command_analyzer import analyze_command
import sys
from generate_code import generate_code

def command_analyze():
    analysis_result = analyze_command()
    print(analysis_result)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "analyze":
        command_analyze()
    elif len(sys.argv) > 1 and sys.argv[1] == "generate":
        generate_code()
    else:
        print("Usage: python main.py [analyze|generate]")
        print("analyze: Execute and Analyze a shell command output based on user input.")
        print("generate: Generate sample code based on user input.")