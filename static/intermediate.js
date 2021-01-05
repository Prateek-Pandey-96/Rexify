$(document).ready(function(){
    var emailRegEx = /\S+@\S+\.\S+/;
    var nameError =  document.getElementById("customerNameError");
    var emailError =  document.getElementById("customerEmailError");
    var jobError =  document.getElementById("customerJobError");
    var phoneError =  document.getElementById("customerPhoneError");
    var objectiveError = document.getElementById("customerObjectiveError");
    $('#customerName').on("input", function(){
        if ($(this).val().length <= 5 )
        {
            nameError.innerHTML = "Please enter a valid name!";
        }
        else
            {
                nameError.innerHTML = ""; 
            }
    })
    $('#customerEmail').on("input", function(){      
        if (emailRegEx.test($(this).val()) == false )
            emailError.innerHTML = "Please enter a valid email!";
        else
            emailError.innerHTML = "";
    })
    $('#customerJob').on("input", function(){    
        if ($(this).val().length <= 5 )
            jobError.innerHTML = "Please enter a valid job!";
        else
            jobError.innerHTML = "";
    })
    $('#customerPhone').on("input", function(){
        if ($(this).val().length != 10 && $(this).val().length != 11 && $(this).val().length != 12)
            phoneError.innerHTML = "Please enter a valid phone number!";
        else
            phoneError.innerHTML = "";
    })
    $('#customerObjective').on("input", function(){
        if ($(this).val().length <=100)
            objectiveError.innerHTML = "Objective should be appropriate!";
        else
            objectiveError.innerHTML = "";
    })
    $('#intermediateButton').click(function(){
        if($('#customerName').val().length === 0 && $('#customerEmail').val().length === 0 && $('#customerJob').val().length === 0 &&
            $('#customerPhone').val().length === 0 && $('#customerObjective').val().length === 100)
        {
            document.getElementById('formError').innerHTML = "Please fill the form properly";
        }
        var check = $('#customerName').val().length > 5 && emailRegEx.test($('#customerEmail').val()) && $('#customerJob').val().length > 5 &&
                    ($('#customerPhone').val().length != 10 || $('#customerPhone').val().length != 11 || $('#customerPhone').val().length != 12) && 
                    $('#customerObjective').val().length > 100;
        if( check && nameError.innerHTML === "" && emailError.innerHTML === "" && jobError.innerHTML === "" && phoneError.innerHTML === "" && objectiveError.innerHTML === "")
        {  
            return true;  
        }
        else
        {     
            document.getElementById('formError').innerHTML = "Please fill the necessory fields";          
            return false;
        }
    });
    
})