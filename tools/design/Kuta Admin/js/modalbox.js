$(function() {
	$("a.b-alert").click(function(e) {
		e.preventDefault();
		bootbox.alert("Hello world!", function() {
			console.log("Alert Callback");
		});
	});

	$("a.b-confirm").click(function(e) {
		e.preventDefault();
		bootbox.confirm("Are you sure?", function(confirmed) {
			console.log("Confirmed: "+confirmed);
		});
	});

	$("a.b-prompt").click(function(e) {
		e.preventDefault();
		bootbox.prompt("What is your name?", function(result) {
			console.log("Result: "+result);
		});
	});

	$("a.b-dialog").click(function(e) {
		e.preventDefault();
		bootbox.dialog("I am a custom dialog", [{
			"label" : "Success!",
			"class" : "btn-success",
			"callback": function() {
				console.log("great success");
			}
		}, {
			"label" : "Danger!",
			"class" : "btn-danger",
			"callback": function() {
				console.log("uh oh, look out!");
			}
		}, {
			"label" : "Click ME!",
			"class" : "btn-primary",
			"callback": function() {
				console.log("Primary button");
			}
		}, {
			"label" : "Just a button..."
		}, {
			"Condensed format": function() {
				console.log("condensed");
			}
		}]);
	});

	$("a.b-multiple").click(function(e) {
		e.preventDefault();

		bootbox.alert("Prepare for multiboxes...", "Argh!");

		setTimeout(function() {
			bootbox.confirm("Are you having fun?", "No :(", "Yeah!", function(result) {
				if (result) {
					bootbox.alert("Glad to hear it!");
				} else {
					bootbox.alert("Aww boo. Click the button below to get rid of all these popups", function() {
						bootbox.hideAll();
					});
				}
			});
		}, 1000);
	});

	$("a.b-dialog-close").click(function(e) {
		e.preventDefault();
		var box = bootbox.alert("This dialog will close in two seconds");
		setTimeout(function() {
			box.modal('hide');
		}, 2000);
	});

	$("a.b-generic-modal").click(function(e) {
		e.preventDefault();
		bootbox.modal('<img src="screenshots/blank-image.png" alt=""/>', 'Modal popup!');
	});

	$("a.b-dynamic").click(function(e) {
		e.preventDefault();
		var str = $("<p>This content is actually a jQuery object, which will change in 3 seconds...</p>");
		bootbox.alert(str);
		setTimeout(function() {
			str.html("See?");
		}, 3000);
	});

	$("a.b-onescape").click(function(e) {
		e.preventDefault();
		bootbox.dialog("Dismiss this dialog with the escape key...", {
			"label" : "Press Escape!",
			"class" : "btn-danger",
			"callback": function() {
				console.log("Oi! Press escape!");
			}
		}, {
			"onEscape": function() {
				bootbox.alert("This alert was triggered by the onEscape callback of the previous dialog", "Dismiss");
			}
		});
	});

	$("a.b-nofade").click(function(e) {
		e.preventDefault();
		bootbox.dialog("This dialog does not fade in or out, and thus does not depend on <strong>bootstrap-transitions.js</strong>.",
		{
			"OK": function() {}
		}, {
			"animate": false
		});
	});

	$("a.icons-explicit").click(function(e) {
		e.preventDefault();
		bootbox.dialog("Custom dialog with icons being passed explicitly into <b>bootbox.dialog</b>.", [{
			"label" : "Success!",
			"class" : "btn-success",
			"icon"  : "icon-ok-sign icon-white"
		}, {
			"label" : "Danger!",
			"class" : "btn-danger",
			"icon"  : "icon-warning-sign icon-white"
		}, {
			"label" : "Click ME!",
			"class" : "btn-primary",
			"icon"  : "icon-ok icon-white"
		}, {
			"label" : "Just a button...",
			"icon"  : "icon-picture"
		}]);
	});

	$("a.icons-override").click(function(e) {
		e.preventDefault();
		bootbox.setIcons({
			"OK"      : "icon-ok icon-white",
			"CANCEL"  : "icon-ban-circle",
			"CONFIRM" : "icon-ok-sign icon-white"
		});

		bootbox.confirm("This dialog invokes <b>bootbox.setIcons()</b> to set icons for the standard three labels of OK, CANCEL and CONFIRM, before calling a normal <b>bootbox.confirm</b>", function(result) {
			bootbox.alert("This dialog is just a standard <b>bootbox.alert()</b>. <b>bootbox.setIcons()</b> only needs to be set once to affect all subsequent calls", function() {
				bootbox.setIcons(null);
			});
		});
	});

	$("a.no-close-button").click(function(e) {
		e.preventDefault();
		bootbox.dialog("If a button's handler now explicitly returns <b>false</b>, the dialog will not be closed. Note that if anything <b>!== false</b> - e.g. nothing, true, null etc - is returned, the dialog will close.", [{
			"I'll close on click": function() {
				console.log("close on click");
				return true;
			},
		}, {
			"I won't!": function() {
				console.log("returning false...");
				return false;
			}
		}]);
	});
});