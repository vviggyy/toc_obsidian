from dotenv import load_dotenv
import os
import glob

load_dotenv()

vault_path = os.getenv("VAULT") #load in Vault path
dns = sorted(os.listdir(vault_path)) # get all daily notes, sort by date

with open(f"{vault_path}/toc.md", "w") as file: #write to toc
    for i in dns:
        file.write(f"[[{i[:-3]}]]\n")
