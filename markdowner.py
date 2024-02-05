#!/usr/bin/python3

import os
import sys

if len(sys.argv) < 2:
    print("Usage: markdowner.py <filename>")
    sys.exit(1)

content = os.popen(f"markdown {sys.argv[1]}").read()

with open("template.html", "r") as f:
    template = f.read()

    with open("/tmp/index.html", "w") as f:
        f.write(template.replace("{{content}}", content))

os.system("cp retro.css /tmp/retro.css")
os.system('open -a "Safari" /tmp/index.html')
