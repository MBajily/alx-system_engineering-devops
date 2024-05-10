#!/usr/bin/env ruby
# output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name
# The receiver phone number or name
# The flags that were used
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
