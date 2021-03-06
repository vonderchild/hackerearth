"""

Arpasland has surrounded by attackers. A truck enters the city.
The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland.
He doubts about the truck, maybe it's from the siege.
He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel.
Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

Input Format

The first line contains a string of length 9. The format is "DDXDDD-DD",
where D stands for a digit (non zero) and X is an uppercase english letter.

Output Format

Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

SAMPLE INPUT 
12X345-67

SAMPLE OUTPUT
invalid

"""

a = input()
a = list(a)
count = 0
if (int(a[0]) + int(a[1])) % 2 is 0:
    count += 1
if a[2] not in ['A', 'E', 'I', 'O', 'U', 'Y']:
    count += 1
if (int(a[3]) + int(a[4])) % 2 is 0:
    count += 1
if (int(a[4]) + int(a[5])) % 2 is 0:
    count += 1
if (int(a[7]) + int(a[8])) % 2 is 0:
    count += 1

if count is 5:
    print("valid")
else:
    print("invalid")
