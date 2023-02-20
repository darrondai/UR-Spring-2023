Execution Instructions: 
Both EspressoChain and LakeOntario are python scripts.
When entering arrays as input in command line, use comma separated values.

Runtimes of all of my examples give 0.0 ms but thats bc my test cases are short

Q1. EspressoChain ------------------------------

Format:
python EspressoChain.py d1,d2,d3 p1,p2,p3 k

Example Inputs/Outputs:
python EspressoChain.py 3,6 50,25 5
Max Profit = 50, Execution Time = 0.1897000038297847 ms

python EspressoChain.py 1,4,6,8,10 3,2,5,6,5 3
Max Profit = 13, Execution Time = 0.3681999951368198 ms

python EspressoChain.py 3,6 25,50 5
Max Profit = 50, Execution Time = 0.3721999964909628 ms

python EspressoChain.py 3,5,9 25,20,10 2
Max Profit: 55, Execution Time: 0.530699995579198 ms

Q2. LakeOntario --------------------------------
python LakeOntario.py d1,d2,d3 M

Example Inputs:
python LakeOntario.py 0,1,1,2,3,3,4,5,6,7,9 2
Min Stops: 5, Execution Time: 0.16540000797249377 ms

python LakeOntario.py 0,1,4,8,13 5
Min Stops: 3, Execution Time: 0.3471999953035265 ms

python LakeOntario.py 0,2,3,5,8 2
Min Stops: inf, Execution Time: 0.331300005200319 ms

python LakeOntario.py 0,4,7,14,19,21 9
Min Stops: 3, Execution Time: 0.24900000425986946 ms
