function generateCard() {
    let name = document.getElementById('u_name').value;
    let job = document.getElementById('u_job').value;
    let contact = document.getElementById('u_contact').value;
    let email = document.getElementById('u_email').value;

   
    document.getElementById('card-box').style.display = "block";

    document.getElementById('display_name').textContent = name;
    document.getElementById('display_job').textContent = job;
    document.getElementById('display_contact').textContent = contact;
    document.getElementById('display_email').textContent = email;

    return false;
}


