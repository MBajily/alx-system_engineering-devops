# Increase system-wide file descriptor limits
file { '/etc/security/limits.conf':
  ensure  => present,
  content => template('limits/limits.conf.erb'),
  mode    => '0644',
}

# Increase session-wide file descriptor limits
file_line { 'increase-soft-file-limit':
  path  => '/etc/security/limits.conf',
  line  => '* soft nofile 50000',
  match => '^\*\s+soft\s+nofile',
}

file_line { 'increase-hard-file-limit':
  path  => '/etc/security/limits.conf',
  line  => '* hard nofile 50000',
  match => '^\*\s+hard\s+nofile',
}

# Ensure changes take effect immediately
exec { 'reload-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/security/limits.conf'],
}
