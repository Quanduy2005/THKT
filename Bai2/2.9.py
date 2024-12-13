print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

str=input("Enter a String:") 
dict = {} 
for n in str: 
 keys = dict.keys() 
 if n in keys: 
  dict[n] += 1 
 else: 
  dict[n] = 1 
print (dict) 
