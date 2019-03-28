\(This is draft text in progress.  Portions are just outline and notes.\)

# HTML + CSS + JS: The components of a web page 

A web page as experienced by the user has three major components:  HTML that contains the structure and main content of the page, CSS that controls its presentation \(layout, typefaces, etc\), and JavaScript that provides interactivity.  In this chapter we describe how these three parts fit together.  Whole volumes have been written about each of the three components, so you won't find an encyclopedic reference here, but you will find enough basic information to get started and build web pages that incorporate all three elements.  Most importantly, you will have enough understanding of the principles underlying the design to help you find and integrate more details when you want to go beyond the basics. 

## Before the beginning: How we got here

Today we take for granted that the world-wide web is a distributed, federated system in which web servers transmit the content of web sites to browsers, which display it to users.  It wasn't always so.  Early hypertext systems were mostly not distributed systems, and did not make a clear distinction between the server and the client \(browser\).  These hypertext systems maintained complex internal records of each user's browsing path.  They were complex.  One of the early systems, HyperCard for the Apple Macintosh, was a fascinating glimpse of the potential of hypertext as a platform.  For example, the first version of the successful  adventure game Myst was implemented as a set of HyperCard "stacks".  But HyperCard was inherently a single computer, single user system.  The few distributed hypertext systems were far more limited, and producing content for them was difficult. 

A key principle of the World-Wide Web as originally designed by Tim Berners-Lee was to create a client/server architecture in which the servers are extremely simple.  A web server does not lay out the text of a web page or combine graphics with text.  It does not determine what typefaces to use, or any other presentation information.  All the web server does is receive a URL and respond by transmitting a file.  The web page is just a text file, and all the server does is transmit it to the client.  The client \(what we call a browser\) is where the page is assembled from its parts, and where all the presentation decisions are made.  If there is a graphic image to be included in the page, the client makes a separate request to the server for the graphic, which transmits the file \(typically a .gif or .jpg\) just as it transmitted the web page. 

The World-Wide Web was quickly successful, and displaced its competitors so thoroughly that today we hardly think of it as just one of the possible ways a hypertext system could be designed.  It has evolved considerably since its inception, but the basic principles of its design that made it successful in the first place remain: 

* The server is dumb.  It just receives individual requests and sends files in reply. _The web server does not interpret the contents of a web page._ 
* The web client \(usually a browser\) interprets the content of a web page, which is usually coded in the hypertext markup language, HTML.  A page may contain links to other material, some of which \(e.g., graphics\) may be included in the presentation of the page to a user.  It is the browser that interprets those links and, as needed, makes additional requests to a web server for the content. That material doesn't even have to come from the same web server.  It is the browser that composes those parts into the page as the user sees it.

One additional principle, weakly present in the original design, has become a pillar of the architecture of the web: 

* The structure and content of a web page, described in HTML, is separate from its presentation, described in CSS, and interactivity, represented in JavaScript. 

## HTML: Structure and Content

Basic structure: Head and body 

Document structure:  h1 ... p etc. 

What's in a tag;  nesting blocks; spans; 

Links and images 

What goes in the head

## Presentation with CSS

Why CSS:  Separation of concerns 

### CSS Structure

Referencing a CSS file from the HEAD

Associating style with an element:   by class, by kind, by name

Composing selectors;  selection by specificity

Debugging CSS selection:  Why isn't this text green? 

### CSS Styling

Page layout: The box model   \(include &lt;div class=...&gt;\)

Dimensions: As pixels, as fractions, as characters 

Positioning: Relative and absolute 





