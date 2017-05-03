./gottylinux bash -ip "node节点ip"



scp -r * root@172.20.1.10:/root/sshpods



    
#### 开发环境 
    
    # kubectl get nodes
    172.20.1.10   Ready      174d
    172.20.1.18   Ready      174d
    172.20.1.19   Ready      174d
    172.20.1.27   Ready      174d
    172.20.1.28   Ready      174d
    
    
    /root/sshpods
    
    
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    scp -r bindata/* root@172.20.1.18:/root/sshpods
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    

https://sshpods.boxlinker.com/api/v1.0/sshpods/nodes