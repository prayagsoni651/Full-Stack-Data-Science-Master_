#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the
number of seconds in a minute (60) by the number of minutes in an hour (also 60).
sol. 60

'''

seconds_in_minute = 60
minutes_in_hour = 60

seconds_in_hour = seconds_in_minute * minutes_in_hour
print(seconds_in_hour)


# In[2]:


'''
2. Assign the result from the previous task (seconds in an hour) to a variable called
seconds_per_hour.
'''

seconds_per_hour = 60 * 60


# In[3]:


'''
3. How many seconds do you think there are in a day? Make use of the variables seconds per hour
and minutes per hour.
'''

seconds_per_hour = 3600
minutes_per_hour = 60

hours_per_day = 24

seconds_per_day = seconds_per_hour * hours_per_day
print(seconds_per_day)




# In[4]:


'''
4. Calculate seconds per day again, but this time save the result in a variable
called seconds_per_day
'''
seconds_per_hour = 3600
hours_per_day = 24

seconds_per_day = seconds_per_hour * hours_per_day
print(seconds_per_day)



# In[5]:


'''
5. Divide seconds_per_day by
seconds_per_hour. Use floating-point (/) division.'''

seconds_per_day = 86400
seconds_per_hour = 3600

result = seconds_per_day / seconds_per_hour
print(result)


# In[6]:


'''
6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree
with the floating-point value from the previous question, aside from the final .0?

'''

seconds_per_day = 86400
seconds_per_hour = 3600

result = seconds_per_day // seconds_per_hour
print(result)


# In[7]:


'''
7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to
its next() method: 2, 3, 5, 7, 11, ...
'''
def genPrimes():
    primes = []  # Store prime numbers generated so far
    num = 2      # Start with the first prime number
    while True:
        # Check if num is prime
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            primes.append(num)  # Add num to the list of primes
        num += 1  # Move to the next number

# Example usage:
prime_generator = genPrimes()
for _ in range(10):
    print(next(prime_generator))



# In[ ]:




