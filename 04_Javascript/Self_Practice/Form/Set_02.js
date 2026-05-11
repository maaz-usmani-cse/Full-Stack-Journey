// Jab page khule toh data dikhao
window.onload = showData;

function store() {
    // 1. Form se values uthana (Tumhari IDs ke hisaab se)
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let contact = document.getElementById('contact').value;
    let address = document.getElementById('Address').value;

    // 2. Database (LocalStorage) se purani list mangwana
    // Agar kuch nahi hai toh [] (khali array) mil jayegi
    let database = JSON.parse(localStorage.getItem('myDatabase')) || [];

    // 3. Naya data ek object mein pack karna
    let newUser = {
        n: name,
        a: age,
        c: contact,
        ad: address
    };

    // 4. Packet ko database (Array) mein push karna
    database.push(newUser);

    // 5. Wapas database mein save kar dena
    localStorage.setItem('myDatabase', JSON.stringify(database));

    // Form khali karne ke liye
    document.getElementById('name').value = "";
    document.getElementById('age').value = "";
    document.getElementById('contact').value = "";
    document.getElementById('Address').value = "";

    // Table update karne ke liye
    showData();

    return false; // Page refresh rokne ke liye
}

function showData() {
    let database = JSON.parse(localStorage.getItem('myDatabase')) || [];
    let table = document.getElementById('resultTable');

    table.innerHTML = "";

    // Loop chala kar ek-ek karke data dikhao
    database.forEach(function (item) {
        table.innerHTML += `
            <tr>
                <td>${item.n}</td>
                <td>${item.a}</td>
                <td>${item.c}</td>
                <td>${item.ad}</td>
            </tr>
        `;
    });
}