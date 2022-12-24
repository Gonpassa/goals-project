
// Make the form unable to be sumbitted unless all field are filled in in create.html//
const fields = document.querySelectorAll('.valid');
const submitButton = document.getElementById('formBtn');
      
function checkFields() {
          let filled = true;
          fields.forEach(function(field) {
            if (field.value === '') {
              filled = false;
            }
          });
          submitButton.disabled = !filled;
}
      
fields.forEach(function(field) {
          field.addEventListener('input', checkFields);
        });


// Send goal_id to the server when pursue button is pressed
document.addEventListener('DOMContentLoaded', function() {
  let buttons = document.querySelectorAll('.dash');
  buttons.forEach(function(button) {
      button.addEventListener('click', function() {
          let goalId = this.getAttribute('data-goal-id');
          let xhr = new XMLHttpRequest();
          xhr.open('POST', '/pursue', true);
          xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
          xhr.onload = function() {
              if (xhr.status === 200) {
                  // handle the response from the server
                  document.body.innerHTML = xhr.response
              }
          };
          xhr.send('goal_id=' + goalId);
      });
  });
});