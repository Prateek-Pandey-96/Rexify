$(document).ready(function(){
$('#experienceIncrement').click(function(){
    var structure = $('#experienceCard').html();
    const companyName = $('#companyName').val();
    const companyDesination = $('#companyDesination').val();
    const startDate = $('#startDate').val();
    const endDate = $('#endDate').val();
    const project1Title = $('#project1Title').val();
    const project1Description = $('#project1Description').val();
    const project2Title = $('#project2Title').val();
    const project2Description = $('#project2Description').val();
    const button = '<input type="button" class="btn btn-sm btn-danger deleteItemExp" value="Remove">';
    $('#experienceDiv').append(
      '<div class="row addedRow"><div class="col-sm-4"><h5 class="namex">'+companyName+'</h5><h6 class="namex">'+companyDesination+'</h6>'+
      '<p class="namex">'+endDate+'<br/><p class="namex">'+startDate+'</p></div><div class="col-sm-8"><h6 class="namex">'+project1Title+'</h6><p><small class="namex">'+project1Description+'</small></p>'+
      '<h6 class="namex">'+project2Title+'</h6><p><small class="namex">'+project2Description+'</small></p><br/>'+button+'</div></div>');
    $('#experienceCard').empty();
    $('#experienceCard').append(structure);
  })
  
  $('#skillIncrement').click(function(){
    var structure = $('#skillCard').html();
    const skillName = $('#skillName').val();
    const proficiency = $('#myList').val();
    const button = '<input type="button" class="btn btn-sm btn-danger deleteItem" value="Remove">';
    $('.dynamic-body').append('<tr class="dynamicRow"><td class="attrName">'+skillName+'</td><td class="attrValue">'+proficiency+'</td><td>'+button+'</td></tr>');
    $('#skillCard').empty();
    $('#skillCard').append(structure);
  })
  $(document).on('click','input.deleteItemExp',function(){
    $(this).closest('div.row').remove();    
  })
  $(document).on('click','input.deleteItem',function(){
    $(this).closest('tr').remove();
  })
  $('#secondarySchoolName').on("input", function(){
      $("#secondarySchoolNameFiller").html($(this).val());
  })
  $('#secondaryPassingYear').on("input", function(){
      $("#secondaryPassingYearFiller").html($(this).val());
  })
  $('#secondaryCityName').on("input", function(){
      $('#secondaryCityNameFiller').html($(this).val());
  })
  $('#secondaryBranch').on("input", function(){
      $('#secondaryBranchFiller').html($(this).val());
  })
  $('#srsecondarySchoolName').on("input", function(){
      $("#srsecondarySchoolNameFiller").html($(this).val());
  })
  $('#srsecondaryPassingYear').on("input", function(){
      $("#srsecondaryPassingYearFiller").html($(this).val());
  })
  $('#srsecondaryCityName').on("input", function(){
      $('#srsecondaryCityNameFiller').html($(this).val());
  })
  $('#srsecondaryBranch').on("input", function(){
      $('#srsecondaryBranchFiller').html($(this).val());
  })
  $('#collegeName').on("input", function(){
      $("#collegeNameFiller").html($(this).val());
  })
  $('#collegePassingYear').on("input", function(){
      $("#collegePassingYearFiller").html($(this).val());
  })
  $('#collegeCity').on("input", function(){
      $('#collegeCityNameFiller').html($(this).val());
  })
  $('#collegeBranch').on("input", function(){
      $('#collegeBranchFiller').html($(this).val());
  })
  $('#saveBtnCheck').on('change',function(){
    if(document.getElementById('saveBtnCheck').checked == true)
      $("#saveBtn").attr('hidden',false);
    else
      $("#saveBtn").attr('hidden',true);
  })  
})