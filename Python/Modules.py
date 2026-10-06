#subprocess - Python is a built-in module that allows Python to run commands that you normally run in the terminal/command prompt.
import subprocess
#subprocess.run(["docker", "images"])
output = subprocess.check_output(
    ["docker", "ps", "-a", "--format", "{{.Names}} {{.Image}}"],
    text=True
)
print(output)