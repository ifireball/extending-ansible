FROM centos-systemd
RUN \
	yum install -y epel-release && \
	yum install -y python-pip python-ipython ptpython && \
	yum clean all
ADD src /src
RUN pip install --user /src
