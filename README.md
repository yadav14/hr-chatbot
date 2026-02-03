[root@bastion 25B]# oc get nodes --show-labels
NAME                                STATUS                     ROLES                         AGE    VERSION   LABELS
master1.viairtel.samsungbsc.local   Ready                      control-plane,master,worker   436d   v1.31.9   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,cluster.ocs.openshift.io/openshift-storage=,feature.node.kubernetes.io/network-sriov.capable=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=master1.viairtel.samsungbsc.local,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=,node-role.kubernetes.io/worker=,node.openshift.io/os_id=rhcos,sriovnetwork.openshift.io/device-plugin=Enabled,topology.rook.io/rack=rack0
master2.viairtel.samsungbsc.local   Ready                      control-plane,master,worker   55d    v1.31.9   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,cluster.ocs.openshift.io/openshift-storage=,feature.node.kubernetes.io/network-sriov.capable=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=master2.viairtel.samsungbsc.local,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=,node-role.kubernetes.io/worker=,node.openshift.io/os_id=rhcos,sriovnetwork.openshift.io/device-plugin=Enabled,topology.rook.io/rack=rack1
master3.viairtel.samsungbsc.local   Ready                      control-plane,master,worker   436d   v1.31.9   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,cluster.ocs.openshift.io/openshift-storage=,feature.node.kubernetes.io/network-sriov.capable=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=master3.viairtel.samsungbsc.local,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=,node-role.kubernetes.io/worker=,node.openshift.io/os_id=rhcos,sriovnetwork.openshift.io/device-plugin=Enabled,topology.rook.io/rack=rack2
worker1.viairtel.samsungbsc.local   Ready,SchedulingDisabled   large,worker                  364d   v1.31.9   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,feature.node.kubernetes.io/largeflavor-sriov.capable=true,flavor=large,kubernetes.io/arch=amd64,kubernetes.io/hostname=worker1.viairtel.samsungbsc.local,kubernetes.io/os=linux,node-role.kubernetes.io/large=,node-role.kubernetes.io/worker=,node.openshift.io/os_id=rhcos,sriovnetwork.openshift.io/device-plugin=Enabled
worker2.viairtel.samsungbsc.local   Ready,SchedulingDisabled   large,worker                  364d   v1.31.9   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,feature.node.kubernetes.io/largeflavor-sriov.capable=true,flavor=large,kubernetes.io/arch=amd64,kubernetes.io/hostname=worker2.viairtel.samsungbsc.local,kubernetes.io/os=linux,node-role.kubernetes.io/large=,node-role.kubernetes.io/worker=,node.openshift.io/os_id=rhcos,sriovnetwork.openshift.io/device-plugin=Enabled
[root@bastion 25B]#




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




