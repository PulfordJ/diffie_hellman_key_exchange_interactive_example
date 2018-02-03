import diffie_hellman

p = int(input("Specify shared p, 23 works, other user must use the same: "))
g = int(input("Specify shared g, 5 works, other user must use the same: "))

number = -1
while(number < 1 or number > p-1):
    number = int(input("Specify (private!) number between 1 and "+str(p-1)+": "))

print("Public number, give to other user: " + str(int(diffie_hellman.encrypt_integer(g, p, number))))
print()

g = int(input("Specify other users message: "))
print("Common secret (shared password!): " + str(int(diffie_hellman.encrypt_integer(g, p, number))))
print()
