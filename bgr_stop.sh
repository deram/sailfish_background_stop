#!/bin/bash

pid=$$

monitor_background ()
{
  interface=org.nemomobile.compositor
  member=privateTopmostWindowProcessIdChanged
  dbus-monitor --system "interface='${interface}',member='${member}'" 2>/dev/null | \
  sed -n -u 's/ *int32 //p' | \
  while read -r active; do
    if [ "$active" -eq "$PPID" ]; then
      pkill -sigcont -P $pid -n || exit 1
    else
      pkill -sigstop -P $pid -n || exit 1
    fi
  done
}

monitor_background &
"$@"

kill $(jobs -p)
