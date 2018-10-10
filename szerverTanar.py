import socket

#UDP Szerver neptunnal
neptun = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
neptun_address = ('localhost', 10001)

#UDP Szerver hallgatoval
hallgato = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hallgato_address = ('localhost', 10002)

#neptun.settimeout(1.0)
#hallgato.settimeout(1.0)
neptun.bind(neptun_address)
hallgato.bind(hallgato_address)

try:
	while True:
		print "Varunk a neptunra"
		data, neptun_address = neptun.recvfrom(1024)
		
		print "kaptam: %s, tole: %s" % (data, neptun_address)
		if data:
			jegy = raw_input("A hallgato jegye: ")
			neptun.sendto(jegy, neptun_address)
			print "Elkuldtem a hallgato jegyet a neptunnak"
			data, hallgato_address = hallgato.recvfrom(1024)
			if data == "elfogadom":
				uzenet = "OK"
				hallgato.sendto(uzenet, hallgato_address)
				print "Valaszoltam a hallgatonak"
except socket.error, m:
	print m
finally:
	neptun.close()
	hallgato.close()