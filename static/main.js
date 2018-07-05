function displayUploadFiles() {
    var input = document.getElementById('file');
    var label = input.nextElementSibling
    var labelVal = label.innerHTML;
    var orLabel = input.previousElementSibling;
    var removefile = document.getElementById("removefile");
    removefile.className = "removefileActive";

    var fileName = '';
    if( input.files.length > 1 )
        fileName = ( input.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', input.files.length );
    else
        fileName = input.value.split( '\\' ).pop();

    if( fileName ) {
        label.innerHTML = fileName;
        orLabel.innerHTML = "";
    }
    else
        label.innerHTML = labelVal;
}

function removeFile() {
    var input = document.getElementById('file');
    input.value = null;

    var removefile = document.getElementById("removefile");
    removefile.className = "removefile";

    var label = input.nextElementSibling
    var orLabel = input.previousElementSibling;

    label.innerHTML = "Upload file(s)";
    orLabel.innerHTML = "or";
}