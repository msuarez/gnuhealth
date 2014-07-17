#!/bin/bash

GNUHEALTH_PATH='/srv/gnuhealth'
AS_VAGRANT='su vagrant'

echo 'Running bootstrap for Vagrant'

echo '.. installing firewall'
apt-get install -y iptables
mkdir -p /etc/iptables
cp $GNUHEALTH_PATH/misc/vagrant/scripts/iptables/iptables.rules /etc/iptables/
iptables-restore < /etc/iptables/iptables.rules
cat - > /etc/network/if-pre-up.d/iptables <<EOF
#!/bin/sh
iptables-restore < /etc/iptables/iptables.rules
EOF
chmod +x /etc/network/if-pre-up.d/iptables

echo '.. checking updates'
apt-get update

echo '.. installing python libraries'
apt-get install -y python-pip python-imaging \
build-essential python-dev libxml2-dev libxslt1-dev \
libldap2-dev libsasl2-dev python-ldap

echo '.. installing PostgreSQL database'
sed -i -e "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g" /etc/locale.gen
locale-gen en_US.UTF-8
export LANGUAGE="en_US.UTF-8"
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
apt-get install -y postgresql postgresql-server-dev-9.1

echo '.. creating the database user'
su - postgres -c "createuser --createdb --no-createrole --no-superuser vagrant"

cd $GNUHEALTH_PATH/tryton

echo '.. starting GNU Health installer'
$AS_VAGRANT ./gnuhealth_install.sh

echo '.. enabling the BASH environment for the vagrant user'
$AS_VAGRANT ./gnuhealthrc

if [ $? -eq 0 ]; then
  echo 'Done.'
else
  echo 'Something failed.'
fi
