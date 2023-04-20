import string
import subprocess
import time
import itertools
#Having to run the application via command line in Linux and supply the actual password it asks for.  Subprocess allows it to run in conjunction with the script
def run_vault(password):
    command = "./vault.o " + password
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = result.communicate()
    return stdout.decode().strip()
#As we are told the password is all lowercase this allows it to grow in length and ad a letter to each attemptNot fast by any means.  
def generate_passwords(length):
    for password in itertools.product(string.ascii_lowercase, repeat=length):
        yield "".join(password)
#So each password that is given is then tried and we are waiting for a response of "Success" while ignoring "Wrong password" and just attempting the next try.  This also waits for a response when the password is success so it just doesn't close on you while it ticks away.
if __name__ == '__main__':
    length = 1
    while True:
        passwords = generate_passwords(length)
        for password in passwords:
            result = run_vault(password)
            print(f"Trying password: {password}")
            if result == "Success":
                print(f"Success! Password is {password}")
                input("Press Enter to exit")
                quit()
            time.sleep(1)
        length += 1
