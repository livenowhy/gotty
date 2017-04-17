#!/usr/bin/env python
# encoding: utf-8

"""
@version: 0.1
@author: liuzhangpei
@contact: liuzhangpei@126.com
@site: http://www.livenowhy.com
@time: 17/4/17 15:03
"""

"""
woker-api-doc-70ac01f95be8af7539fbec600be78bef-cjk6e   1/1       Running   0          39m
[root@iZ25v6e1euaZ ~]# kubectl get pod woker-api-doc-70ac01f95be8af7539fbec600be78bef-cjk6e -o yml
error: output format "yml" not recognized
[root@iZ25v6e1euaZ ~]# kubectl get pod woker-api-doc-70ac01f95be8af7539fbec600be78bef-cjk6e -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubernetes.io/created-by: |
      {"kind":"SerializedReference","apiVersion":"v1","reference":{"kind":"ReplicationController","namespace":"b5e1b55a-20c3-4fed-b2b1-f7b921e2c1a7","name":"woker-api-doc-70ac01f95be8af7539fbec600be78bef","uid":"cd2f5198-2335-11e7-9473-00163e03018d","apiVersion":"v1","resourceVersion":"19713256"}}
  creationTimestamp: 2017-04-17T06:19:24Z
  generateName: woker-api-doc-70ac01f95be8af7539fbec600be78bef-
  labels:
    component: woker-api-doc
    deployment: 70ac01f95be8af7539fbec600be78bef
    logs: woker-api-docb5e1b55a-20c3-4fed-b2b1-f7b921e2c1a7
    name: woker-api-doc
  name: woker-api-doc-70ac01f95be8af7539fbec600be78bef-cjk6e
  namespace: b5e1b55a-20c3-4fed-b2b1-f7b921e2c1a7
  resourceVersion: "19713338"
  selfLink: /api/v1/namespaces/b5e1b55a-20c3-4fed-b2b1-f7b921e2c1a7/pods/woker-api-doc-70ac01f95be8af7539fbec600be78bef-cjk6e
  uid: cd3ae788-2335-11e7-9473-00163e03018d
spec:
  containers:
  - image: index.boxlinker.com/allreach/woker-api-doc:latest
    imagePullPolicy: Always
    name: woker-api-doc
    ports:
    - containerPort: 80
      protocol: TCP
    resources:
      limits:
        cpu: 200m
        memory: 256M
      requests:
        cpu: 200m
        memory: 256M
    terminationMessagePath: /dev/termination-log
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: default-token-vt4y0
      readOnly: true
  dnsPolicy: ClusterFirst
  imagePullSecrets:
  - name: registry-key
  nodeName: 192.168.1.18
  nodeSelector:
    role: user
  restartPolicy: Always
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  volumes:
  - name: default-token-vt4y0
    secret:
      secretName: default-token-vt4y0
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: 2017-04-17T06:19:31Z
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: 2017-04-17T06:19:35Z
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: 2017-04-17T06:19:31Z
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: docker://6aa8cfac484fe67126c02c6e24aa745e1a323782ec8d0f2554a4abed67665e14
    image: index.boxlinker.com/allreach/woker-api-doc:latest
    imageID: docker://sha256:bc8484c60ca0246a4a00be594b25c80e43236fb3dd1540b63bedea7af9caad96
    lastState: {}
    name: woker-api-doc
    ready: true
    restartCount: 0
    state:
      running:
        startedAt: 2017-04-17T06:19:34Z
  hostIP: 192.168.1.18
  phase: Running
  podIP: 172.16.48.4
  startTime: 2017-04-17T06:19:31Z

"""