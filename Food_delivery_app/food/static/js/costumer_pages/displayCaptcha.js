// usage in userlogin.html

var canvas = document.getElementById("captchaCanvas");
var captchaValue = document.getElementById("captchaVar").value;
var ctx = canvas.getContext("2d");
ctx.font = "30px Comic Sans MS";
ctx.fillSytle = "red"
ctx.textAlign = "center"
ctx.fillText(captchaValue, canvas.width / 2, canvas.height / 2);
