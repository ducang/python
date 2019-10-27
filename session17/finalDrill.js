var songCont = document.getElementById('song_container');
// console.log(songCont);
var songs = songCont.getElementsByClassName('song');
// console.log(songs);
// for (var i = 0; i < songs.length; i++) {
//     var titles = songs[i].getElementsByClassName('title');
//     console.log(titles);
//     var artists = songs[i].getElementsByClassName('artist');
//     console.log(artists)
// };

function addDiv(){
    var div = document.createElement('div');
    div.className = 'song' ;
    var divId = prompt('Song Id')
    div.setAttribute('song_id', divId );
    var title = prompt('Title');
    var titleCreate = document.createElement('h4');
    titleCreate.className = 'title';
    titleCreate.textContent = title;
    div.appendChild(titleCreate);
    var artist = prompt('Song by');
    var artistCreate = document.createElement('h5');
    artistCreate.className = 'artist';
    artistCreate.textContent = artist;
    div.appendChild(artistCreate);
    var del = document.createElement('button');
    del.className = 'delete';
    del.textContent = 'Delete';
    del.addEventListener('click', (e) => {
        let d = e.target;
        let btnDel = d.parentNode;
        btnDel.remove()
    });
    var ed = document.createElement('button');
    ed.className = 'edit';
    ed.textContent = 'Edit';
    ed.addEventListener('click', (e) => {
        let tar = e.target;
        let pn = tar.parentNode;
        let id = pn.getAttribute('song_id');
        console.log(id)
    });
    var mor = document.createElement('button');
    mor.className = 'more';
    mor.textContent = 'More';
    mor.addEventListener('click', (e) => {
        let mo = e.target;
        let  pm = mo.parentNode;
        let tle = pm.getElementsByClassName('title')[0].textContent;
        let art = pm.getElementsByClassName('artist')[0].textContent;
        let sId = pm.getAttribute('song_id');
        console.log(title);
        console.log(artist);
        console.log(sId);
    });
    var hr = document.createElement('hr');
    div.appendChild(hr);
    div.appendChild(del);
    div.appendChild(ed);
    div.appendChild(mor);
    songCont.appendChild(div);
    
}

var deleteBtns = document.getElementsByClassName('delete');
for ( var j = 0; j < deleteBtns.length; j++) {
    var deleteBtn = deleteBtns[j];
    deleteBtn.addEventListener('click', function(e) {
        var d = e.target;
        var btnDel = d.parentNode;
        btnDel.remove();
    })
};

var editBtns = document.getElementsByClassName('edit');
for ( var k = 0; k < editBtns.length; k++ ) {
    var editBtn = editBtns[k];
    editBtn.addEventListener('click', function(e) {
        var edit = e.target;
        var p = edit.parentNode;
        var songId = p.getAttribute('song_id');
        console.log(songId);
    })
}    

var moreBtns = document.getElementsByClassName('more');
for ( var l = 0; l < moreBtns.length; l++) {
    var moreBtn = moreBtns[l];
    moreBtn.addEventListener('click', function(e) {
        var more = e.target;
        var m = more.parentNode;
        var title = m.getElementsByClassName('title')[0].textContent;
        var artist = m.getElementsByClassName('artist')[0].textContent;
        var songId = m.getAttribute('song_id');
        console.log(title);
        console.log(artist);
        console.log(songId);
    })
}


