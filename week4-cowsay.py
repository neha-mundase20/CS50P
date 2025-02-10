# pip - package manager, used for easy installation of packages.

# pip install cowsay

# 'cowsay' is a package allows you to have a cow that says something

import cowsay
import sys

if len(sys.argv)==2:
    cowsay.cow("Hello, "+sys.argv[1])
    cowsay.trex("Hello, "+sys.argv[1])