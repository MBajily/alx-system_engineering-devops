file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/home/vagrant/.ssh/config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/home/vagrant/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}