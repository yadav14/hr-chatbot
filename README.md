



an 24 21:55:46 localhost systemd[1]: Created slice Slice /system/rdma-load-modules.
Jan 24 21:55:46 localhost systemd[1]: Starting Load RDMA modules from /etc/rdma/modules/rdma.conf...
Jan 24 21:55:46 localhost systemd[1]: Finished dracut initqueue hook.
Jan 24 21:55:46 localhost systemd[1]: Finished Wait for udev To Complete Device Initialization.
Jan 24 21:55:46 localhost systemd[1]: Reached target Preparation for Remote File Systems.
Jan 24 21:55:46 localhost systemd[1]: Reached target Remote Encrypted Volumes.
Jan 24 21:55:46 localhost systemd[1]: Reached target Remote File Systems.
Jan 24 21:55:46 localhost systemd[1]: Starting dracut pre-mount hook...
Jan 24 21:55:46 localhost systemd[1]: Device-Mapper Multipath Default Configuration was skipped because of an unmet condition check (ConditionKernelCommandLine=rd.multipath=default).
Jan 24 21:55:46 localhost systemd[1]: Starting Device-Mapper Multipath Device Controller...
Jan 24 21:55:46 localhost systemd[1]: Finished dracut pre-mount hook.
Jan 24 21:55:46 localhost systemd-journald[1895]: Missed 11 kernel messages
Jan 24 21:55:46 localhost kernel: iscsi: registered transport (iser)
Jan 24 21:55:46 localhost systemd-modules-load[3627]: Inserted module 'ib_iser'
Jan 24 21:55:46 localhost multipathd[3642]: --------start up--------
Jan 24 21:55:46 localhost multipathd[3642]: read /etc/multipath.conf
Jan 24 21:55:46 localhost multipathd[3642]: /etc/multipath.conf does not exist, blacklisting all devices.
Jan 24 21:55:46 localhost multipathd[3642]: You can run "/sbin/mpathconf --enable" to create
Jan 24 21:55:46 localhost multipathd[3642]: /etc/multipath.conf. See man mpathconf(8) for more details
Jan 24 21:55:46 localhost multipathd[3642]: path checkers start up
Jan 24 21:55:46 localhost multipathd[3642]: /etc/multipath.conf does not exist, blacklisting all devices.
Jan 24 21:55:46 localhost multipathd[3642]: You can run "/sbin/mpathconf --enable" to create
Jan 24 21:55:46 localhost multipathd[3642]: /etc/multipath.conf. See man mpathconf(8) for more details
Jan 24 21:55:46 localhost systemd[1]: Started Device-Mapper Multipath Device Controller.
Jan 24 21:55:46 localhost systemd[1]: Reached target Preparation for Local File Systems.
Jan 24 21:55:46 localhost systemd[1]: Reached target Local File Systems.
Jan 24 21:55:46 localhost systemd-journald[1895]: Missed 13 kernel messages
Jan 24 21:55:46 localhost kernel: Rounding down aligned max_sectors from 4294967295 to 4294967288
Jan 24 21:55:46 localhost kernel: db_root: cannot open: /etc/target
Jan 24 21:55:46 localhost systemd[1]: Starting File System Check on /dev/disk/by-uuid/0f266e9b-6989-4772-b6f6-ffd0174afde8...
Jan 24 21:55:46 localhost systemd-modules-load[3627]: Inserted module 'ib_isert'
Jan 24 21:55:46 localhost systemd-journald[1895]: Missed 2 kernel messages
Jan 24 21:55:46 localhost kernel: ens1f3 speed is unknown, defaulting to 1000
Jan 24 21:55:46 localhost kernel: ens4f3 speed is unknown, defaulting to 1000
Jan 24 21:55:46 localhost systemd-modules-load[3627]: Inserted module 'ib_srpt'
Jan 24 21:55:46 localhost systemd-modules-load[3627]: Inserted module 'rdma_ucm'
Jan 24 21:55:46 localhost systemd-fsck[3656]: /usr/sbin/fsck.xfs: XFS file system.
Jan 24 21:55:46 localhost systemd[1]: Finished File System Check on /dev/disk/by-uuid/0f266e9b-6989-4772-b6f6-ffd0174afde8.
Jan 24 21:55:46 localhost systemd[1]: Mounting /sysroot...
Jan 24 21:55:47 localhost systemd-journald[1895]: Missed 5 kernel messages
Jan 24 21:55:47 localhost kernel: RPC: Registered named UNIX socket transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered udp transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered tcp transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered tcp-with-tls transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered tcp NFSv4.1 backchannel transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered rdma transport module.
Jan 24 21:55:47 localhost kernel: RPC: Registered rdma backchannel transport module.
Jan 24 21:55:47 localhost systemd-modules-load[3627]: Inserted module 'rpcrdma'
Jan 24 21:55:47 localhost systemd[1]: Finished Load RDMA modules from /etc/rdma/modules/rdma.conf.
Jan 24 21:55:47 localhost systemd[1]: Reached target Preparation for Network.
Jan 24 21:55:47 localhost systemd-journald[1895]: Missed 3 kernel messages
Jan 24 21:55:47 localhost kernel: SGI XFS with ACLs, security attributes, scrub, quota, no debug enabled
Jan 24 21:55:47 localhost systemd[1]: Reached target RDMA Hardware.
Jan 24 21:55:47 localhost systemd-journald[1895]: Missed 1 kernel messages
Jan 24 21:55:47 localhost kernel: XFS (sda4): Mounting V5 Filesystem 0f266e9b-6989-4772-b6f6-ffd0174afde8
Jan 24 21:55:47 localhost systemd[1]: Reached target System Initialization.
Jan 24 21:55:47 localhost systemd[1]: Reached target Basic System.
Jan 24 21:55:47 localhost systemd[1]: Persist Osmet Files (ISO) was skipped because of an unmet condition check (ConditionKernelCommandLine=coreos.liveiso).
Jan 24 21:55:47 localhost systemd[1]: Acquire Live PXE rootfs Image was skipped because of an unmet condition check (ConditionPathExists=/run/ostree-live).
Jan 24 21:55:47 localhost systemd[1]: Persist Osmet Files (PXE) was skipped because of an unmet condition check (ConditionPathExists=/run/ostree-live).
Jan 24 21:55:47 localhost systemd-journald[1895]: Missed 5 kernel messages
Jan 24 21:55:47 localhost kernel: XFS (sda4): Starting recovery (logdev: internal)
Jan 24 21:55:47 localhost kernel: XFS (sda4): Ending recovery (logdev: internal)
Jan 24 21:55:47 localhost systemd[1]: Mounted /sysroot.
Jan 24 21:55:47 localhost systemd[1]: Starting OSTree Prepare OS/...
Jan 24 21:55:47 localhost ostree-prepare-root[3676]: Resolved OSTree target to: /sysroot/ostree/deploy/rhcos/deploy/f6d79aa7f74feb7db4d4713c6521d1eec7ea2ed23747e60a159b495b4c7b3a79.0
Jan 24 21:55:47 localhost ostree-prepare-root[3676]: Found legacy sysroot.readonly flag, not configured in ostree/prepare-root.conf
Jan 24 21:55:47 localhost ostree-prepare-root[3676]: sysroot.readonly configuration value: 1 (fs writable: 1)
Jan 24 21:55:47 localhost ostree-prepare-root[3676]: composefs: No image present
Jan 24 21:55:47 localhost ostree-prepare-root[3676]: Using legacy ostree bind mount for /
Jan 24 21:55:47 localhost systemd[1]: sysroot.tmp.mount: Deactivated successfully.
Jan 24 21:55:47 localhost systemd[1]: Finished OSTree Prepare OS/.
Jan 24 21:55:47 localhost systemd[1]: Reached target Initrd Root File System.
Jan 24 21:55:47 localhost systemd[1]: CoreOS Propagate Multipath Configuration was skipped because of an unmet condition check (ConditionKernelCommandLine=rd.multipath=default).
Jan 24 21:55:47 localhost systemd[1]: Starting Mountpoints Configured in the Real Root...
Jan 24 21:55:48 localhost multipathd[3642]: exit (signal)
Jan 24 21:55:48 localhost multipathd[3642]: --------shut down-------
Jan 24 21:55:48 localhost systemd[1]: Stopping Device-Mapper Multipath Device Controller...
Jan 24 21:55:48 localhost systemd[1]: initrd-parse-etc.service: Deactivated successfully.
Jan 24 21:55:48 localhost systemd[1]: Finished Mountpoints Configured in the Real Root.









Warning  FailedScheduling  12m                    default-scheduler  0/2 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.

  Warning  FailedScheduling  2m10s (x2 over 7m10s)  default-scheduler  0/2 nodes are available: pod has unbound immediate PersistentVolumeClaims. preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.



Warning  ProvisioningFailed    7m5s                    rook-ceph.cephfs.csi.ceph.com_csi-cephfsplugin-provisioner-6d8fbb66b7-5hdbw_b7b48ea2-c7be-439c-85eb-d34afc978db8  failed to provision volume with StorageClass "cephfs": rpc error: code = DeadlineExceeded desc = context deadline exceeded
  Normal   ExternalProvisioning  3m28s (x26 over 9m35s)  persistentvolume-controller                                                                                       Waiting for a volume to be created either by the external provisioner 'rook-ceph.cephfs.csi.ceph.com' or manually by the system administrator. If volume creation is delayed, please verify that the provisioner is running and correctly registered.
  Normal   Provisioning          41s (x11 over 9m35s)    rook-ceph.cephfs.csi.ceph.com_csi-cephfsplugin-provisioner-6d8fbb66b7-5hdbw_b7b48ea2-c7be-439c-85eb-d34afc978db8  External provisioner is provisioning volume for claim "vos-bscf/bscf9901-db-pvc"
  Warning  ProvisioningFailed    41s (x10 over 7m4s)     rook-ceph.cephfs.csi.ceph.com_csi-cephfsplugin-provisioner-6d8fbb66b7-5hdbw_b7b48ea2-c7be-439c-85eb-d34afc978db8  failed to provision volume with StorageClass "cephfs": rpc error: code = Aborted desc = an operation with the given Volume ID pvc-73bb04fd-d918-4f5e-b98a-887ab6c7b616 already exists


- name: Update core passwordHash in MachineConfig
  ansible.builtin.replace:
    path: /root/openshift/machine-config-99-set-core-master-password.yaml
    regexp: 'passwordHash:\s*".*"'
    replace: 'passwordHash: "{{ core_password_hash }}"'
  no_log: true
- name: Ensure core passwordHash exists
  ansible.builtin.blockinfile:
    path: /root/openshift/machine-config-99-set-core-master-password.yaml
    insertafter: 'name:\s*core'
    block: |
      passwordHash: "{{ core_password_hash }}"
  no_log: true


- name: Generate core user password hash
  ansible.builtin.set_fact:
    core_password_hash: "{{ core_password_plain | password_hash('sha512') }}"
  no_log: true
oc_tarball: "openshift-client-linux.tar.gz"
installer_tarball: "openshift-install-linux.tar.gz"

oc_url: "{{ openshift_base_url }}/{{ openshift_version }}/{{ oc_tarball }}"
installer_url: "{{ openshift_base_url }}/{{ openshift_version }}/{{ installer_tarball }}"

cluster_dir: "{{ work_dir }}/{{ cluster_name }}"



---
- name: Create working directories
  file:
    path: "{{ item }}"
    state: directory
    mode: '0755'
  loop:
    - "{{ work_dir }}"
    - "{{ cluster_dir }}"

- name: Download OpenShift client (oc)
  get_url:
    url: "{{ oc_url }}"
    dest: "{{ work_dir }}/{{ oc_tarball }}"
    mode: '0644'

- name: Download OpenShift installer
  get_url:
    url: "{{ installer_url }}"
    dest: "{{ work_dir }}/{{ installer_tarball }}"
    mode: '0644'

- name: Extract oc binary
  unarchive:
    src: "{{ work_dir }}/{{ oc_tarball }}"
    dest: "{{ install_dir }}"
    remote_src: yes
    creates: "{{ install_dir }}/oc"

- name: Extract openshift-install binary
  unarchive:
    src: "{{ work_dir }}/{{ installer_tarball }}"
    dest: "{{ install_dir }}"
    remote_src: yes
    creates: "{{ install_dir }}/openshift-install"

- name: Ensure binaries are executable
  file:
    path: "{{ install_dir }}/{{ item }}"
    mode: '0755'
  loop:
    - oc
    - openshift-install

- name: Verify OpenShift installer version
  command: openshift-install version
  register: installer_version
  changed_when: false

- debug:
    msg: "{{ installer_version.stdout }}"

# install-config.yaml must already exist in cluster_dir
- name: Create manifests
  command: >
    openshift-install create manifests
    --dir {{ cluster_dir }}
  args:
    creates: "{{ cluster_dir }}/manifests"

- name: Create agent-based ISO image
  command: >
    openshift-install agent create image
    --dir {{ cluster_dir }}
  args:
    creates: "{{ cluster_dir }}/agent.x86_64.iso"
