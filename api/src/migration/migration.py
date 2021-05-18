import subprocess
from subprocess import PIPE

def initialize_migration():
    subprocess.run("./migration/initialize_migration.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)

def execute_migration():
    subprocess.run("./migration/execute_migration.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)

def exec_seed():
    subprocess.run("./migration/exec_seed.sh", shell=False, stdout=PIPE, stderr=PIPE, text=True)
