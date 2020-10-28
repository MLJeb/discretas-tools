def zn_value(a: int, n: int):
  return a%n

def add(a: int, b: int, n: int):
  addition = (a + b) % n
  return addition

def multiply(a: int, b: int, n:int):
  product = (a * b) % n
  return product

def additive_inverse(a: int, n: int):
  if(a == 0):
    return a
  return n-a
  
"""For this algorithm i'd imagine that a more efficient version would be on the internet, as my idea was the naviest one
  iterating to find a number x that meets the condition of (a*x)%n == 1
 in that research i found about extended Euclidean Algorithm the Bézout's identity that provides along with the GCD
 a usefulness on the matter of finding de modular multiplicative inverse
 source of that research: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
 source of the python implementation:  https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
"""
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if(a == 0):
      raise ZeroDivisionError
    if (m == 1) : 
        return 0
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
        # Update x and y 
        y = x - q * y 
        x = t 
    # Make x positive 
    if (x < 0) : 
        x = x + m0  
    return x 

def formatted_mod_inverse(a,n):
  try:
    return '{}^-1 = {}'.format(a,modInverse(a,n))
  except ZeroDivisionError:
    return '{} has not inverse'.format(a)

def x_to_multiply(a:int, expected: int, n:int):
  for i in range(0, n):
    if(multiply(a,i,n) == expected):
      result = i
      return result
  
def variable_product(a: int, expected: int, n: int):
  try:
    result = modInverse(a, n)
  except ZeroDivisionError:
    result = x_to_multiply(a,expected,n)
    if(result is None):
      raise ZeroDivisionError
  return result

def cuadratic_adition(a: int, b: int, n:int,neg:int = False):
  aa = multiply(a,a,n)
  ab2 =  multiply(2,multiply(a,b,n),n)
  bb2 = multiply(b,b,n)
  if(neg):
    ab2 = additive_inverse(ab2,n)
  return aa, ab2, bb2


def add_table(n:int):
  matrix = [[add(i,j,n) for j in range(0,n)] for i in range(0,n)]
  return matrix

def multiply_table(n:int):
  matrix = [[multiply(i,j,n) for j in range(0,n)] for i in range(0,n)]
  return matrix

def print_add_table(n:int):
  m = add_table(n)
  for arr in m:
    print(arr)

def print_multiply_table(n:int):
  m = multiply_table(n)
  for arr in m:
    print(arr)
  
class Zn:
  n = 2
  def __init__(self, value):
    self.value = zn_value(value,Zn.n)

  def __add__(self,other):
    a, b = self.value, self.__return_Zn(other)
    return Zn(add(a, b, Zn.n))

  def __sub__(self,other):
    a, b = self.value, additive_inverse(self.__return_Zn(other), Zn.n)
    return Zn(add(a, b, Zn.n))

  def __mul__(self,other):
    a, b = self.value, self.__return_Zn(other)
    return Zn(multiply(a, b, Zn.n))

  def inv(self):
    return Zn(modInverse(self.value, Zn.n))

  def __neg__(self):
    return Zn(additive_inverse(self.value, Zn.n))
  
  def __str__(self):
    return '{}'.format(self.value)

  def __return_Zn(self, other):
  	if(type(other) is int):
  		return zn_value(other, Zn.n)
  	return other.value	
  
def cuadratic_match(x2: Zn, x1: Zn, x0: Zn, value:int):
  solutions = []
  for i in range(Zn.n):
    left_side = x2*i*i + x1*i + x0
    if(left_side == value):
      solutions.append(i)
  return solutions
  
def factors(x2: Zn, x1: Zn, x0: Zn): #use numpy broadcasting for god's sake
  factors = []
  if(x2.value == 1):
    for i in range(0,Zn.n):
      for j in range(0,Zn.n):
        if(Zn(i*j).value == x0.value and Zn(i+j).value == x1.value):
          return [i,j]
  return factors