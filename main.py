import cmd
import os
import platform
import subprocess
from typing import IO
from response  import Command
import mysql.connector
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
class MyCLI(cmd.Cmd):
    # prompt = '>> '
    # intro = 'Welcome to MyCLI. Type "help" for available commands.'
    def __init__(self):
        super().__init__()
        self.prompt = Fore.LIGHTMAGENTA_EX+'>> '
        self.intro = Fore.CYAN+'Welcome to MyCLI. Type "help" for available commands.'
        self.db_connection = None
        self.cursor = None

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")
    
    def do_os_command(self, line):
        """Run an OS command."""
        try:
            print(line)
            command_gen = Command()
            command = command_gen.request_command(line)
            print(command)
            process = subprocess.run(command, shell=True, capture_output=True, text=True)

            if process.returncode == 0:
                print(Fore.GREEN+f"Command executed successfully.\nOutput:\n{process.stdout}")
            else:
                print(Fore.YELLOW+f"Command failed due to invalid input or having error:"+Fore.RED+ f"{process.stderr}")
        except Exception as e:
            print(Fore.YELLOW+f"Error executing command: "+ Fore.RED+"f{e}")

    def do_run_query(self, line):
        """Run an MySQL query."""
        try:
            print(line)
            command_gen = Command()
            command = command_gen.request_command(line)
            print("cmd "+command)
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            print(Fore.GREEN+result)
        except mysql.connector.Error as err:
            print(f"Error executing SQL query: {err}")
            
        # except Exception as e:
        #     print(f"Error executing command: {e}")

        
    def do_config_db(self,line):
        """connect with mysql database"""
        line = line.split()
        username = line[0]
        password = line[1]
        host = line[2] if len(line) > 2 else "localhost"
        try:

            self.db_connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password
            )
            self.cursor = self.db_connection.cursor()
        except Exception as e:
            print(Fore.YELLOW+f"Connection failed with error: "+Fore.RED+f"{e}")
    
    
    def do_quit(self, line):
        """Exit the CLI."""
        print(Fore.CYAN+"\nExiting the CLI.")
        return True

if __name__ == '__main__':
    try:

        MyCLI().cmdloop()
    except KeyboardInterrupt:
        print(Fore.CYAN+"\nExiting the CLI.")