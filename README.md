# sailfish_background_stop

This script monitors sailfish compositor and sends SIGSTOP and SIGCONT to the command executed through it.

## Example 1:
Run mosh connection to server in fingerterm (use as command in a .desktop file):

```fingerterm -e "/path/to/bgr_stop.sh mosh -- user@example.com screen -rDU"```

## Example 2:
To run the same mosh command in already opened fingerterm shell, 
exec to replace the original shell to get the correct parent pid set.

```$ exec /path/to/bgr_stop.sh mosh -- user@example.com screen -rDU```
