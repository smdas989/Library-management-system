const search_table = document.querySelector('#search-results');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const tbody = document.querySelector('.table-body');
const noResult = document.querySelector('.no-result');
tableOutput.style.display = 'none';

$("#search_box").keyup(function(e) {
  var user_input=$(this).val();
  console.log(user_input)
  e.preventDefault();
  if (user_input.trim().length>0) {
    tbody.innerHTML = ""
    $.ajax({
      method:'GET',
      url: '/search_record/',
      data: { 
        user_input: user_input,
      },
      success: function(data) {
        console.log(data)
        appTable.style.display = 'none';
        tableOutput.style.display = 'block';
        
        if (data.length===0){
          noResult.innerHTML='No results found';
          noResult.style.display='block';
          tableOutput.style.display='none';
        }
        else{
          
          noResult.style.display='none';
          data.forEach((item)=>{
            tbody.innerHTML+=`
            <tr>
            <td><a href="/user_details/${ item.id }">${ item.username } </a></td>
            <td> ${ item.role } </td>
            <td> ${ item.book }</td>
            <td> ${ item.issue_date }</td>
            <td> ${ item.due_date }</td>
            <td> ${ item.return_date }</td>
          </tr>
            `
          });
        }
      },
  });

  }
  else{
    tableOutput.style.display = 'none';
    appTable.style.display = 'block';
    noResult.style.display='none';
  }
  });