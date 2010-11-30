#!/usr/bin/env python
import sys
import os
import parser
import subprocess

if "VIRTUAL_ENV" not in os.environ:
    sys.stderr.write("$VIRTUAL_ENV not found.\n\n")
    parser.print_usage()
    sys.exit(-1)
virtualenv = os.environ["VIRTUAL_ENV"]
file_path = os.path.dirname(__file__)
subprocess.call(["pip", "install", "-E", virtualenv, "--requirement",
                 os.path.join(file_path, "REQUIREMENTS")])
if not os.path.isdir("media"):
    os.mkdir("media")
if not os.path.islink("settings.py") and os.path.isfile("settings_development.py"):
    os.symlink("settings_development.py", "settings.py")
    # todo: add ignore settings.py check and adding to .gitignore file