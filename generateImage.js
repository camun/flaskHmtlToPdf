var page = require('webpage').create();
page.open('http://127.0.0.1:5000/leaft', function(status) {
	
  console.log("Status: " + status);
  if(status === "success") {
  	/*window.setTimeout(function () {
            page.render('example.png');
            phantom.exit();
        }, 1000); */
  	page.render('static/map.png');
    phantom.exit();
  }
});