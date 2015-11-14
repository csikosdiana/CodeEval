message = "012222 1114142503 0313012513 03141418192102 0113 2419182119021713 06131715070119"
message = message.split(" ")
key = "BHISOECRTMGWYVALUZDNFJKPQX"
import string
A = string.ascii_uppercase

Decrypted = []
for i in message:
	m = ""
	for j in range(0, len(i), 2):
		num = int(i[j:(j+2)])
		letter = A[num]
		idx = key.index(letter)
		dec_letter = A[idx]
		m = m + dec_letter
	Decrypted.append(m)
print " ".join(Decrypted)