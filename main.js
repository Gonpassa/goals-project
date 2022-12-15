
// Make the form unable to be sumbitted unless all field are filled in in create.html//
function() {
    $('form > input').keyup(function() {

        var empty = false;
        $('form > input').each(function() {
            if ($(this).val() == '') {
                empty = true;
            }
        });

        if (empty) {
            $('#create').attr('disabled', 'disabled');
        } else {
            $('#create').removeAttr('disabled');
        }
    });
}
