# This function return each repeated char consecutive once and the number of repeatition.

def run_length_encoding(seq):
  compressed = []
  count = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char:
      count = count + 1
    else :
      compressed.append(char+str(count))
      char = seq[i]
      count = 1
  compressed.append(char+str(count))
  return ''.join(compressed)


a = "aaabbblllqmellr"   # In this example the result is: a3b3l3q1m1e1l2r1
print(run_length_encoding(a))