#### 启动命令

    ./gottylinux -ip "172.20.1.10" bash
    
    172.20.1.10  node节点ip, bash 要做最后



scp -r * root@172.20.1.10:/root/sshpods



    
#### 开发环境 
    
    # kubectl get nodes
    172.20.1.10   Ready      174d
    172.20.1.18   Ready      174d
    172.20.1.19   Ready      174d
    172.20.1.27   Ready      174d
    172.20.1.28   Ready      174d
    
    
    /root/sshpods
    
    
    
    ssh root@172.20.1.10  "/root/sshpods/gottylinux -ip 172.20.1.10 bash"
    
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    scp -r bindata/* root@172.20.1.18:/root/sshpods
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    scp -r bindata/* root@172.20.1.10:/root/sshpods
    
    
    
    scp id_rsa.pub root@172.20.1.27:/root/liu.pub
    scp id_rsa.pub root@172.20.1.18:/root/liu.pub
    scp id_rsa.pub root@172.20.1.19:/root/liu.pub
    scp id_rsa.pub root@172.20.1.28:/root/liu.pub
    
    
    
    
    172.20.1.10  :--> 72f644c94f58b048ce32901d38d30672
    172.20.1.18  :--> a82aad91cc2219f98417329f38d13d51
    172.20.1.19  :--> 4fcb0c3a5307ba0755c9b38f8c8cc7a5
    172.20.1.27  :--> f55420b42563c2aeed87595b0c38459c
    172.20.1.28  :--> a84f9f5da1ed442ff3a8ded7bc970e56
    

https://sshpods.boxlinker.com/api/v1.0/sshpods/nodes