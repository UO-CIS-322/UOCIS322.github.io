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

function next_english_toggle() {
    console.log("Click noted");
    tr = $(this).next(".en");
    if (tr == null) {
        console.log("Didn't find translation");
        return;
    }
    tr.toggleClass("reveal");
}

$(document).ready( function() {
    $(".es").click(next_english_toggle);
});

