# create a file in /tmp.


file { 'dee_alx_with_puppet_lint':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  path    => '/tmp/school',
}