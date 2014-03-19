# What is this spec?

This spec is an attempt to keep autoconf updated to the latest stable version available and to be used on Amazon AWS infrastructure.

# What is the current version?

Autoconf 2.69

# How to build?

Move the repository contents for a directory like that:

    /home/ec2-user/packaging/autoconf

And run rpmbuild:

    cd /home/ec2-user/packaging/autoconf && rm -rf BUILDROOT/* BUILD/* RPMS/x86_64/* RPMS/noarch/* && cd SPECS/ && rpmbuild -ba --buildroot=/home/ec2-user/packaging/autoconf/BUILDROOT --define='_topdir /home/ec2-user/packaging/autoconf' --sign autoconf.spec

# How to install?

To install a new autoconf:

    sudo rpm -ivh /home/ec2-user/packaging/autoconf/RPMS/noarch/autoconf-2.69-1.amzn1.noarch.rpm

To upgrade an existing autoconf installation:

    sudo rpm -Uvh /home/ec2-user/packaging/autoconf/RPMS/noarch/autoconf-2.69-1.amzn1.noarch.rpm

# Sources

This spec is based on Fedora's spec available on http://pkgs.fedoraproject.org/cgit/autoconf.git/.

Also, it has been used the spec of the latest autoconf rpm available on Amazon's repositories.

