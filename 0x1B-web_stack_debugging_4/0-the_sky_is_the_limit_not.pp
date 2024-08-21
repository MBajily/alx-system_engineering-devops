# Sky is the limit, let's bring that limit higher
file { '/etc/default/nginx':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  restart    => '/usr/sbin/service nginx reload',
}
