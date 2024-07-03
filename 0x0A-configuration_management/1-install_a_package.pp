#!/usr/bin/pup
# Install flask (2.1.0)
package {'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}