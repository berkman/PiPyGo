$(document).ready(function() {
  $("#up")
    .mousedown(function() {
      $("#status").val("UP");
    })
    .mouseup(function() {
      $("#status").val("");
    });

  $("#left")
    .mousedown(function() {
      $("#status").val("LEFT");
    })
    .mouseup(function() {
      $("#status").val("");
    });

  $("#right")
    .mousedown(function() {
      $("#status").val("RIGHT");
    })
    .mouseup(function() {
      $("#status").val("");
    });

  $("#down")
    .mousedown(function() {
      $("#status").val("DOWN");
    })
    .mouseup(function() {
      $("#status").val("");
    });
});

/*
$.post("/command", {"length": $("input[name='length']").val()})
 .done(function(string) {
    $("#the-string").show();
    $("#the-string input").val(string);
 });
e.preventDefault();
*/
