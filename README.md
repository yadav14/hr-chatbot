



[root@bastion 25B]# oc get net-attach-def -n openshift-storage
NAME                 AGE
ocs-public-cluster   3h36m
[root@bastion 25B]# oc describe net-attach-def ocs-public-cluster -n openshift-storage
Name:         ocs-public-cluster
Namespace:    openshift-storage
Labels:       <none>
Annotations:  <none>
API Version:  k8s.cni.cncf.io/v1
Kind:         NetworkAttachmentDefinition
Metadata:
  Creation Timestamp:  2026-02-03T07:09:42Z
  Generation:          2
  Resource Version:    298960671
  UID:                 c94c42ab-28ea-4547-ac0c-a2ae0f4bc3d3
Spec:
  Config:  { "cniVersion": "0.3.1", "type": "macvlan", "master": "bond1-mvlan", "mode": "bridge", "ipam": { "type": "whereabouts", "range": "20.1.15.0/23", "exclude": [ "20.1.15.102/32", "20.1.15.103/32", "20.1.15.104/32", "20.1.15.105/32", "20.1.15.106/32" ], "routes": [ {"dst": "20.1.15.0/23"} ] } }
Events:    <none>
[root@bastion 25B]# oc get network
NAME      AGE
cluster   436d
[root@bastion 25B]# oc get network  cluster -o yaml
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  creationTimestamp: "2024-11-23T13:04:51Z"
  generation: 62
  name: cluster
  resourceVersion: "297514131"
  uid: 9548a3a7-8ffe-4eb8-b4ba-3e67ed3a9c27
spec:
  clusterNetwork:
  - cidr: 10.20.0.0/16
    hostPrefix: 24
  - cidr: fd01::/48
    hostPrefix: 64
  externalIP:
    policy: {}
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.21.0.0/16
  - fd02::/112
status:
  clusterNetwork:
  - cidr: 10.20.0.0/16
    hostPrefix: 24
  - cidr: fd01::/48
    hostPrefix: 64
  clusterNetworkMTU: 8400
  conditions:
  - lastTransitionTime: "2026-01-31T08:20:59Z"
    message: ""
    observedGeneration: 0
    reason: AsExpected
    status: "True"
    type: NetworkDiagnosticsAvailable
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.21.0.0/16
  - fd02::/112




