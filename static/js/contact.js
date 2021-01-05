$(document).ready(function(){
    $('#three').addClass('underlinePerma');
    $('#submitButton').click(function(){
      var name = $('#senderName').val();
      var email = $('#senderEmail').val();
      var emailRegEx = /\S+@\S+\.\S+/;
      var query = $('#senderQuery').val();
      if(name === "" || name.length <=3 ){
        document.getElementById('nameError').innerHTML = "Please enter a valid name";
        return false;
      }
      if(email === "" || emailRegEx.test(email)==false){
        document.getElementById('emailError').innerHTML = "Please enter a valid email";
        return false;
      }
      if(query === ""){
        document.getElementById('queryError').innerHTML = "Please write something!";
        return false;
      }
      return true;
    })
  })