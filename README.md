# vaulter
This python script is a brute forcer having to wait for a response before moving on.  Having to import string, subprocess, time, and itertools to assist. 
String module was used to use the constant of 'ascii_lowercase'.  Could have provided each lowercase letter, but this was a cleaner apprach.  
The subprocess module was used for executing the 'vault.o' application and the password line argument that the file needed.  
Importing time lets us pause the exectuion of the probgram in case the application crashes from too many attempts too fast.  Thus the need for a timed attack.  
This does lengthen the pocess by quite a bit however.  I also had to add itertools.  Importing string alone wouldn't work and itertools itself.  So needed both string and itertools.

You will need to open terminal and cd to where the vault.o file is and have the v14.py in the same directory.

$python3 v14.py

This will begin starting at the first letter and trying each one until you get a "Success" and the script will wait until you respond.
