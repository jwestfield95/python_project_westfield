
This python script will generate  one output file for each string[ATTTGGATT,
ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT,
ATATATATATATATATA] containing a
data frame, and a statement about complexity for each string printed to the command line.

To run this python script, type into the command line:
python3 sub_str_possible.py

to test this python script, type into the command line:
py.test sub_str_poss_test.py
(this will take anything file with _test and test the python script)
in this case the _test file is called sub_str_poss_test
*for some reason this does not seem to work*
The output of the python script should create a data table for each string with linguistic complexity printed after the last k value for each string.


There is also a second python script called automated.py and this script will read in the file called 'testing.txt' containing all three strings seen above. The idea
is that if there were more than just three strings in the file, the script would create a pandas data frame for all strings in the file.

To load the file into python you need to type this code into a python notebook:
myfile= 'testing.txt'
with open(myfile,"r") as f:
    print(f.read())

You can then run the automated.py script into the command line:
python3 automated.py

The output should print out a series of panda data frames having columns for k, observed kmers, and possible kmers, along with the string being run and the linguistic complexity to the command line
