/* usage in costumerwelcome.html */

function increaseQuantity(foodID){
    var value = parseInt(document.getElementById(foodID).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 100){
        value++;
        document.getElementById(foodID).value = value;
    }
}

function decreaseQuantity(foodID){
    var value = parseInt(document.getElementById(foodID).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 0){
        value--;
        document.getElementById(foodID).value = value;
    }
}
