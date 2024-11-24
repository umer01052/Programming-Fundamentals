#part a(2)
def return_middle(a, b, c):
	middle = a
	if (b > a and b < c) or (b > c and b < a):     	middle = b;
	elif (c > a and c < b) or (c > b and c < a):	middle = c;
	return middle
#part b(2)
def return_average(a, b, c):
	return (a+b+c)/3
#part c(2)
def return_x_power_y(x, y):
    ans = 1
    for i in range(y, 0, -1):
        ans = ans * x
    return ans

#part d(2)
def return_next_vowel(c):
	if c>='a' and c<'e':	return 'e';
	if c>='e' and c<'i':	return 'i';
	if c>='i' and c<'o':	return 'o';
	if c>='o' and c<'u':	return 'u';
	return 'a'		#This statement will execute, if all above statments will become false because return statement is written with all

def main():
	#print("Middle: ", return_middle(-2, 2, 1))
	#print("Middle: ", return_middle(2, -2, -1))
	#print("Middle: ", return_middle(2, 3, -1))
	#print("Average: ", return_average(4, 2, 1))
	#print("Average: ", return_average(2, 6, 5))
	#rint("Average: ", return_average(2, 3, 9))
	#print("2^5: ", return_x_power_y(2, 5))
	#print("3^4: ", return_x_power_y(3, 4))
	print("Next Vowel of t: ", return_next_vowel('t'))
	print("Next Vowel of b: ", return_next_vowel('b'))
	print("Next Vowel of e: ", return_next_vowel('e'))
	print("Next Vowel of i: ", return_next_vowel('i'))
	print("Next Vowel of o: ", return_next_vowel('o'))
	print("Next Vowel of u: ", return_next_vowel('u'))

main()

