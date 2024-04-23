# **GenShell_Application**

GenShell is a Python project that utilizes generative AI to generate Linux commands and SQL queries based on the input provided.
## Overview

This project aims to assist users in generating Linux commands and SQL queries for various purposes. It utilizes machine learning techniques to generate coherent and relevant commands and queries based on the provided input.

## Features

- Input-driven Command and Query Generation: Users can input a prompt or context, and the AI generates a Linux command or SQL query relevant to that input.
- Customization: Users can adjust the parameters of the AI model to fine-tune the generated commands and queries.
- Multiple Applications: The generated commands and queries can be used for scripting, database management, system administration, and more.
- Easy-to-Use Interface: Simple command-line interface for generating commands and queries quickly.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/your-username/linux-sql-generator.git
    ```

2. Navigate to the project directory:

    ```
    cd linux-sql-generator
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the command generator script:

    ```
    python command_generator.py
    ```

2. Follow the prompts to input your context or prompt.

3. The AI will generate a Linux command or SQL query based on your input.

## Configuration

You can adjust the following parameters in `config.py`:

- `MODEL_TYPE`: Specify the type of generative AI model to use.
- `MODEL_PARAMS`: Set parameters for the selected model.
- `INPUT_LENGTH`: Define the maximum length of the input prompt.
- `OUTPUT_LENGTH`: Define the maximum length of the generated command or query.
- `NUM_GENERATIONS`: Number of command/query generations to produce.
- `TEMPERATURE`: Temperature parameter for controlling randomness in generation.

## Examples

- Linux Command:
  
  ```
  Input: "List all files in the current directory"
  Output: "ls -l"
  ```

- SQL Query:

  ```
  Input: "Retrieve all employees from the 'HR' department"
  Output: "SELECT * FROM employees WHERE department = 'HR';"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.