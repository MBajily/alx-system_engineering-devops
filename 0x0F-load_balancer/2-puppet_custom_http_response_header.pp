# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task

exec {'system update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install_nginx'],
}

exec {'install_nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['HTTP header'],
}

exec { 'HTTP header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart_Nginx'],
}

exec { 'restart_Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}