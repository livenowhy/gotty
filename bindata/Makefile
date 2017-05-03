OUTPUT_DIR = ./builds

devscp:
	scp -r * root@172.20.1.10:/root/sshpods
	scp -r * root@172.20.1.18:/root/sshpods
	scp -r * root@172.20.1.19:/root/sshpods
	scp -r * root@172.20.1.27:/root/sshpods
	scp -r * root@172.20.1.28:/root/sshpods




devrun:
	ssh root@172.20.1.10  "/root/sshpods/gottylinux -ip 172.20.1.10 bash >> /root/sshpods/log.log"
	ssh root@172.20.1.18  "/root/sshpods/gottylinux -ip 172.20.1.18 bash >> /root/sshpods/log.log"
	ssh root@172.20.1.19  "/root/sshpods/gottylinux -ip 172.20.1.19 bash >> /root/sshpods/log.log"
	ssh root@172.20.1.27  "/root/sshpods/gottylinux -ip 172.20.1.27 bash >> /root/sshpods/log.log"
	ssh root@172.20.1.28  "/root/sshpods/gottylinux -ip 172.20.1.28 bash >> /root/sshpods/log.log"