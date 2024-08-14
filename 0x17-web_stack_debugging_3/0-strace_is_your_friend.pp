# to find out why Apache is returning a 500 error

exec { 'fix-wordpress':
  command => 'sed -i "s/\.phpp/\.php/" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'grep -q "\.phpp" /var/www/html/wp-settings.php',
}