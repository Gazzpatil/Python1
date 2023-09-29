s1=input("enter the name")
s2=input("enter the second name:")

if len(s1) != len(s2):
    print("string are not anagram")
else:
    s1 =sorted(s1)
    s2 = sorted(s2)
    if( s1==s2):
        print("string are anagram")
    else:
        print("string are not anagram")    