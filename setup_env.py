
import os
import sys
from sys import platform

def is_venv():
    return (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

def activate_venv():
    if is_venv(): return False
    print("Detecting Your Platform is '{}'".format(platform))
    if platform == "win32":
        executable = os.path.join(".","","venv","Scripts","activate")
        print("To activate the virtual environment on Windows run {} ".format(executable))
        print("To deactivate the virtual environment on Windows run {} ".format("deactivate"))
    else:
        executable = "{} {}".format("source" , os.path.join("venv","bin","activate"))
        print("To activate the virtual environment on Non Windows run {} ".format(executable))
        print("To deactivate the virtual environment on Non Windows run {} ".format("deactivate"))
    return True

print("Checking if virtual environment exists")

if os.path.isdir(os.path.join("venv","bin","")) or os.path.isdir(os.path.join("venv","Scripts","")):
    print("looks like we already have a virtual environment in this project")
    if is_venv():
        print("Looks likt your Virtual Environment is activated.")
        print("To deactivate run command deactivate")
    else:
        activate_venv()
else:
    answer = input("would you like to setup virtual environment (y/n)? ")
    if answer == "y":
        print("setting up the virtual environment")
        os.system("python -m venv venv")
        print("Installation of virtual environment completed")
        activate_venv()
        print()
        print("After you activate the virtual environment for the first time, run the following commands")
        print("python -m pip install --upgrade pip")
        print()
        print("if you are in a project for the first time, run pip install for the project requirements file usually \"requirements.txt\"")
        print("pip install -r requirements.txt")
    else:
        print("you choose not to, Exiting...")
        sys.exit()


