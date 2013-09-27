import struct, serial, time

effects = {
	'hold': 0x41,
	'scroll': 0x42,
	'snow': 0x43,
	'flash': 0x44,
	'hold+flash': 0x45
}

class Sign:

	def __init__(self, devpath):
		# connect to sign via USB
		self.device = serial.Serial(devpath, 38400)

	def setmessage(self, text, slot=1, effect='hold', speed=1):
		# validate message
		if not speed in xrange(1, 6) or not slot in xrange(1, 9) or not effect in effects:
			return

		# write null char packet
		packets = [struct.pack('B', 0x00)]
		
		# write packets for message
		for i in xrange(4):
			packet = struct.pack('BBBB', 0x02, 0x31, 0x05+slot, 0x40*i)
			if i is 0:
				packet += struct.pack('BBBB60s',  0x30+speed, 0x31, effects[effect], len(text), text[:64])
			else:
				packet += struct.pack('64s', text[60+64*(i-1):60+64*i])
			
			# calculate checksum excluding first byte
			checksum = 0
			for byte in packet[1:]:
				checksum += ord(byte)
			checksum %= 256
			packet += struct.pack('B', checksum)

			packets.append(packet)

		# write final packet, including which slot to display
		packets.append(struct.pack('BBB', 0x02, 0x33, pow(2, slot-1)))

		# write packets over serial
		for packet in packets:
			self.device.write(packet)
			time.sleep(0.20)






