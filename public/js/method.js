$(document).ready(function(){
  $("#forward").mousedown(function() {
    $.post("/drive", {"drive_direction": "FORWARD"}).done(function() {
      $("#drive_direction").val("FORWARD");
    });
  });

  $("#reverse").mousedown(function() {
    $.post("/drive", {"drive_direction": "REVERSE"});
  });

  $("#left").mousedown(function() {
    $.post("/steer", {"steering_direction": "LEFT"});
  });

  $("#right").mousedown(function() {
    $.post("/steer", {"steering_direction": "RIGHT"});
  });

  $(document).mouseup(function() {
    $.post("/drive", {"drive_direction": "NONE"});
    $.post("/steer", {"steering_direction": "NONE"});
  });
});
