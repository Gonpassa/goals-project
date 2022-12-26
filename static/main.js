
// Make the form unable to be sumbitted unless all field are filled in in create.html//
if (document.querySelector('.formContainer')){
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
      }

// Send goal_id to the server when pursue button is pressed
document.addEventListener('DOMContentLoaded', function() {
  let buttons = document.querySelectorAll('.dash');
  buttons.forEach(function(button) {
      button.addEventListener('click', function() {
          let goalId = this.getAttribute('data-goal-id');
          let xhr = new XMLHttpRequest();
          xhr.open('POST', '/pursue', true);
          xhr.setRequestHeader('Content-Type', 'application/json');
          xhr.onload = function() {
              if (xhr.status === 200) {
                  // handle the response from the server
                  document.open();
                  document.write(this.response);
                  document.close();
              }
          };
          xhr.send(JSON.stringify(goalId));
      });
  });
});

// Goal pursuit. When clicking the button next, the content that is shown should hide, and the next step should show. //

if (document.querySelector('.pursueContainer')){
  document.querySelector('#next').addEventListener('click', hideFirst)

  function hideFirst(){
    let items = document.querySelectorAll('.firstPursue');
    items = Array.from(items);
    items.forEach(item => item.classList.add('hidden'))
    let hidden = document.querySelectorAll('.secondPursue');
    hidden = Array.from(hidden)
    hidden.forEach(element => element.classList.remove('hidden'))

    document.querySelector('#next').classList.add('hidden')
    document.querySelector('#next2').classList.remove('hidden')
  }

  document.querySelector('#next2').addEventListener('click', hideSecond);

  function hideSecond(){
    let secondItems = document.querySelectorAll('.secondPursue');
    secondItems = Array.from(secondItems)
    secondItems.forEach(element => element.classList.add('hidden'))
    document.querySelector('#next2').classList.add('hidden')

    document.querySelector('.end').classList.remove('hidden')
}}