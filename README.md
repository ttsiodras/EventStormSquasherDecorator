In a project I've been involved with, the UI team could not
figure out why GTK was sending bursts of events when doing
actions like rolling the mousewheel. Since these events were
associated with DB searches, the performance was unacceptable...

I introduced this decorator, which basically coallesces bursts
of calls (that have inter-arrival times less than the given
decorator argument) to only the last one - so the following
code...

    @delayed(100)  # Coallesce calls that arrive at freq > 10Hz
    def foo(i):
        print("Foo called with", i)

    def test():
        for i in range(1000):
            foo(i)

...will only actually execute the last call (`foo(999)`), 
and will in fact do so 100ms *after* this last call is made.

I hope this code will be useful to others as well - if nothing
else, it's a good example of a complex decorator:

- it has to store the context of the call, regardless of the 
  complexity of the function's arguments
- it has to be able to invoke the call later on (so it basically
  needs to turn the calls into closures)
- it's also using GTK3 timers to schedule the execution later on.
  I had to do this in this project, since the actions must happen
  in the conxtext of the UI thread - but if this is not a requirement
  for you, you can move the timer logic to a worker thread.

Enjoy!
