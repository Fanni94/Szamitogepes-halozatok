import socket
import random

#TCP Szerver
hallgato = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hallgato_address = ('localhost', 10000)

#UDP Kliens
tanar = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tanar_address = ('localhost', 10001)

hallgato.bind(hallgato_address)

hallgato.listen(1)
#hallgato.settimeout(1.0)
#tanar.settimeout(1.0)

osszeg = 0
db = 0

try:
	print "Varunk a hallgatora"
	hallgato, hallgato_address = hallgato.accept()
	while True:
		data = hallgato.recv(50)
		print "Hallgatotol kaptam: %s" % data
		if data:
			tanar.sendto(data, tanar_address)
			print "Elkuldtem a tanarnak a jelentkezest"
			jegy, tanar_address = tanar.recvfrom(1024)
			db += 1
			int_jegy = int(jegy)
			osszeg += int_jegy
			print "osszeg: %d, db: %d, atlag: %d" % (osszeg, db, (float(osszeg)/float(db)))
			hallgato.sendall(jegy)
			print "Elkuldtem a hallgatonak a tanar altal kapott jegyet"
		else:
			break;
except socket.error, msg:
	print msg
finally:
	try:
		client
	except NameError:
		pass
	else:
		hallgato.close()
		tanar.close()