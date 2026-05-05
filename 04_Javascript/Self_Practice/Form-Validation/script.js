/*
 Project-Name:  Student Admission Portal (Mini)
*/ 
function store() {
    // 1. Data Retrieval
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let contact = document.getElementById('contact').value;

    // 2. Name Validation
    if (name == "") {
        alert("Bhai, Name likhna zaruri hai!");
        document.getElementById('name').focus();
        return false;
    }

    // 3. Age Validation
    if (age == "") {
        alert("Please enter your age");
        document.getElementById('age').focus();
        return false;
    }
    if (isNaN(age)) {
        alert("Age sirf number mein honi chahiye");
        document.getElementById('age').focus();
        return false;
    }
    if (age < 18 || age > 30) {
        alert("Age 18 se 30 ke beech honi chahiye");
        return false;
    }

    // 4. Contact Validation
    if (contact == "") {
        alert("Mobile number bharna zaruri hai");
        document.getElementById('contact').focus();
        return false;
    }
    if (isNaN(contact)) {
        alert("Contact sirf numbers mein likho");
        document.getElementById('contact').focus();
        return false;
    }
    if (contact.length != 10) {
        alert("Mobile number poore 10 digit ka hona chahiye");
        document.getElementById('contact').focus();
        return false;
    }

    // 5. Success: Display Card & Fill Data
    document.getElementById('result-card').style.display = "block";
    
    document.getElementById('res_name').textContent = name;
    document.getElementById('res_age').textContent = age;
    document.getElementById('res_contact').textContent = contact;

    // Form ko hide karne ke liye (Optional par professional lagta hai)
    // document.querySelector('.form-box').style.display = "none";

    return false; // Page refresh rokne ke liye
}