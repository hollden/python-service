# python-service
Linux: Ubuntu 22.04

Docker: 20.10.20
1.  Install microk8s
```
sudo snap install microk8s --classic --channel=1.27
sudo usermod -a -G microk8s $USER
alias kubectl="microk8s kubectl"
newgrp microk8s
microk8s enable registry ingress
```
2. Install docker according official manual: https://docs.docker.com/engine/install/ubuntu/

3. Clone repository
```
git clone https://github.com/hollden/python-service.git && cd python-service
```

4. Build docker image
```
sudo docker build -t localhost:32000/service:1.0 .
```

5.  add insecure registry to docker daemon
```
sudo bash -c 'cat << EOF > /etc/docker/daemon.json
{
  "insecure-registries" : ["localhost:32000"]
}
EOF'
```

6. Restart docker
```
sudo systemctl restart docker
```

7. Push image to local registry
```
sudo docker push localhost:32000/service:1.0
```

8. Apply cubernetes manifets
```
for manifest in $(ls -1 manifests/); do kubectl apply -f manifests/$manifest; done
```

9. Check whether the pod are running
```
# you should see similar like this
$ kubectl get pod
NAME                                     READY   STATUS    RESTARTS   AGE
my-application-deploy-8696d5c476-tj42h   1/1     Running   0          19m
my-application-deploy-8696d5c476-p2g56   1/1     Running   0          19m
my-application-deploy-8696d5c476-phbhw   1/1     Running   0          19m
```

10. Check service
```
curl localhost -H "Host:my-application.local"
```
