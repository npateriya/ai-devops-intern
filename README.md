# AI DevOps Intern

AI DevOps Intern is tool designed to assist with DevOps tasks by leveraging the power of AI. It serves as a virtual intern, capable of analyzing shell commands and generating code scripts based on user input. By harnessing the capabilities of locally running Ollama-based Language Models like phi3 or Mistral, this project aims to streamline and enhance the DevOps process, making it more efficient and user-friendly.

AI DevOps Intern repo currently supports a command analyzer and a code script generator.

The command analyzer executes and analyzes shell command outputs based on user input, while the code generator produces sample code/script for a given programming/devops task. 



*This project serves as an introduction to the capabilities of AI and LLMs. It is a beginner-friendly project designed to demonstrate the potential of these technologies in software development. However, it is not intended for production use.*

## Setup

Follow these steps to set up and run the project:

1. Clone the repository:

```bash
git clone <repo-url>
```
2. Navigate to the project directory and install the required Python packages: 
```
cd <project-directory>
pip install -r requirements.txt
```

3. Install and run the phi3 model locally using [Ollama](https://ollama.com/):
```
ollama run phi3
```
# Usage

Utility supports two modes of operation: `analyze` and `generate`.

```
python main.py 
Usage: python main.py [analyze|generate]
analyze: Execute and Analyze a shell command output based on user input.
generate: Generate sample code based on user input.
```


### Analyze Mode

In analyze mode, the script will prompt the user to input a Unix command. It will then execute the command, analyze the output, and provide a summary.

To run the script in analyze mode, use the following command:

``` bash
>> python main.py analyze 
Analayze command executes the input command and returns the analysis result for as question asked.
The sample commands are:

1. df -h, What is the disk space usage on the system?
2. top -l 1 -n 5 -o mem, Which processes are using the most resources?
3. ls -l, What are the files in the current directory?

Enter the number corresponding to the command you want to execute (or press Enter to enter a new command): 2
```
#### Sample Command Analysis response
```
- The process using the most resources is `Microsoft Excel` with a memory usage of 1128M. This system utilization indicates that it's currently running and consuming significant amounts of RAM, which might be expected during data processing tasks often performed by spreadsheets like Microsoft Excel.

- Other notable processes are:
    - `WindowServer`: Memory usage is substantial (3064M), but it seems to have a lower priority as its CPU utilization is relatively low at 0.0%. This process manages the windowing system for macOS, responsible for windows, dialog boxes, and other graphical user interface elements.
    - `Webex`: It has the lowest memory usage (3819M) amongst all processes, but still holds a considerable amount of memory. As an application, it likely serves as a communication platform or video conferencing service in this context.
    Market-leading products like Microsoft Office Excel are known to be resource-intensive due to their complex functionalities and capabilities for data analysis and visualization.
```



## Generate Sample Code/Script Mode
In generate mode, the script will prompt the user to input a programming task. It will then generate sample code/script for the task.

To run the script in generate mode, use the following command:

generate
Example:
```
command-ai-assist % python3 main.py generate
Choose from the following sample code inputs:
1. create ansible playbook to ping all hosts in the inventory file
2. create a python script to list all files in a directory
3. create a dockerfile to build a flask application
4. create a terraform script to provision an AWS EC2 instance
5. create an ansible playbook to install and configure Nginx
6. create a bash script to backup a MySQL database
7. create a docker-compose file to deploy a multi-container application
8. create a terraform script to create an S3 bucket
9. create an ansible playbook to deploy a web application
10. create python script using Meraki SDK to list all network in organization
Or press enter to provide a custom input.
Enter your choice: 1
```
#### Generated Sample Code 
```yaml
# Note: The generated code may require some modifications to work correctly or it may even hallucinate some code. Please review the generated code before using it.
# Ansible Playbook: Ping All Hosts from Inventory File
# This playbook assumes that you have an `inventory/hosts.yml`
---
- hosts: all
  vars_files:
    - inventory/hosts.yml # Assuming the inventory file is named 'hosts.yml'
  tasks:
    - name: Ping all hosts in the inventory
      ping:
        host: "{{ item }}" # Iterate over each host from the inventory and perform a ping
      loop_control:
        loop: "{{ inventory_hostname | list }}" # Use 'loop' to iterate through the list of hostnames provided by Ansible's inventory module

>> `hosts.yaml` 

# hosts.yml sample content
[webservers]
server1.example.com
server2.example.com

[dbservers]
database-server.example.com
```

## Future Possible Enancements

1. **Multi-Agent System:** Develop the project into a multi-agent system where each agent specializes in a specific task (e.g., one agent for system diagnostics, another for network configuration, etc.). This will allow for more efficient and parallel processing of tasks.

2. **Extensibility:** Design the system to be easily extendible, allowing new features or agents to be added with minimal effort. This could include creating a plugin system or designing the software architecture to be modular.

3. **Automated System Diagnostics:** Enhance the command analyzer to not only execute and analyze shell commands, but also diagnose system issues and suggest solutions.

4. **Network Configuration:** Add a feature to generate network configuration scripts based on user input.

5. **Infrastructure as Code (IaC) Generation:** Implement a feature to generate IaC scripts (like Terraform or CloudFormation) based on user input.

6. **CI/CD Pipeline Generation:** Develop a feature to generate scripts for setting up Continuous Integration/Continuous Deployment pipelines.

7. **Server Management:** Add a feature to generate scripts for common server management tasks.

8. **Code Review and Optimization:** Implement a feature to review and suggest optimizations for the generated code.

9. **Automated Testing:** Add a feature to generate unit tests for the generated code.

10. **Documentation Generation:** Implement a feature to generate documentation for the generated code.

Please note that these are potential future plans and are subject to change based on project development and user feedback.