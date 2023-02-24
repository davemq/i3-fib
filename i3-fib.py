#!/usr/bin/env python3

# Implement one part of a Fibonacci style layout like XMonad has.
# For every new window, toggle its split type.
#
# The other part of a Fibonacci style layout is to specify a ratio
# for the windows. Maybe there's a way to achieve something like that
# with the i3 "resize" command.

from i3ipc import Connection, Event

i3 = Connection()


# handle WindowEvent
def on_new_window(connection, event):
    i3.command("split toggle")


i3.on(Event.WINDOW_NEW, on_new_window)

i3.main()
