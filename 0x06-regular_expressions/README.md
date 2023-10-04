# 0x06 Regular Expression

![DevOps](https://img.shields.io/badge/DevOps-Project-brightgreen)
![By: Sylvain Kalache](https://img.shields.io/badge/By-Sylvain%20Kalache-blue)
![Weight: 1](https://img.shields.io/badge/Weight-1-lightgrey)
![Project Start Date: Oct 3, 2023 6:00 AM](https://img.shields.io/badge/Project%20Start%20Date-Oct%203%2C%202023%206%3A00%20AM-brightgreen)
![Project End Date: Oct 4, 2023 6:00 AM](https://img.shields.io/badge/Project%20End%20Date-Oct%204%2C%202023%206%3A00%20AM-red)
![Checker Released: Oct 3, 2023 12:00 PM](https://img.shields.io/badge/Checker%20Released-Oct%203%2C%202023%2012%3A00%20PM-orange)
![Auto Review at Deadline](https://img.shields.io/badge/Auto%20Review%20at%20Deadline-Yes-green)

## Concepts

For this project, we expect you to look at this concept:
- Regular Expression

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join

sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

Resources
Read or watch:

Regular expressions - basics
Regular expressions - advanced
Rubular is your best friend
Use a regular expression against a problem: now you have 2 problems
Learn Regular Expressions with simple, interactive exercises
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
All your regex must be built for the Oniguruma library
Quiz Questions
Great! You've completed the quiz successfully! Keep going!

Tasks
0. Simply matching School (mandatory)
Requirements:

The regular expression must match "School"
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
1. Repetition Token #0 (mandatory)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
2. Repetition Token #1 (mandatory)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
3. Repetition Token #2 (mandatory)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
4. Repetition Token #3 (mandatory)
Requirements:

Find the regular expression that will match the above cases
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Your regex should not contain square brackets
5. Not quite HBTN yet (mandatory)
Requirements:

The regular expression must be exactly matching a string that starts with 'h', ends with 'n', and can have any single character in between
Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
6. Call me maybe (mandatory)
Requirement:

The regular expression must match a 10-digit phone number
7. OMG WHY ARE YOU SHOUTING? (mandatory)
Requirement:

The regular expression must only match capital letters
