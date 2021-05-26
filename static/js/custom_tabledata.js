$(document).ready(function(){
// Setup - add a text input to each footer cell
    $('#table_id thead tr').clone(true).appendTo('#table_id thead');

    $('#table_id thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Search '+title+'" />');
            $('input', this).on('keyup change', function() {
                if (table.column(i).search()!== this.value ){
                    table
                        .column(i)
                        .search( this.value )
                        .draw();
                }
            });
    });

    $('#table_id').DataTable({

    orderCellsTop: true,
    fixedHeader  : true,
    scrollX      : true,
    dom          : 'Bfstip',
    buttons      : {
                    name: 'primary',
                    buttons: ['copy', 'csv', 'excel','pdf']
                    }
    });
});

$(document).ready(function(){
// Setup - add a text input to each footer cell
$('#table_id2 thead tr').clone(true).appendTo('#table_id2 thead');
$('#table_id2 thead tr:eq(1) th').each( function (i) {
    var title = $(this).text();
    $(this).html('<input type="text" placeholder="Search '+title+'" />');
    $('input', this).on('keyup change', function() {
        if (table.column(i).search()!== this.value ){
            table
                .column(i)
                .search( this.value )
                .draw();
        }
    });
});

var table = $('#table_id2').DataTable({

    orderCellsTop: true,
    fixedHeader  : true,
    scrollX      : true,
    dom          : 'B<"clear">lfstip',
    buttons      : {
                    name: 'primary',
                    buttons: ['copy', 'csv', 'excel','pdf']
                    }
});
});

$(document).ready(function(){
// Setup - add a text input to each footer cell
$('#table_id3 thead tr').clone(true).appendTo('#table_id3 thead');
$('#table_id3 thead tr:eq(1) th').each( function (i) {
    var title = $(this).text();
    $(this).html('<input type="text" placeholder="Search '+title+'" />');
    $('input', this).on('keyup change', function() {
        if (table.column(i).search()!== this.value ){
            table
                .column(i)
                .search( this.value )
                .draw();
        }
    });
});

var table = $('#table_id3').DataTable({

    orderCellsTop: true,
    fixedHeader  : true,
    scrollX      : true,
    dom          : 'B<"clear">lfstip',
    buttons      : {
                    name: 'primary',
                    buttons: ['copy', 'csv', 'excel','pdf']
                    }
});
});
