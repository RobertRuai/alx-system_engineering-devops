#manifest to fix apache server by replacing php typo
#in the settings.php file

exec {'apache_fix':
  path    => '/bin',
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}
