//Unused snippets:

// How to hide and show elements:
var x = document.getElementById("testDIV");
if (x.style.display === "none") {
  x.style.display = "block";
} else {
  x.style.display = "none";
}


// from manifest: "content_security_policy": "script-src 'self' https://ajax.googleapis.com; object-src 'self'"

"content_security_policy": "script-src 'self' http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js; object-src 'self'"
