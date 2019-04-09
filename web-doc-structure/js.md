# Interaction with Javascript

As of 2012, [it was estimated](https://gist.github.com/jboner/2841832) that the time it took for one packet of data to travel on the internet from the west coast of the U.S. to the Netherlands and back was 150 milliseconds, or 0.15 seconds.  We can take that as a lower bound  on the time required to get a response to an http request, e.g., following a link or submitting a form, if both the web server and the browser were infinitely fast.  And that's a problem.

There are some interactions that take place entirely within the browser, using only the default and built-in behavior of the browser.  For example, when we resize the browser window, the browser may adjust the layout of the web page without any interaction with the server, using only the information available to it in the HTML and CSS of the page it is displaying, without any changes.  This interaction may be fast enough to feel quite interactive.  Likewise, when we are filling in a web form and press the 'k' key, the browser may display a 'k' in the field or possibly a dark circle if we are typing in a password field.  Again, this requires no interaction with the server, and is likely to take much less than  .05 to 0.1 second, which is  about the threshold for an interaction seem "immediate" and fluid.  But if we want a more complex interaction that requires more than the built-in responses of the browser, something programmed for a specific application or requiring information from the server, we cannot achieve a feel of real interactivity by sending an http request and building a new web page with the reply.

Javascript was introduced initially to provide interaction within the browser, without involving additional round trips to the server, and it is still used extensively for this purpose.  In addition, though, Javascript is now used extensively to communicate asynchronously with servers.  Asynchronous communication, in which the client \(browser\) continues interacting with the user while waiting for a response from the server, does not eliminate the latency of the request/response round trip cycle, but it makes  it less jarring because the user interaction is not stalled for that fraction of a second while waiting for a response.  We will look first at Javascript interaction within the browser, and then at the "AJAX" style of asynchronous interaction with a web server.

## The language

Javascript is widely reviled \(but sometimes also loved\) as a programming language.  As you have no doubt heard, it has a syntax that somewhat resembles Java, but is in many other ways completely different from Java. Javascript is a dynamically typed language, meaning _values_ have types but _variables_ do not \(more like Python than Java or C++ in this regard\).  Javascript also does not have a conventional class system like Java, C++, and Python; rather it uses a _delegation_ model like Self and Newtonscript, languages you are unlikely to have encountered.  A Javascript object is roughly like a hashmap in Java or a dict in Python.  Much of the time, for simple scripts, we can almost set the peculiarities of Javascript aside, but occasionally we will find that we must study its workings more deeply to find an effective way to do something.

One of the things that gives Javascript a very different "feel" from Java is that functions in Javascript are first-class objects, meaning they are values just like integers, strings, and floating-point numbers.  For example, we can assign a function to a variable:

```
x = function(t) { return t + 1; }
```

and having done so, we can assign that value to another variable, and then call it.

```
 y = x;
 y(3);
```

If we enter the lines above into a Javascript interpreter, it will show us that y\(3\) returns 4.

Many of the peculiarities of Javascript can be annoying or downright dangerous.  For example, semicolons are used as in Java to terminate statements, but if you omit a semicolon the Javascript interpreter will usually \(but not quite always!\) supply one implicitly, sometimes transforming one bug into a different bug in a way that will complicate debugging.  In some ways Javascript is a victim of rapid success. Javascript has been characterized as  the first draft of a pretty good scripting language.  Most new programming languages go through periods of instability and refinement before they achieve widespread adoption.   When Javascript was introduced, the need for a scripting language was so severe that it was widely adopted almost immediately, with the unfortunate consequence that it became very difficult to make changes that would break existing scripts.  Some refinements have made it into the language, and the current version ES6 has repaired some of the most egregious flaws of the original language \(e.g., by introducing variables with proper block scoping\), but many jagged edges remain for backward compatibility.

There are many Javascript tutorials written for absolute beginners in programming.  [For experienced programmers, we can recommend the Javascript "reintroduction" from the Mozilla organization. ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

## The libraries

Javascript is often used with one or more substantial libraries like JQuery or complete frameworks like Node, Angular, or React.  These libraries and frameworks are extensive and almost like a programming language in themselves, raising the level of Javascript programming while also imposing their own particular style and conceptual model on scripts.  They evolve and are released rapidly, to the extent that the site "[https://dayssincelastjavascriptframework.com/](https://dayssincelastjavascriptframework.com/)" is probably not far from accurate: 

 In this chapter we'll use JQuery, which is rather basic compared to a large framework like Angular, but which also imposes fewer constraints on our applications.  JQuery is very widely used.

Used always with extensive libraries, often with frameworks.  We'll use JQuery, but there are many bigger frameworks widely used \(Angular, React, ...\) and more appearing all the time.

Basics:

Objects are like dicts; JSON is  an exchange format based on object literals \(but only a subset of them\).

Typical use is to "listen" to a field and do something in another field.

## The DOM model:  A web page is a tree

Scripts modify web pages, not as big blocks of text with tags, but as a tree in which tags identify nodes.  A pair of tags &lt;t&gt;..&lt;/t&gt; identify a subtree of element kind \_t, \_e.g., &lt;p&gt;Paragraph text &lt;span&gt;with a span&lt;/span&gt; in it&lt;/p&gt; is a "p" subtree with three children,  two of which are blocks of text and one of which is a "span" subtree.   You can view this tree as an outline in the 'inspector' window of the Firefox web developer tools, and in similar displays in the web development tools of other browsers.

![](/web-doc-structure/img/firefox-show-zombie-dom-small.png)

Javascript listener functions can be attached to elements of the DOM tree so that they will be triggered by events like clicks and mouse hovers,  and Javascript functions can  traverse and modify the content of the tree.   Javascript libraries like JQuery provide very convenient ways to search and traverse the DOM tree with "selector" patterns, e.g., `$(".precis")` to select all the DOM tree nodes with class "precis".

## Scripts and events

\[The basic idea:  Download scripts along wth pages.  Scripts triggered by events; can change the HTML or CSS.\]

The DOM model:  Your HTML is a tree.

## Example?   Maybe color encoder?



