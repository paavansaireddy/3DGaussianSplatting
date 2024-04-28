import os
import subprocess
import requests

# Change the current working directory to '/content'
os.chdir('/content')

# Check if the directory already exists and remove it if it does
if os.path.exists('gaussian-splatting'):
    subprocess.run(['rm', '-rf', 'gaussian-splatting'])

# Clone the repository from GitHub
subprocess.run(['git', 'clone', '--recursive', 'https://github.com/camenduru/gaussian-splatting'])

# Change the current working directory to the cloned directory
os.chdir('/content/gaussian-splatting/')

# URL of the new 'train.py' file on GitHub
new_train_py_url = 'https://raw.githubusercontent.com/username/repository/branch/path/to/train.py'

# Check if a file named 'train.py' exists in the directory
if os.path.exists("train.py"):
    os.remove("train.py")

# Download the new 'train.py' from GitHub
response = requests.get(new_train_py_url)
if response.status_code == 200:
    with open("train.py", 'wb') as f:
        f.write(response.content)
else:
    print("Failed to download file")