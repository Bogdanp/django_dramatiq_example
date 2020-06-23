import docker
client = docker.from_env()
redis_container = client.containers.run(
	'redis:3-alpine', 
	detach=True, 
	labels={"type": "redis"},
	name=f"test_redis",
	user="redis",
	ports={
		"6379/tcp":6379
	}
)
