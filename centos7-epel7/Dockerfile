FROM centos/s2i-base-centos7

MAINTAINER Dan Callaghan <dcallagh@redhat.com>

ENV PYTHON_VERSION=2.7 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8

LABEL io.k8s.description="Platform for building Python 2.7 web applications as RPM packages on CentOS7 + EPEL7" \
      io.k8s.display-name="Python web app RPM on CentOS7+EPEL7" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,python,python27"

RUN yum -y install --setopt=tsflags=nodocs epel-release

RUN yum -y install --setopt=tsflags=nodocs \
        python-setuptools \
        python-rpm-macros \
        python2-rpm-macros \
        /usr/bin/yum-builddep \
        /usr/bin/rpmbuild \
        && yum -y clean all

COPY ./s2i/bin/ $STI_SCRIPTS_PATH

# Conventionally s2i images set USER 1001, but we need to be root to install 
# RPM packages inside the container.
#USER 1001

EXPOSE 8080

CMD $STI_SCRIPTS_PATH/usage
