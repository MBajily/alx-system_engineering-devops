# Increase system-wide file descriptor limits
exec {'replace-1':
  provider => shell,
  command  => 'sed -i "/holberton soft/s/nofile [0-9]*/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['increase-hard-limit'],
}

exec {'increase-hard-limit':
  provider => shell,
  command  => 'sed -i "/holberton hard/s/nofile [0-9]*/nofile 50000/" /etc/security/limits.conf',
}
