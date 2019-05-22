extending-ansible
=================
Code for PyCON-IL 2019 Extending Ansible talk

Running the code here
---------------------

### Installing needed software

This project uses [Docker][1] to run some containers to emulate hosts
that Ansible works with. You will need to follow the instructions for
having Docker installed on your operating system to proceed.

Python dependencies for this project are managed via [pipenv][2]. You
can install it with:

    pip install -u pipenv

Once you have `pipenv` installed, you can install this project's
dependencies into a Python virtual environment with:

    pipenv install

[1]: https://www.docker.com/
[2]: https://github.com/pypa/pipenv

### SElinux settings

If you're running on a Linux machine with SElinux enabled, you need to
enable containers to create cgroups by running the following command:

    sudo setsebool -P container_manage_cgroup 1

### Bringing up test systems

To bring up the test containers you can run the following command:

    pipenv run docker-compose up -d

### Shutting things down

To shot down the containers simply run:

    pipenv run docker-compose down

### Running the playbooks

First start up the test containers as explained above, then you can run
the playbooks with the following command:

    pipenv run ansible-playbook \
        -i playbooks/inventories/test-containers.yaml \
        playbooks/${playbook_name}

Where `${playbook_name}` is the name of the playbook you want to run.
For example, to run the 'example' playbook:

    pipenv run ansible-playbook \
        -i playbooks/inventories/test-containers.yaml \
        playbooks/example.yaml
