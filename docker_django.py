import docker
client = docker.from_env()


network=None

networks=client.networks.list()
for net in networks:
	print(f"Net: {net.name}		{net.id}")
	if(net.name == ("test-net")):
		network = net
if network is None:
	network = client.networks.create("test-net", driver="bridge")

django_container = client.containers.run(
	'threew/dramatiq:1', 
	detach=True, 
	labels={"type": "dramatiq"},
	name=f"test_dramatiq",
	#user="redis",
	ports={
		"8888/tcp":8888
	}
)
#network.connect("test_redis")
network.connect("test_dramatiq")