#uses pkill command to stop killmenow execution

exec {'pkill':
  path    => '/usr/bin',
  command => 'pkill killmenow',
}
