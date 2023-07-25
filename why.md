# "Why is `future_router` is created?"

In short answer, f**k import hell.

In long answer, i was found myself in a special condition where specific module depends on other module which depends on the first module,
multiple files and directories. Code were co-dependant to each other because of inability of future-purpose.
I made this specifically to not enclose the app-creation within simple function.

All it takes is only `Router()`
