OUTPUT_DIR = ./builds

devscp:
	scp -r * root@172.20.1.10:/root/sshpods
	scp -r * root@172.20.1.18:/root/sshpods
	scp -r * root@172.20.1.19:/root/sshpods
	scp -r * root@172.20.1.27:/root/sshpods
	scp -r * root@172.20.1.28:/root/sshpods




devrun:
	ssh root@172.20.1.10  "/root/sshpods/gottylinux -ip 172.20.1.10 bash & > /dev/null &"
	ssh root@172.20.1.18  "/root/sshpods/gottylinux -ip 172.20.1.18 bash & > /dev/null &"
	ssh root@172.20.1.19  "/root/sshpods/gottylinux -ip 172.20.1.19 bash & > /dev/null &"
	ssh root@172.20.1.27  "/root/sshpods/gottylinux -ip 172.20.1.27 bash & > /dev/null &"
	ssh root@172.20.1.28  "/root/sshpods/gottylinux -ip 172.20.1.28 bash & > /dev/null &"


# https://terminal.boxlinker.com:8000/72f644c94f58b048ce32901d38d30672/?container_id=525de4c734b1
# https://terminal.boxlinker.com:8000/a82aad91cc2219f98417329f38d13d51/?container_id=2ee52bf3f956
# https://terminal.boxlinker.com:8000/a84f9f5da1ed442ff3a8ded7bc970e56/?container_id=d08f07d7af4b