s,h = map(int, input().split())

s_items=[int(x) for x in input().split()]
cmd = [int(x) for x in input().split()]

move = 0
pos = 0
pickup = 0
for i in range(len(cmd)):
	if cmd[i] == 1:
		if pos == 0:
			pass
		else:
			pos -= 1

	elif cmd[i] == 2:
		if pos == s-1:
			pass
		else:
			pos += 1

	elif cmd[i] == 3:
		if pickup == 1:
			pass
		elif pickup == 0 and s_items[pos] == 0:
			pass
		else:
			if s_items == 0:
				pickup = 0
			else:
				pickup = 1
				s_items[pos] -= 1

	elif cmd[i] == 4:
		if pickup == 1 and s_items[pos] != h:
			pickup = 0
			s_items[pos] += 1

	elif cmd[i] == 0:
		for i in s_items:
			print(i, end=' ')
		exit(0)
