# python_project_westfield
This python script will generate  one output file for each string[ATTTGGATT,
ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT,
ATATATATATATATATA] containing a
data frame, and a statement about complexity printed to the command line.

To run this python script, type into the command line:
python3 sub_str_possible.py

to test this python script, type into the command line:
py.test
(this will take anything file with _test and test the python script)
in this case the _test file is called sub_str_poss_test
*for some reason this does not seem to work*
The output of the python script should create a data table for each string with linguistic complexity printed after the last k value for each string:


ATTTGGATT
   k  observed kmers  possible kmers
0  1               3               4
1  2               5               8
2  3               6               7
3  4               6               6
4  5               5               5
5  6               4               4
6  7               3               3
7  8               2               2
8  9               1               1
0.875
ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT
     k  observed kmers  possible kmers
0    1               4               4
1    2              14              16
2    3              31              53
3    4              43              52
4    5              47              51
5    6              49              50
6    7              49              49
7    8              48              48
8    9              47              47
9   10              46              46
10  11              45              45
11  12              44              44
12  13              43              43
13  14              42              42
14  15              41              41
15  16              40              40
16  17              39              39
17  18              38              38
18  19              37              37
19  20              36              36
20  21              35              35
21  22              34              34
22  23              33              33
23  24              32              32
24  25              31              31
25  26              30              30
26  27              29              29
27  28              28              28
28  29              27              27
29  30              26              26
30  31              25              25
31  32              24              24
32  33              23              23
33  34              22              22
34  35              21              21
35  36              20              20
36  37              19              19
37  38              18              18
38  39              17              17
39  40              16              16
40  41              15              15
41  42              14              14
42  43              13              13
43  44              12              12
44  45              11              11
45  46              10              10
46  47               9               9
47  48               8               8
48  49               7               7
49  50               6               6
50  51               5               5
51  52               4               4
52  53               3               3
53  54               2               2
54  55               1               1
0.9738111647139903
ATATATATATATATATA
     k  observed kmers  possible kmers
0    1               2               4
1    2               2              16
2    3               2              15
3    4               2              14
4    5               2              13
5    6               2              12
6    7               2              11
7    8               2              10
8    9               2               9
9   10               2               8
10  11               2               7
11  12               2               6
12  13               2               5
13  14               2               4
14  15               2               3
15  16               2               2
16  17               1               1
0.2357142857142857
