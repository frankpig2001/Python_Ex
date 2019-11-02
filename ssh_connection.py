import paramiko
import os.path
import time
import sys
import re

# Checking username /password file
# Prompting the user for input - USERNAME/PASSWORD FILE
user_file = input("\n Username/password file is valid. \n")

# Verifying the validity of the USERNAME/PASSWORD FILE
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid.\n")
else:
    print("\n* File {} does not exist. Please check and try again.\n".format(user_file))
    sys.exit()


# Checking Command file validity
# Prompting user for input
cmd_file = input("\n# Enter command file path and name (e.g. D:\MyApps\myfile.txt): ")

# Checking if the file exists
if os.path.isfile(cmd_file) == True:
    print("\n Command file is valid : \n ")
else:
    print("\n File {} does not exist : ( Please check and try again. \n".format(cmd_file))
    sys.exit()

# Open SSHv2 connection to the device


def ssh_connection(ip):
    global user_file
    global cmd_file

    # Creating SSH CONNECTION
    try:
        # Define SSH parameters
        selected_user_file = open(user_file, 'r')

        # Starting from the beginning of the file
        selected_user_file.seek(0)

        # Read the username from the file
        username = selected_user_file.readlines()[0].split.('.')[0].rstrip("\n")

 		# Starting from the beginning of the file
        selected_user_file.seek(0)

        # Read password from file
        password = selected_user_file.readlines()[0].split('.')[1].rstrip('\n')

        # Log into device
        session = paramiko.SSHClient()

        # For testing purposes, this allows auto-accepting unknown host keys
        # Do not use in production! The default would be RejectPolicy
        sesson.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device using username and password
        session.connect(ip.rstrip('\n'), username = username, password = password)

        # Start an interactive shell session on the router 
        connection = session.invoke_shell()

        # Setting terminal length for entire output -disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Entering gloabal configuration mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        # Starting from the beginning of the file
        selected_cmd_file.


        # Setting terminal length for entire output - disable pagination
        conneciton







