import string
import subprocess
import time

def run_vault(password):
    command = "./vault.o " + password
    subprocess.run(command, shell=True)

def generate_passwords():
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                for l in string.ascii_lowercase:
                    password = i + j + k + l
                    yield password

if __name__ == '__main__':
    passwords = generate_passwords()
    while True:
        password = next(passwords)
        result = run_vault(password)
        print(f"Trying password: {password}")
        if result == "Success":
            print(f"Correct password is: {password}")
            input("Press Enter to exit")
            break
        elif result == "Wrong Password":
            continue
        time.sleep(1)
