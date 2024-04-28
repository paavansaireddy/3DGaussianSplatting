import os
import requests

# Define the directory where the repo is cloned
directory = '/content/gaussian-splatting'

# Define the URL of the new train.py
url = 'https://raw.githubusercontent.com/paavansaireddy/3DGaussianSplatting/main/train.py'

# Change to the directory
os.chdir(directory)

# Remove the existing train.py file if it exists
if os.path.exists("train.py"):
    os.remove("train.py")

# Download the new train.py from the given URL
response = requests.get(url)
if response.status_code == 200:
    with open("train.py", "wb") as f:
        f.write(response.content)
    print("train.py has been updated.")
else:
    print("Failed to download the file. Status code:", response.status_code)
