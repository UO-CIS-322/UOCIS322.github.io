# Interaction with Javascript

As of 2012, [it was estimated](https://gist.github.com/jboner/2841832) that the time it took for one packet of data to travel on the internet from the west coast of the U.S. to the Netherlands and back was 150 milliseconds, or 0.15 seconds.  We can take that as a lower bound  on the time required to get a response to an http request, e.g., following a link or submitting a form, if both the web server and the browser were infinitely fast.  That's a problem.

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

To emphasize that 'function \(\) { ... }' really is a function _value_ and not just a declaration, consider that I can also do the following:

```
x = function(k) { 
   y = k + 7; 
   return y; 
}(8);
```

The statement above \(yes, it's a single statement\) will assign the value 15 to x.  Make sure you see why that is, because typical Javascript code is fairly easy to read once you do, but completely wacky until then.

Once you have internalized and gotten comfortable with the basic idea of functions as values in Javascript, you need just a few more foundation stones to grasp enough of the language to start writing useful code. One of these is that an 'object' is essentially like a Java hashmap or a Python dict, with a literal syntax close to Python's except that keys don't need to be quoted if they follow identifier syntax.  We'll illustrate with some interaction in a Javascript interpreter console:

```
> my_obj = { "k1": "v1", k2: "v2", 
...          f: function() { return this.k1; }
... };
{ k1: 'v1', k2: 'v2', f: [Function: f] }
```

Notice that key k2 is "bare", i.e., unquoted, because it is a valid identifier.  We can access object member values using either braces \[ \] or dot notation:

```
> my_obj.k1
'v1'
> my_obj["k1"]
'v1'
```

A member that is a function value can be used as a method, and when called using dot notation has access to the object through the 'this' variable:

```
> my_obj.f(); 
'v1'
```

Javascript has objects that act like something like arrays in Java or lists in Python, but reveal their true nature when twisted:

```
> li = ["a", "b", 7]; 
[ 'a', 'b', 7 ]
> li[99] = "whoa";
'whoa'
> li.length
100
> li[99]
'whoa'
> li[98]
undefined
> li["not_an_integer"] = 13;
13
> li.not_an_integer
13
> li[3.1415] = "Are you serious?";
'Are you serious?'
> li[3.1415]
'Are you serious?'
```

While we can access arrays with a syntax similar to the loop we would write in Java

```
> for (let i=0; i < 2; ++i) { console.log(li[i]); }
a
b
```

But we can also use a more functional style:

```
> li.forEach(function(el) { console.log(el); })
a
b
7
whoa
```

Scope in Javascript is a bit of a mess.  We can use 'let' to introduce a variable in the scope of the current block, 'var' to introduce a variable in scope of the current function, but if we assign to a variable for the first time using neither 'let' nor 'var' the scope will default to global, which is almost never what we want.  Consider:

```
> function litterbug(x) {
...      z = x + x; 
...      q = z + z; 
...      return q; 
... }
undefined
> litterbug(4); 
16
> z
8
```

We accidentally created z and q as global variables!  One way to prevent that mistake is to run Javascript in strict mode.

```
> function litterbug(k) {
...    "use strict"; // Written exactly like this! 
...    x = k + k; 
...    z = x + x; 
...    return z; 
... }
undefined
> litterbug(7)
ReferenceError: x is not defined
    at litterbug (repl:3:6)
```

Many of the peculiarities of Javascript can be annoying or downright dangerous.  For example, semicolons are used as in Java to terminate statements, but if you omit a semicolon the Javascript interpreter will usually \(but not quite always!\) supply one implicitly, sometimes transforming one bug into a different bug in a way that will complicate debugging.  In some ways Javascript is a victim of rapid success. Javascript has been characterized as  the first draft of a pretty good scripting language.  Most new programming languages go through periods of instability and refinement before they achieve widespread adoption.   When Javascript was introduced, the need for a scripting language was so severe that it was widely adopted almost immediately, with the unfortunate consequence that it became very difficult to make changes that would break existing scripts.  Some refinements have made it into the language, and the current version ES6 has repaired some of the most egregious flaws of the original language \(e.g., by introducing variables with proper block scoping\), but many jagged edges remain for backward compatibility.

There are many Javascript tutorials written for absolute beginners in programming.  [For experienced programmers, we can recommend the Javascript "reintroduction" from the Mozilla organization. ](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

## The libraries

Javascript is often used with one or more substantial libraries like JQuery or complete frameworks like Node, Angular, or React.  These libraries and frameworks are extensive and almost like a programming language in themselves, raising the level of Javascript programming while also imposing their own particular style and conceptual model on scripts.  They evolve and are released rapidly, to the extent that [a site purporting to track the number of days](https://dayssincelastjavascriptframework.com/) since a new Javascript framework was introduced is probably not far from accurate:

![](img/days-since-last-js-framework.png)

In this chapter we will initially use just the built-in functions provided by web browsers, including the document object model of the web page, described next.  In the section on "ajax" interaction we will additionally use the jQuery library.  If you pursue web development professionally, you are likely to spend at least as much time learning a more sophisticated Javascript framework as learning the Javascript language, but it is impossible for us to guess which one, and in fact it is quite likely to be one that doesn't yet exist as of this writing.

### The DOM model:  A web page is a tree

Scripts modify web pages, not as big blocks of text with tags, but as a tree in which tags identify nodes.  A pair of tags &lt;t&gt;..&lt;/t&gt; identify a subtree of element kind \_t, \_e.g., &lt;p&gt;Paragraph text &lt;span&gt;with a span&lt;/span&gt; in it&lt;/p&gt; is a "p" subtree with three children,  two of which are blocks of text and one of which is a "span" subtree.   You can view this tree as an outline in the 'inspector' window of the Firefox web developer tools, and in similar displays in the web development tools of other browsers.

![](img/firefox-show-zombie-dom-small.png)

Javascript listener functions can be attached to elements of the DOM tree so that they will be triggered by events like clicks and mouse hovers,  and Javascript functions can  traverse and modify the content of the tree.   That is how we will make elements interactive.

## Scripts and events

Let us suppose we want to present a poem by Pablo Neruda for a student of Spanish literature.  The student may be an English speaker who is not yet fluent in Spanish, but we do not want to provide an English translation by default.  Rather, we want to let the student to attempt to comprehend the poem in Spanish, and to see one line at a time of English translation on request.

We could accomplish this interaction without Javascript.  We could treat each line as a link, so that when the student clicks a line of Spanish poetry, the browser sends a request to the server, which creates and returns a version of the page with some lines translated.  This interaction might take only a fraction of a second, but it would still be too slow.

Instead of interacting with the server each time the user asks to show or hide a line of translation, we can put all of the translated text in the original document, marking spans of the original Spanish text with class "es" and the translated English text "en".

```
  <p><span class="es">
  Quise ser como el pan : <br />
  </span><span class="en">
  I wished to be like bread.<br />
  </span> <span class="es">
  la lucha no me encontr&oacute; ausente.<br />
  </span><span class="en">
  The struggle never found me wanting. <br />
  </span></p>
```

Although tedious to enter by hand, we could easily create a program to generate this html for interleaved Spanish and English text.   Initially we will simply hide all the English, using our style sheet:

```
.es { color: black; }
.en { display: none; }
```

Now the initial appearance of the page is all in Spanish:

![](img/nada-mas-es.png)

We'll create another CSS class to reveal a span of English text.  If there are two CSS selectors that match an element, the more specific selector has priority, so we'll specify both the element type and the class to make the selector for revealing English more specific than the selector for hiding it, when the class `reveal` is applied to a `span` element.

```
span.reveal { display: inline;
          font: italic; 
          color: rgb(150, 50, 50);
        }
```

Now all we need to do is to add the 'reveal' class to selected lines of English translation.  That's where the Javascript comes in.

We'll create the Javascript in a separate file `vtranslate.js`, and link it from the head section of our page:

```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>
<head>
  <title>Neruda: Nada Mas</title>
  <meta charset="utf-8" />
  <link rel="stylesheet" href="vtranslate.css">
  <script src="vtranslate.js" ></script>
</head>
```

In the Javascript file, we'll write an event handling function to "toggle" the "reveal" class for a node.  To "toggle" in this case means to insert the class if it is absent, and delete it if it is present.  Note that our event handler function traverses from a span node with class es to its first sibling node with class en, toggling that sibling if it is found:

```
function toggle_translation(event) {
    // The 'this' object is set automatically in event handlers
    var sib = this.nextElementSibling;
    while (sib) {  // Just in case it isn't the very next sibling
    css_classes = sib.classList;
    if (css_classes.contains("en")) {
        css_classes.toggle("reveal");
        return;
    }
    sib = sib.nextElementSibling; 
    }
    alert("Didn't find translation");
    return;
}
```

The properties `nextElementSibling` and `classList` and the method `toggle` are parts of the DOM API in modern browsers.  They are not a core part of the Javascript language, but all current browsers provide them as part of their built-in API for web pages.

So far so good, but this event handler won't do us any good until we attach it to the spans of Spanish text.  So:

```
document.addEventListener("DOMContentLoaded", function() {  
    let es_elements = document.querySelectorAll(".es");
    for (let i=0; i < es_elements.length; ++i) {
    es_elements[i].addEventListener('click', toggle_translation);
    }
});
```

This code actually adds an event handler to the top-level document object, which represents the web page as a whole.  This handler is triggered when the browser has completely loaded the page and built the DOM.  If we didn't wait for the DOM tree to be completely built, we might miss some of the Spanish text!  Once the DOM is built, we select all of the Spanish spans with a single call to `document.querySelectorAll`, then loop through them to attach the `toggle_translation` handler to each one.

Now, if we click a line of the Spanish text, the `toggle_translation` handler  attaches \(or removes\) the `reveal` class, causing it to match \(or not\) the `span.reveal` selector in our CSS file, giving us the desired effect:

![](img/nada-mas-tr.png)

## Updating the page with Ajax

The interaction we have enabled so far takes place completely within the browser; the web server is not involved.  What if the interaction we want requires some information from a database, or a library or program that is not available on the user's computer?    Of course we could send a request and build a whole new page, but that would defeat the purpose of Javascript and be too slow for some interactions.   We need middle ground:  Exchanging new information with the server but remaining responsive by not blocking other user actions.

We can't prevent the latency of sending a request to the server and receiving a response go away, but we can make it less annoying by making the communication asynchronous:  We send the request, allow the user to continue interacting, and perform some action with the response when it arrives.  We could even have multiple requests "in flight" at the same time.  The action we take upon receiving a response from the server should not be too disruptive.  We may add or change some content on the page, but we should not redraw the whole page while the user is interacting.   This style of server interaction is called "Ajax", for "asynchronous javascript and XML", although today the data sent by the client-side javascript and the response received from the server is usually encoded in javascript object notation \(JSON\) rather than XML.

We will illustrate the Ajax approach with a tiny spelling helper.  As the user begins typing a word, the spelling helper application provides a list of up to five possible completions:

![](img/nanospell.png)

We want to provide the possible word completions keystroke-by-keystroke:  Each time the user adds \(or removes\) a letter in the form entry area, we find and display possible completions.  We don't want to include the whole list of dictionary words in the web page, because that would make the page slow to transmit.  We also don't want to reload the page with each keystroke, because that would be annoying and slow.  Instead, we will leave the dictionary lookup to the server.  With each keystroke, we will send a request to the server with the current content of the input field, and receive from the server a response that could be from zero to six possible words starting with the input text.  For example, if the current input is "we", we might receive the "we", 'weak", "weaken", "weakener", "weakfish", and "week-kneed" in the response.  We display each of these under the input field.

Two aspects of this approach avoid the annoying delays and disruptions of a complete page refresh.  The first, and most important, is that the request will be asynchronous:  Even if the user presses more keys before a response arrives from the server, the input field continues to receive and display the input characters, and eventually the last response is displayed.  Second, the area for displaying responses is updated without refreshing the whole page.

We will focus first on the browser side of this interaction, then look briefly at how it is handled by the server.

### Triggering action on keystrokes

We will attach an event listener to the input field of nanospell.html much as we attached listeners to lines of Spanish poetry in the earlier example, except that this time we will use the jQuery Javascript library.  We load the library \(requesting it from the server\) in the 'head' part of the web page:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NanoSpell</title>
    <link rel="stylesheet" href="/static/nanospell.css" />
    <script src="/static/js/jquery-3.4.0.js"> </script>
</head>
```

In this example we are loading a local copy of the jQuery library.  We could instead have loaded it from a remote content delivery network \(CDN\).  If the same library is used by several different applications, using a CDN can sometimes allow the browser to cache and reuse a library script that another page has loaded.  However, loading scripts from other servers can open an application to a class of security vulnerabilities called cross-site scripting attacks, so we include a digital signature to ensure that the version of the library we obtain has not been modified.  This of course means that we must reference a particular version of the library, rather than indicating we want whichever version is most up-to-date: 

```
<script
  src="https://code.jquery.com/jquery-3.4.0.min.js"
  integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg="
  crossorigin="anonymous"></script>
```

The body of our page will contain an HTML form.  The input field will be labeled "entry" so that we can refer to it from Javascript. 

```
<body>
 <form id="entry">
    <label for="word">Word:</label>
    <input id="word" name="word" type="text" width="25"
      autocomplete="off"  autofocus />
  </form>
  <!-- (more here) -->
</body>
```

We will create an empty "div" element into which our script can insert suggestions, again giving it an identifier so that we can refer to it in our script. 

```
  <div id="suggestions"></div>
```

In our poetry translation application, we used `document.addEventListener` to attach listener functions to elements of the page.  With jQuery we can do the same, a little more concisely.   We want to attach the event listener to the input field we called "entry".  The listener will respond to "key up" events, i.e., it will respond each time the user presses and then releases a key: 

```
<script>
  // ... more here ... 
  
     jQuery(document).ready(function(ev) {
                   jQuery("#word").keyup(be_helpful);
                 });
                 
</script>
```

The outer call to the jQuery listens for the document DOM to be fully loaded.  When the document is loaded, the inner call to `jQuery("#word")` selects elements with identifier "word", i.e., the input field in our form, and attaches to it a function `be_helpful` to be called on each keyup event. 

The function `be_helpful` sends the request to the server.  Since this is an *asynchronous* communication, it does not block while waiting for the reply.  Instead, it schedules another function, `insert_suggestions`, to handle the reply when it arrives: 

```
    /** Ask the server for suggested completions of a word. */
    function be_helpful(event) {
        jQuery.get('/_suggest_completions',  // to the same server that provided the page
                  { "prefix": this.value },  // 'this' is where the keyup happened
                  function(data) {
                    insert_suggestions(data.suggestions);
                  }
        );
    }
```

The data to be transmitted to the server is provided as a Javascript object: 

```
{ "prefix": this.value }
```

The `jQuery.get` method (a shorthand form of `jQuery.ajax`) encodes the object as a parameter in the URL.  The response comes in the form, not of HTML, but another Javascript object represented by Javascript object notation (JSON), e.g., 

```
{"suggestions": ["we", "weak", "weaken", "weakener", "weakfish", "weak-kneed"]}
```

### Updating the Page 

Our function `be_helpful` schedules an anonymous function to handle the response, 
and that function in turn calls `insert_suggestions` to update the page.  

```
   /** Insert suggested completions into the the paragraph
     * with identifier #suggestions
     */
    function insert_suggestions(suggestions) {
        let the_div = jQuery("#suggestions");
        // Clear the old content
        the_div.text("");
        // Insert each suggestion
        suggestions.forEach( function (s) {
            the_div.append(`<p>${s}</p>`);
        });
    }
```

`insert_suggestions` begins by using Query to select the document div element with identify "suggestions".  It clears the div by setting its text to the empty string,
then inserts each suggestions. We could have written a loop in a more familiar form: 

```
       for (let i=0; i < suggestions.length; ++i) {
            the_div.append(`<p>${suggestions[i]}</p>`);
        }
```

We have instead chosen a more "functional" form, using the `forEach` method of 
Javascript arrays and passing it a function to evaluate on each element: 

```
        suggestions.forEach( function (s) {
           the_div.append(`<p>${s}</p>`);
        });
```

The string we append, enclosed in backtick \` marks, is the Javascript approach to *string interpolation*, similar to f-strings in Python. 

### The Server Side

The server side of an Ajax request/response cycle is no different than a request for a web page, with one small exception:  Instead of sending an HTML document, the server encodes some response values in a JSON string, which is usually much smaller, and transmits that as the response.  There is nothing else at all special on the server side.  In fact, for any Ajax call, you give the request URL with data directly in the browser to see the text of the response: 

![Trying the Ajax request as an ordinary URL](img/ajax-direct.png)

## Example source code 

The nanospell example is in the [Samples directory](Samples) in directory ['nanospell'](Samples/nanospell).  It is constructed as a Python application using the Flask web framework.  The Python code for the server side is [flask_server.py](Samples/nanospell/flask_server.py).  The HTML of the page, with embedded Javascript, is in [Samples/nanospell/templates/nanospell.html](Samples/nanospell/templates/nanospell.html).  A stylesheet and a copy of the jQuery library are in the [static](Samples/nanospell/static) subdirectory. 




