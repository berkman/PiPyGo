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

//on RELEASE VS ON CLICK?
