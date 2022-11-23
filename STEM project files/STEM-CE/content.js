chrome.storage.sync.get(['cb1'], function(items){
    cb1 = items.cb1;
    document.getElementById("checkbox1").checked = cb1;
    if(cb1){
      cb1_clicked()
    }
    else{$("#result").html("off");}
});
function cb1_clicked(){
  console.log("attempting to connect to server...");
  //create_overlay2();
  //create_overlay1();
  connect();
}
document.addEventListener('DOMContentLoaded', function () {
  var btn = document.getElementById('checkbox1');
  if (btn) {btn.addEventListener('click', checkbox1_clicked);}
});
function checkbox1_clicked(){
  cb1 = document.getElementById("checkbox1").checked;
  chrome.storage.sync.set({'cb1': cb1}, function() {});
  if(cb1){
    cb1_clicked();
  }
  else{$("#result").html("off");}
}
/*chrome.runtime.onMessage.addListener(function(request, sender) {
  if (request.action == "getSource") {
    chrome.storage.sync.set({'source_html': request.source}, function() {}); // this is where I have the HTML code
    console.log("source_html set");
  }
});*/

function getHTML(){
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
     chrome.scripting.executeScript(
      {
        target: {tabId: tabs[0].id},
        files: ["getPagesSource.js"],
      }, function() {
        if (chrome.runtime.lastError) {
          message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
        }
      });
  });
}
function connect(){
  console.log("connecting...");
  $("#result").html("connecting...");
  chrome.storage.sync.get(['source_html'], function(items){
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
         siteURL = tabs[0].url;
         getHTML();
         $.ajax({
           url: 'http://localhost:8080/connect',
           type: 'POST', // POST or GET
           data: {
             'url': siteURL,
             'html': items.source_html,
           },
           success: function(result){
             $("#result").html("Buttons: " + result);
           }});
      });

      /*const css = '.center{ outline: 2px solid red; }';
      chrome.scripting.insertCSS(
      {
        target: {tabId: tabs[0].id},
        css: css,
      },
      () => { ... });*/
  });
}
function create_overlay2(){
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.scripting.executeScript(
     {
       target: {tabId: tabs[0].id},
       files: ["inject.css"],
     }, function() {
       if (chrome.runtime.lastError) {
         message.innerText = 'There was an error injecting css : \n' + chrome.runtime.lastError.message;
       }
     });
  });
}
function create_overlay1(){
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    css = 'body { background-color: "red" !important; }';
    $("#result").html("injecting CSS...");
    chrome.scripting.insertCSS(
     {
       target: {tabId: tabs[0].id},
       css: css,
     }, function() {
       if (chrome.runtime.lastError) {
         message.innerText = 'There was an error injecting css : \n' + chrome.runtime.lastError.message;
       }
     });
     $("#result").html("CSS injected...");
  });
}
