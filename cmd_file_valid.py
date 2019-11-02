import os.path
import sys

# Checking Command file validity
def cmd_file_valid():
	# Prompting user for input
	cmd_file = input("\n# Enter command file path and name (e.g. D:\MyApps\myfile.txt): ")

	# Checking if the file exists
	if os.path.isfile(cmd_file) == True:
		print("\n Command file is valid : \n ")

	else:
		print("n\ File {} does not exist : ( Please check and try again. \n".format(cmd_file))
		sys.exit()