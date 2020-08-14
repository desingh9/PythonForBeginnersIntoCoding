#6.) Write a program to check vowel or consonant.
I=(input("please input letter from Small Alphabet: "))

if I in ('a','e','i','o','u'):
    print(" is a vowel ")
else:
    print (" %s is a constant")

#2 step - program to check Charactor is Vowel or Constant
ch=input("please input a Alphabet in Small or Capital letter")
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' ):
    print( "the given alphabet", ch, "is vowel")
else:
    print("the given alphabet", ch, "is Constant")