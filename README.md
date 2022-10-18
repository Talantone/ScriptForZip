# usage
Use this script to pack your files to .tar.gz format

# launch
If you want to try this script, you can type `make run` or `python3 main.py`

# additional information for system administrator
If you want to run this script on a schedule, you should get a handle on cron.
Make the script file executable by using the command `sudo chmod a+x main.py`.
Then write `echo '0 0 1 * * cd </path/to/script/folder> ./main.py' > some-file-name` at the root folder. 
After that try to initiate new created file as cron `crontab some-file-name`.
Type `export EDITOR=nano`.
Now you can change file, but it is not necessary.
Use command `crontab -e` to change file.
