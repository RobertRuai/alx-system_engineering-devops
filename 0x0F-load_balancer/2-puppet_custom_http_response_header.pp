#automate the task of creating a custom HTTP header response

exec {'restart_Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['add_head'],
}

exec {'add_head':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  require     => Exec['install_Nginx'],
}

exec {'install_Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install Nginx',
  require  => Exec['update'],
}

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}
