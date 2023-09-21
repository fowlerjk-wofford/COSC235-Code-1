count = 0
keep_going = True

word = input()
while keep_going:
  count += 1
  print(count)
  word = input()
  if word != 'quit':
    keep_going = True
  else:
    keep_going = False
