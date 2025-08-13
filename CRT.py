import math

#efficient condition for crt
def gcd(nums):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      gcd = math.gcd(nums[i], nums[j])
      if gcd != 1:
        return False
  return True


#compute partial termsw

def partial_terms(nums, remainders, M):
  congruence = []
  mod_inverse = []
  for i in range(len(nums)):
    congruence.append(M/nums[i])
    k = 0
    while (congruence[i] * k) % nums[i] != 1: #modular inverse condition
      k += 1
    mod_inverse.append(k)
  return congruence, mod_inverse


# Helper function for integer input with validation
def get_int_input(prompt):
    while True:
        try:
            value = input(prompt)
            int_value = int(value)
            if float(value) != int_value:
                raise ValueError  # Catch float entered as string like "3.0"
            return int_value
        except ValueError:
            print("Invalid input! Please enter an integer.")


#main execution body
if __name__=="__main__":
  repeats = get_int_input("How many number pairs(divisor and remainder) you want to enter?:  ")
  nums=[]
  remainders = []
  for i in range(repeats):
    nums.append(get_int_input(f"Enter {i+1} divisor: "))
    remainders.append(get_int_input(f"Enter {i+1} remainder: "))
 #<<<<1>>>>
  print(nums, remainders)

#if effecient condition fullfils gcd(i,j)=1
  if gcd(nums):
    print("CRT is possible")
  else:
    print("Invalid Input! \nPlease Enter numbers that are co-prime.")

#finding product of nums
  M = math.prod(nums)
#<<<2>>>
  print(M)

#calling for getting partial terms
  congruence, mod_inverse = partial_terms(nums, remainders, M)
#<<<3>>>
  print(congruence, mod_inverse)

#product for final step in modular inverse
  product = []
  for i in range(len(nums)):
    product.append(congruence[i] * mod_inverse[i] * remainders[i])
#<<<4>>>>
  print(product)

#final result
  result = sum(product) % M
  print(result)
