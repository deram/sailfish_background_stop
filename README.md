# sailfish_background_stop

This script monitors sailfish compositor and sends SIGSTOP and SIGCONT to the command executed through it.

## Motivation
* Mosh can handle loss of connection, and even freezing the process between activations.
* Remote terminal applications rarely benefit from being active while the screen is not visible.
* Keeping the connection up in low connectivity places eat battery very fast.
* Disconnecting and reconnecting to check for activity is annoying.

I wanted a solution that I can keep the mosh connected to screen running in a shell server all the time, 
and not worry about battery being emptied in the morning.

## Results
Can keep up connection for few days with single charging of the Jolla phone battery. 

I consider this a huge boost compared to 100% to 15% in couple of hours forgotten 
on in basement with neglible cellphone coverage.

## Requirements:
* dbus-monitor
* sed
* bash

And the command you intend to run. Mosh in my case.

## Example 1:
Run mosh connection to server in fingerterm (use as command in a .desktop file).

```fingerterm -e "/path/to/bgr_stop.sh mosh -- user@example.com screen -rDU"```


## Example 2:
To run the same mosh command in already opened fingerterm shell, 
exec to replace the original shell to get the correct parent pid set.

```$ exec /path/to/bgr_stop.sh mosh -- user@example.com screen -rDU```
