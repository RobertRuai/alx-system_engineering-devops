# Fix nginx server requests limit

exec {'increase max files limit':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',
}

exec {'restart nginx server':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
