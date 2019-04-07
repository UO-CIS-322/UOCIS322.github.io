# Interaction with Javascript

As of 2012, [it was estimated](https://gist.github.com/jboner/2841832) that the time it took for one packet of data to travel on the internet from the west coast of the U.S. to the Netherlands and back was 150 milliseconds, or 0.15 seconds.  We can take that as a lower bound  on the time required to get a response to an http request, e.g., following a link or submitting a form, if both the web server and the browser were infinitely fast.  And that's a problem.

There are some interactions that take place entirely within the browser, using only the default and built-in behavior of the browser.  For example, when we resize the browser window, the browser may adjust the layout of the web page without any interaction with the server, using only the information available to it in the HTML and CSS of the page it is displaying, without any changes.  This interaction may be fast enough to feel quite interactive.  Likewise, when we are filling in a web form and press the 'k' key, the browser may display a 'k' in the field or possibly a dark circle if we are typing in a password field.  Again, this requires no interaction with the server, and is likely to take much less than  .05 to 0.1 second, which is  about the threshold for an interaction seem "immediate" and fluid.  But if we want a more complex interaction that requires more than the built-in responses of the browser, something programmed for a specific application or requiring information from the server, we cannot achieve a feel of real interactivity by sending an http request and building a new web page with the reply.

Javascript was introduced initially to provide interaction within the browser, without involving additional round trips to the server, and it is still used extensively for this purpose.  In addition, though, Javascript is now used extensively to communicate asynchronously with servers.  Asynchronous communication, in which the client \(browser\) continues interacting with the user while waiting for a response from the server, does not eliminate the latency of the request/response round trip cycle, but it makes  it less jarring because the user interaction is not stalled for that fraction of a second while waiting for a response.  We will look first at Javascript interaction within the browser, and then at the "AJAX" style of asynchronous interaction with a web server.

## Scripts and events

\[The basic idea:  Download scripts along wth pages.  Scripts triggered by events; can change the HTML or CSS.\]

The DOM model:  Your HTML is a tree.

## The language

Javascript is widely reviled \(but sometimes also loved\) as a programming language.  WAT

It's not Java, or even close,.

Basic characteristics:  Untyped, dynamic, a bit functional;  delegation-based method calls

Used always with extensive libraries, often with frameworks.  We'll use JQuery, but there are many bigger frameworks widely used \(Angular, React, ...\) and more appearing all the time.

Basics:

Objects are like dicts; JSON is  an exchange format based on object literals \(but only a subset of them\).

Typical use is to "listen" to a field and do something in another field.

Example?   Maybe color encoder? 

