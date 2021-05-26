$(document).ready(function() {
    $("#btn-approve").click(function(e) {
        // if the leave balanace is not enough, then stop submitting the form

        var total_count_leave_bal = Number(document.getElementById('total_count_leave_bal').innerHTML);
        var apply_leave_days = Number(document.getElementById('id_leave_total_day').value);

        if (total_count_leave_bal - apply_leave_days < 0) {
            alert("Cant Approved! The leave balance is not enough!!!")
            e.preventDefault();
            console.log(typeof total_count_leave_bal)
            console.log(typeof apply_leave_days)
        }
    });
});
