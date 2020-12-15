'''
It is believed by some tribes of South Codelenica that only two events determine the person's destiny: the first time he picked a flower, and the first time he planted one. They also believe in the power of prime numbers and in the power of sums (and a bunch of other most probably unrelated stuff), so you are wondering if it has something to do with their belief in the destiny-determining events.

You know that you first picked a flower in year a of the Codelenican calendar, and planted it in year b. Now you're curious about the sum of all the prime numbers in the range [a, b], to see if this number could possibly affect your life.

Example

For a = 10 and b = 20, the output should be
primesSum(a, b) = 60.

There are 4 prime numbers in the range [10, 20]: 11, 13, 17 and 19. Their sum is equal to 11 + 13 + 17 + 19 = 60. It's a round number, maybe it does mean something?..
'''
def primesSum(a, b):
    return sum([i for i in range(max(a,2),b+1) if not 0 in [i%j for j in range(2,int(i**0.5+1))]])
    # return sum(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))
    # return sum([n for n in range(a, b+1) if n > 1 and all([n % b for b in range(2, int(math.sqrt(n))+ 1)])])
    # return sum(filter(lambda x:len(list(filter(lambda y:x%y==0,range(2,int(x**0.5)+1))))==0,range((lambda x:x+1-x%2)(max(a,2)),b+1,2)))+(2 if a<=2 else 0)
    
def SieveOfEratosthenes(a,b): 
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    result_sum=0
    prime = [True for i in range(b+1)] 
    p=2
    while (p * p <= b): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, b+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, b+1): 
        if prime[p]: 
            if p >= a:
                result_sum +=p
    return result_sum
print(SieveOfEratosthenes(10, 20))