# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > * show current working directory path - `pwd`
> > * creating a directory - `mkdir`
> > * deleting a directory - `rmdir`
> > * creating a file using `touch` command - `touch abc.py`
> > * deleting a file - `rm`
> > * renaming a file - `mv`
> > * listing hidden files - `ls -ad .*`
> > * copying a file from one directory to another - `cp` 
> > * copying one director called 'a' to a new directory called 'b' - `cp -r a b`
> > * removing a directory,'hello', along with the files inside it - `rm -rf hello`

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` - Lists all files and folders in the current directory that are not hidden
> > `ls -a` - Lists all files and folders in the current directory including the ones that are hidden. 'a' includes the directory entries whose names begin with (.) 
> > `ls -l` - Gives a detailed list of all files and folders in the current directory that are not hidden. 'l' is for long format
> > `ls -lh` - Gives a detailed list of all files and folders in the current directory that are not hidden with the file/dirctory size abbreviated with unit suffixes like B for Byte, K for Kilibyte, etc. in order to reduce the number of digits to three or less. 'h' is for the file size suffixes.
> > `ls -lah` - Gives a detailed list just like the command 'ls -lh' but the 'a' also includes the hidden files/directories that begin with (.) 
> > `ls -t` -  Lists all files and folders in the current directory that are not hidden in the order of time and date of creation. 't' is for arranging in order of last modification time starting first with the newest and going down to the oldest and then it modifies it inlexicographical order.
> > `ls -Glp` - Lists all files and folders in the current directory that are not hidden with different color codings for files and folders. 'G' is for enabling colorized output with different color codings of files and folders, 'l' is for long list format and 'p' writes a / at the end of each filename if that file is a directory 

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * `ls -lahGp` - 'l' gives a detailed list of all files and folders in the current directory. 'a' includes in the list the files/directories that are hidden.'h' abbreviates the file/directory size with unit suffixes like B for Byte, K for Kilibyte, etc. in order to reduce the number of digits to three or less.'G' enables colorized output with different color codings of files and folders and lastly 'p' writes a / at the end of each filename if that file is a directory  
> > * `ls -R` - 'R' displays subdirectories as well
> > * `ls -1` - '1' displays each entry on a line
> > * `ls -r` - 'r' displays files in reverse order
> > * `ls -p` - 'p' displays directories with /

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` reads data from standard input (stdin) and executes the command (supplied to it as argument) one or more times based on the input read.
> > Example: `xargs touch`   Stdin - a1.txt, b1.txt   ls a1.txt, b1.txt

 

