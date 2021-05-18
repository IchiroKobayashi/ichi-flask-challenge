import subprocess
from subprocess import PIPE

def initialize_migration():
    subprocess.run("./migration/initialize_migration.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)

def exec_migration():
    subprocess.run("./migration/exec_migration.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)

def exec_seed():
    subprocess.run("./migration/exec_seed.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)
