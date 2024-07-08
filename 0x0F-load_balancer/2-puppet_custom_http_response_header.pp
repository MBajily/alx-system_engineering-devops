# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task

exec { 'update':
    command => '/usr/bin/apt-get update',
}

package { 'Nginx':
	ensure => 'installed',
	require => Exec['update']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'install_header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'Nginx':
	ensure => running,
	require => Package['Nginx']
}