def compare(num1, num2):
  if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
    return -1
  if int(str(num1) + str(num2)) > int(str(num2) + str(num1)):
    return 1
  else:
    return 0

def get_maximal_order(data):
  max_order = sorted(data, cmp=lambda x, y: compare(x, y))
  print "Input", data, "Max sum", "".join([str(x) for x in max_order])
  return max_order

if __name__ == "__main__":
  assert(get_maximal_order([100, 9, 9]) == [9, 9, 100])

  assert(get_maximal_order([100, 8, 9]) == [9, 8, 100])
