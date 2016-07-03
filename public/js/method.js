$(document).ready(function() {
  $("#forward")
    .mousedown(function(e) {
      $.post("/drive", {"motor_direction": "FORWARD"})
        .done(function() {
          $("#motor_direction").val("FORWARD");
        })
    })
    .mouseup(function() {
      $.post("/drive", {"motor_direction": "NONE"})
        .done(function() {
          $("#motor_direction").val("NONE");
        })
    })
  ;

  $("#reverse")
    .mousedown(function(e) {
      $.post("/drive", {"motor_direction": "REVERSE"})
        .done(function() {
          $("#motor_direction").val("REVERSE");
        })
    })
    .mouseup(function() {
      $.post("/drive", {"motor_direction": "NONE"})
        .done(function() {
          $("#motor_direction").val("NONE");
        })
    })
  ;
});
/*
  $("#left")
    .mousedown(function() {
      $("#status").val("LEFT");
    })
    .mouseup(function() {
      $("#status").val("CENTER");
    });

  $("#right")
    .mousedown(function() {
      $("#status").val("RIGHT");
    })
    .mouseup(function() {
      $("#status").val("CENTER");
    });

    $(document).keydown(function(e) {
      switch(e.which) {
          case 37: // left
          $("#status").val("LEFT");
          break;

          case 38: // up
          $("#status").val("UP");
          break;

          case 39: // right
          $("#status").val("RIGHT");
          break;

          case 40: // down
          $("#status").val("DOWN");
          break;

          default: return; // exit this handler for other keys
      }
      e.preventDefault(); // prevent the default action (scroll / move caret)
    });
  */
