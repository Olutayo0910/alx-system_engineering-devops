## Processes and Signals in Bash

Tasks
0. What is my PID (mandatory)
Write a Bash script that displays its own PID.

Example:

bash
Copy code
sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
1. List your processes (mandatory)
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those that might not have a TTY.
Display in a user-oriented format.
Show process hierarchy.
Example:

bash
Copy code
sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
...
sylvain@ubuntu$
2. Show your Bash PID (mandatory)
Using your previous script command, write a Bash script that displays lines containing the word 'bash', allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep.
The third line of your script must be # shellcheck disable=SC2009.
Example:

bash
Copy code
sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_pid
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
sylvain@ubuntu$
3. Show your Bash PID made easy (mandatory)
Write a Bash script that displays the PID, along with the process name, of processes whose name contains the word 'bash'.

Requirements:

You cannot use ps.
Example:

bash
Copy code
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$
4. To infinity and beyond (mandatory)
Write a Bash script that displays "To infinity and beyond" indefinitely.

Requirements:

Add a sleep 2 between each iteration of the loop.
Example:

bash
Copy code
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
sylvain@ubuntu$
5. Don't stop me now! (mandatory)
We stopped the '4-to_infinity_and_beyond' process using ctrl+c in the previous task, but there's another way to do this. Write a Bash script that stops the '4-to_infinity_and_beyond' process.

Requirements:

You must use kill.
Example:

bash
Copy code
# Terminal #0
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
# Press Ctrl+C to stop the process

# Terminal #1
sylvain@ubuntu$ ./5-dont_stop_me_now
# The '4-to_infinity_and_beyond' process is stopped
sylvain@ubuntu$
6. Stop me if you can (mandatory)
Write a Bash script that stops the '4-to_infinity_and_beyond' process.

Requirements:

You cannot use kill or killall.
Example:

bash
Copy code
# Terminal #0
sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
# Press Ctrl+C to stop the process

# Terminal #1
sylvain@ubuntu$ ./6-stop_me_if_you_can
# The '4-to_infinity_and_beyond' process is stopped
sylvain@ubuntu$
7. Highlander (mandatory)
Write a Bash script that displays "To infinity and beyond" indefinitely. It should also display "I am invincible!!!" when receiving a SIGTERM signal. Make a copy of your '6-stop_me_if_you_can' script, name it '67-stop_me_if_you_can', and make it kill the '7-highlander' process instead of the '4-to_infinity_and_beyond' one.

Example:

bash
Copy code
# Terminal #0
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
sylvain@ubuntu$

# Terminal #1
sylvain@ubuntu$ ./67-stop_me_if_you_can
# The '7-highlander' process is stopped
sylvain@ubuntu$
8. Beheaded process (mandatory)
Write a Bash script that kills the '7-highlander' process.

Example:

bash
Copy code
# Terminal #0
sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
sylvain@ubuntu$

# Terminal #1
sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$
