import math

def numberOfWays(arr, k):
    print('input',arr,k)
    answers={}
    count=0
    map={}
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]].append(i)
        else:
            map[arr[i]]=[i]
    print(map)
    if k/2 in map:
        combo=len(map[k/2])
        count+=combo*(combo-1)/2
        del map[k/2]
    for i in map:
        if k-i in map:
            count+=len(map[k-i])*len(map[i])
            #print('k-i',k-i,map[k-i])
        
    return int(count-1)











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  


