// 1. Page load hote hi data dikhao
window.onload = () => {
    displayData();
};

// 2. CREATE & UPDATE (Save Data)
function saveData() {
    let name = document.getElementById('stdName').value;
    let age = document.getElementById('stdAge').value;
    let editIndex = document.getElementById('editIndex').value;

    if(name == "" || age == "") {
        alert("Bhai, khali mat chhodo!").
        return;
    }

    // Pehle se saved data nikalo ya khali array lo
    let students = JSON.parse(localStorage.getItem('students')) || [];

    if (editIndex === "") {
        // Naya data add karo (CREATE)
        students.push({ name: name, age: age });
    } else {
        // Purane data ko badlo (UPDATE)
        students[editIndex] = { name: name, age: age };
        document.getElementById('editIndex').value = ""; // Reset
        document.getElementById('mainBtn').innerText = "Add Student";
    }

    localStorage.setItem('students', JSON.stringify(students));
    
    // Inputs khali karo
    document.getElementById('stdName').value = "";
    document.getElementById('stdAge').value = "";

    displayData();
}

// 3. READ (Data Table mein dikhana)
function displayData() {
    let students = JSON.parse(localStorage.getItem('students')) || [];
    let html = "";

    students.forEach((element, index) => {
        html += `<tr>
            <td>${element.name}</td>
            <td>${element.age}</td>
            <td>
                <span class="edit-btn" onclick="editData(${index})">Edit</span>
                <span class="delete-btn" onclick="deleteData(${index})">Delete</span>
            </td>
        </tr>`;
    });

    document.getElementById('tableBody').innerHTML = html;
}

// 4. DELETE
function deleteData(index) {
    let students = JSON.parse(localStorage.getItem('students')) || [];
    students.splice(index, 1); // Array se us index ka data hatao
    localStorage.setItem('students', JSON.stringify(students));
    displayData();
}

// 5. EDIT (Sirf form mein wapas lane ke liye)
function editData(index) {
    let students = JSON.parse(localStorage.getItem('students')) || [];
    
    document.getElementById('stdName').value = students[index].name;
    document.getElementById('stdAge').value = students[index].age;
    document.getElementById('editIndex').value = index; // Index yaad rakho
    document.getElementById('mainBtn').innerText = "Update Student";
}