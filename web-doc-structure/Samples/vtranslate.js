/* Here: 
 * Javascript (using jquery) that turns individual lines of 
 * English translation "on" and "off" by inserting or removing 
 * the "reveal" class on span.  We listen for click on a spanish
 * line, and turn the following English span into class="en" or 
 * class="en reveal", toggling it. 
 */

// Installation check

function is_it_installed() {
     console.log("It is installed");
}

// JQuery version: 
// function next_english_toggle() {
//     console.log("Click noted");
//     tr = $(this).next(".en");
//     if (tr == null) {
//         console.log("Didn't find translation");
//         return;
//     }
//     tr.toggleClass("reveal");
// }

// "Modern" DOM API version:
function toggle_translation(event) {
    console.log("Click noted");
    // The 'this' object is set automatically in event handlers
    var sib = this.nextElementSibling;
    // The very next element should be the english translation,
    // but we'll search for it just in case. 
    while (sib) {
	console.log("Checking " + sib); 
	css_classes = sib.classList;
	if (css_classes.contains("en")) {
	    css_classes.toggle("reveal");
	    console.log("Toggled!");
	    return;
	}
	sib = sib.nextElementSibling; 
    }
    alert("Didn't find translation");
    return;
}


document.addEventListener("DOMContentLoaded", function() {  
    let es_elements = document.querySelectorAll(".es");
    for (let i=0; i < es_elements.length; ++i) {
	es_elements[i].addEventListener('click', toggle_translation);
    }
});
