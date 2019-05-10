"""
Problem Code: ZCO15002
Problem Name: Variations
"""
from sys import stdin, stdout

n, k = [int(x) for x in stdin.readline().rstrip().split()]
arr = [int(x) for x in stdin.readline().rstrip().split()]	
arr.sort()
count = 0	
j = 1	
i = 0

while j < n and i < n - 1:
	if arr[j] - arr[i] >= k:
		count += (n - j)
		i += 1
	else:
		j += 1

stdout.write(str(count) + "\n")