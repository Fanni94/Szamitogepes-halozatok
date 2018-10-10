import socket
#TCP alapu
neptun = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
neptun_address = ('localhost', 10000)
neptun.connect(neptun_address)

#UDP alapu
tanar = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tanar_address = ('localhost', 10002)

try:
	while True:
		neptun1 = raw_input("Kerem a neptun kododat: ")
		vizsga1 = raw_input("Kerem az idopontot: ")
		vizsga_jelentkezes = "vizsga, " + neptun1 + ", " + vizsga1
		neptun.send(vizsga_jelentkezes)
		print "Elkuldtem a neptunnak a jelentkezest"
		data = neptun.recv(50)
		jegy = int(data)
		print "Ezt a jegyet kaptam: %s" % jegy
		if jegy <= 3:
			nemtetszik = "reklamalok"
			tanar.sendto(nemtetszik, tanar_address)
			print "Irtam a tanarnak (nem tetszik a jegy)"
		else:
			tetszik = "elfogadom"
			tanar.sendto(tetszik, tanar_address)
			print "Irtam a tanarnak (tetszik a jegy)"
		data, tanar_address = tanar.recvfrom(1024)
		print "kaptam: %s, tole: %s" % (data, tanar_address)
finally:
	neptun.close()
	tanar.close()