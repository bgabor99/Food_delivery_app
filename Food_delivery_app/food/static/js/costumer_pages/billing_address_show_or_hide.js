//usage in costumerwelcome.html

function billing_address_show_or_hide() {
    var checkBox = document.getElementById("billCheckbox");
    var div = document.getElementById('billingAddressDiv');
    var city = document.getElementById('billingCity');
    var zip = document.getElementById('billingZip');
    var address = document.getElementById('billingAddress');
    var yesNoLabel = document.getElementById('billingCkbLabel');
    if (checkBox.checked) {
        // the a billing address is NOT the same as the delivery address, show its div and add required attributes for all inputs in it
        div.style.display = 'block';
        city.setAttribute('required', ''); //(name, value)
        zip.setAttribute('required', '');
        address.setAttribute('required', '');
        yesNoLabel.innerHTML = "Yes, it's different";
    } else {
        // the a billing address is the same as the delivery address, unshow its div and remove required attributes for all inputs in it
        div.style.display = 'none';
        city.removeAttribute('required');
        zip.removeAttribute('required');
        address.removeAttribute('required');
        city.value = null;
        zip.value = null;
        address.value = null;
        yesNoLabel.innerHTML = "No, it's the same";
    }
}
