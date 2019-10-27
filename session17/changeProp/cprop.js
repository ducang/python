var menuUl = document.getElementById('menu');
// var liList = document.createElement('li');
// liList.textContent = "Fries";
// menuUl.appendChild(liList);
var firstLi = menuUl.getElementsByTagName('li');
var removeLi = firstLi[0];
removeLi.remove();