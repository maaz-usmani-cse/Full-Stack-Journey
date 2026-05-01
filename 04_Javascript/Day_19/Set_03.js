function calculateBMI() {
    let weight = document.getElementById('weight').value;
    let heightCm = document.getElementById('height').value;
    let heightM = heightCm / 100;


    let bmi = weight / (heightM * heightM);
    
    let finalBMI = bmi.toFixed(2);
    document.getElementById('res').textContent = 'Aapka BMI: ' + finalBMI;

    let message = "";
    if (bmi < 18.5) {
        message = "Underweight (Thoda sehat banaiye)";
    } else if (bmi >= 18.5 && bmi <= 24.9) {
        message = "Normal weight (Ek dum fit!)";
    } else {
        message = "Overweight (Thoda exercise shuru kijiye)";
    }
    
    document.getElementById('status').textContent = "Status: " + message;

    return false; 
}