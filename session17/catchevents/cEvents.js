// function startClicking() {
//     console.log('Clicked');
// };

// var btnStart = document.getElementById('btn');
// cach 1
// btnStart.addEventListener('click', startClicking); 
// cach 2
// btnStart.addEventListener('click', function(e) {
//     console.log(e);
// });

// var searchBar = document.getElementById('searchBar');
// searchBar.addEventListener('change', function(e) {
//     console.log(e);
// });

var deleteBtns = document.getElementsByClassName('delete');
for ( var i = 0; i < deleteBtns.length; i++) {
    var deleteBtn = deleteBtns[i];
    deleteBtn.addEventListener('click', function(e) {
        var btn = e.target;
        var btnDel = btn.parentNode;
        btnDel.remove();
    })
}