
function store() {
    let name = document.getElementById('name').value;
    let box = document.getElementById('box');
    let result = document.getElementById('result');

  
    box.style.display = "block";
      result.textContent = name;
    return false;
}



