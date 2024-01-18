import cmd
import os
import platform
import subprocess
from response  import Command
# from gen import GenerativeAI
class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")
    
    def do_run_command(self, line:str):
        """Run an OS command."""
        try:
            print(line)
            command_gen = Command()
            command = command_gen.request_command(line)
            print(command)
            process = subprocess.run(command, shell=True, capture_output=True, text=True)

            if process.returncode == 0:
                print(f"Command executed successfully.\nOutput:\n{process.stdout}")
            else:
                print(f"Command failed with error: {process.stderr}")
        except Exception as e:
            print(f"Error executing command: {e}")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()