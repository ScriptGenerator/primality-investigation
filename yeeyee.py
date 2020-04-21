import math

c = [0] * 100000;
def coef(n): 
	c[0] = 1; 
	for i in range(n): 
		c[1 + i] = 1; 
		for j in range(i, 0, -1): 
			c[j] = c[j - 1] - c[j]; 
		c[0] = -c[0]; 
def isPrime(n): 
	coef(n); 
	c[0] = c[0] + 1; 
	c[n] = c[n] - 1; 
	i = n; 
	while (i > -1 and c[i] % n == 0): 
		i = i - 1;
	return True if i < 0 else False;

#defining the prime functions generators 
def pythagorean_prime(n): return (4*n + 1)
def kynea_prime(n): return (((2**n)+1)**2)-2
def carol_prime(n): return (((2**n)-1)**2)-2
def mersenne_prime(n): return (2**n)-1
def cuban_prime(n): return (3*(n**2))+(3*n)+1
def factorial_prime_upper(n): return (math.factorial(n)+1)
def factorial_prime_lower(n): return (math.factorial(n)-1)
def newman_prime(n): return int(round((((1+ math.sqrt(2))**n) + ((1 - math.sqrt(2))**n))/2, 1))
def thabit_prime(n): return (3*(2**n))-1
def wagstaff_prime(n): return round(((2**n)+1)/3, 0)
def woodall_prime(n): return (n*(2**n))-1

data = {
	"pythagorean_prime":{},
	"kynea_prime":{},
	"carol_prime":{},
	"mersenne_prime":{},
	"cuban_prime":{},
	"factorial_prime_upper":{},
	"factorial_prime_lower":{},
	"newman_prime":{},
	"thabit_prime":{},
	"wagstaff_prime":{},
	"woodall_prime":{}
}



def lol(o):
# generating all the primes 
	All_primes = [l for l in range(1,o) if isPrime(l)]
	print("-"*20)
	print("o = ",o)

	pythagorean_primes = [pythagorean_prime(i) for i in range(1,o) if (pythagorean_prime(i)<=o and isPrime(i))]
	print("pythagorean primes : {0} %  (found {1} in total of {2})".format((len(pythagorean_primes)/len(All_primes))*100, len(pythagorean_primes), len(All_primes)))
	data["pythagorean_prime"][o] = (len(pythagorean_primes)/len(All_primes))*100

	kynea_primes = [kynea_prime(i) for i in range(1,o) if (kynea_prime(i)<=o and isPrime(i))]
	print("kynea primes : {0} %  (found {1} in total of {2})".format((len(kynea_primes)/len(All_primes))*100, len(kynea_primes), len(All_primes) ))
	data["kynea_prime"][o] = (len(kynea_primes)/len(All_primes))*100

	carol_primes = [carol_prime(i) for i in range(1,o) if (carol_prime(i)<=o and isPrime(i))]
	print("carol primes : {0} %  (found {1} in total of {2})".format((len(carol_primes)/len(All_primes))*100, len(carol_primes), len(All_primes)))
	data["carol_prime"][o] = (len(carol_primes)/len(All_primes))*100

	mersenne_primes = [mersenne_prime(i) for i in range(1,o) if (mersenne_prime(i)<=o and isPrime(i))]
	print("mersenne primes : {0} %  (found {1} in total of {2})".format((len(mersenne_primes)/len(All_primes))*100, len(mersenne_primes), len(All_primes)))
	data["mersenne_prime"][o] = (len(mersenne_primes)/len(All_primes))*100

	cuban_primes = [cuban_prime(i) for i in range(1,o) if (cuban_prime(i)<=o and isPrime(i))]
	print("cuban primes : {0} %  (found {1} in total of {2})".format((len(cuban_primes)/len(All_primes))*100, len(cuban_primes), len(All_primes)))
	data["cuban_prime"][o] = (len(cuban_primes)/len(All_primes))*100

	factorial_primes_increase = [factorial_prime_upper(i) for i in range(1,o) if (factorial_prime_upper(i)<=o and isPrime(i))]
	print("factorial primes (increase) : {0} %  (found {1} in total of {2})".format((len(factorial_primes_increase)/len(All_primes))*100, len(factorial_primes_increase), len(All_primes)))
	data["factorial_prime_upper"][o] = (len(factorial_primes_increase)/len(All_primes))*100

	factorial_primes_decrease = [factorial_prime_lower(i) for i in range(1,o) if (factorial_prime_lower(i)<=o and isPrime(i))]
	print("factorial primes (decrease) : {0} %  (found {1} in total of {2})".format((len(factorial_primes_decrease)/len(All_primes))*100, len(factorial_primes_decrease), len(All_primes)))
	data["factorial_prime_lower"][o] = (len(factorial_primes_decrease)/len(All_primes))*100

	newman_primes = [newman_prime(i) for i in range(1,o) if (newman_prime(i)<=o and isPrime(i))]
	print("newman primes : {0} %  (found {1} in total of {2})".format((len(newman_primes)/len(All_primes))*100, len(newman_primes), len(All_primes)))
	data["newman_prime"][o] = (len(newman_primes)/len(All_primes))*100

	thabit_primes = [thabit_prime(i) for i in range(1,o) if (thabit_prime(i)<=o and isPrime(i))]
	print("thabit primes : {0} %  (found {1} in total of {2})".format((len(thabit_primes)/len(All_primes))*100, len(thabit_primes), len(All_primes)))
	data["thabit_prime"][o] = (len(thabit_primes)/len(All_primes))*100

	wagstaff_primes = [wagstaff_prime(i) for i in range(3,o) if (wagstaff_prime(i)<=o and isPrime(i))]
	print("wingstaff primes : {0} %  (found {1} in total of {2})".format((len(wagstaff_primes)/len(All_primes))*100, len(wagstaff_primes), len(All_primes)))
	data["wagstaff_prime"][o] = (len(wagstaff_primes)/len(All_primes))*100

	woodall_primes = [woodall_prime(i) for i in range(3,o) if (woodall_prime(i)<=o and isPrime(i))]
	print("woodall primes : {0} %  (found {1} in total of {2})".format((len(woodall_primes)/len(All_primes))*100, len(woodall_primes), len(All_primes)))
	data["woodall_prime"][o] = (len(woodall_primes)/len(All_primes))*100



e=81

for i in range(1,e):
	lol(i*10)

print(data)

with open("C:\\Users\\ahmed\\OneDrive\\Desktop\\data.csv","w+") as file:
	for i in range(1,e):
		file.write(str(i*10)+", ")
	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["pythagorean_prime"][o])+", ")
	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["kynea_prime"][o])+", ")
	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["carol_prime"][o])+", ")
	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["mersenne_prime"][o])+", ")
	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["cuban_prime"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["factorial_prime_upper"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["factorial_prime_lower"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["newman_prime"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["thabit_prime"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["wagstaff_prime"][o])+", ")

	file.write("\n")
	for t in range(1,e):
		o=10*t 
		file.write( str(data["woodall_prime"][o])+", ")

	file.write("\n")