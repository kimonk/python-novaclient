from novaclient.v2 import client
import json
import socket


# nova =  client.client.Client("2.1", "admin", "akis100", "demo","http://192.168.1.7:5000/v2.0")
# bitstream = nova.bitstreams.find(name="lowercase_bitstream_image")
#
# image = nova.images.list()[1]
# flavor = nova.flavors.list()[0]

# nova.servers.create(name="test_lowercase_vnf",bitstream=bitstream,availability_zone="fpga_az")
# nova.servers.create(name="test_lowercase_vnf",image=image,flavor=flavor,availability_zone="fpga_az")

# vnfs= nova.vnfs.create(name="test_lowercase_vnf",bitstream=bitstream,availability_zone="fpga_az")
#
# vnfs = nova.vnfs.list()
# print json.dumps([p._info for p in vnfs], indent=4)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(("192.168.1.7",11))
print "result %s",result
#
#
