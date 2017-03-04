//structure of each item
//<li><input type= "checkbox"/><span>Finish code assessment</span> </li>
// function addNewItem(){
//     alert("TODO: Add new item");
// };
// var btnNew = document.getElementById("btnAdd");
// btnNew.onclick = addNewItem;

//User clicked on the add button
//If ther eis any text in the item field, add that text to the to do list

var removeImg = "<img src='remove-icon.png' />"
var completeImg = "<img src='complete.png' />"

document.getElementById('add').addEventListener('click',function(){
    var value = document.getElementById("item").value;
    if(value) addItemTodo(value);
    document.getElementById("item").value = '';
    

});

function removeItem(){
    var item = this.parentNode.parentNode;
    var parent = item.parentNode;
    parent.removeChild(item);

    console.log(this.parentNode);
}

function completeItem(){
    var item = this.parentNode.parentNode;
    var parent = item.parentNode;
    var id = parent.id;
    //check if the item should be added to completed or readded to todo
    var target = (id === 'todo') ? document.getElementById('completed'):document.getElementById('todo');
    parent.removeChild(item);
    target.insertBefore(item,target.childNodes[0]);
}

function addItemTodo(text){
    var list = document.getElementById('todo');

    var item = document.createElement('li');
    item.innerText = text;

    var buttons = document.createElement('div');
    buttons.classList.add('buttons');

    var remove = document.createElement('button');
    remove.classList.add('remove');
    remove.innerHTML = removeImg;

    remove.addEventListener('click',removeItem);

    var complete = document.createElement('button');
    complete.classList.add('add');
    complete.innerHTML = completeImg;

    complete.addEventListener('click',completeItem);

    buttons.appendChild(remove);
    buttons.appendChild(complete);
    item.appendChild(buttons);
    list.insertBefore(item,list.childNodes[0]);
}
