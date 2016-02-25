window.onload=function() {
  document.getElementById("zipcode").focus();
}

function zipup() {
  var zipcode = document.getElementById('zipcode').value;
  if (zipcode.search(/[abcdefghijklmnopqrstuvwxyz]/i) != -1) {
    alert("Enter a valid zipcode.");
  }
  else {
    if (zipcode.length == 5){
      document.getElementById('landing').removeAttribute('class', 'unactive');
      document.getElementById('landing').setAttribute('class', 'active');
      document.getElementById('landing').innerHTML += "<span class='header-zip'>" + zipcode + '</span>';
    }
  }
}
