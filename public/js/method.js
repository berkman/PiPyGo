$(document).ready(function() {
  $("#up").click(function(e) {
    $.post("/generator", {"length": $("input[name='length']").val()})
     .done(function(string) {
          alert("Up!");
     });
    e.preventDefault();
  });

  $("#left").click(function(e) {
    alert("Left!")
  });

  $("#right").click(function(e) {
    alert("Right!")
  });

  $("#down").click(function(e) {
    alert("Down!")
  });
});
