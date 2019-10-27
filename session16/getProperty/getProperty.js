var box = document.getElementById('box');
console.log(box);

var width = box.clientWidth;
console.log('Box width: ' + width);

var height = box.clientHeight;
console.log('Box height: ' + height);

var text = box.textContent
console.log(text)

var boxx = document.getElementsByClassName('boxx')
for (var i = 0; i < boxx.length; i++) {
    console.log(boxx[i])
}