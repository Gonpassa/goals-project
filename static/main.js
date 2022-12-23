
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