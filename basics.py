#Array 
arr=[1,2,3,4,5]
print(arr)
print(arr[::-1])
print(sum(arr))

#Stack
st=[]
st.append(10)
st.append(20)
print(st)
st.pop()
print(st)

#Queue
from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
print(queue)
queue.popleft()
print(queue)


#Hashmap
freq={}
text="banana"
for char in text:
    freq[char]=freq.get(char,0)+1
print(freq)

#Set
nums=[1,2,2,3,1,5,6,2]
unique= set(nums)
print(unique)
print(2 in unique)


#Recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))