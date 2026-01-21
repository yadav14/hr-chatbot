
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
