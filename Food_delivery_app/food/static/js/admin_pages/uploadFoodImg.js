// usage in adminhomepage.html

function click_english_pic_upload_label(input){
    document.getElementById('addImgInp').click();
}


function img_check(input) {
    var typ = document.getElementById("addImgInp").value;
    var res = (typ.match(".jpg") || typ.match(".png"));

    const fileSize = input.files[0].size / 1024; // in kB
    //.jpg check
    if (res) {
      //size check (above 200 kB)
      if (fileSize < 200) {
        document.getElementById('addImgBtn').innerHTML = 'Picture added';
        alert("Image sucessfully uploaded.");
      }
      else {
        alert("File size exceeds 200 kB!");
        document.getElementById("addImgInp").value = ''; //clear the uploaded file
      }
    }
    else {
      alert("Only .jpeg or .png images are accepted!");
      document.getElementById("addImgInp").value = ''; //clear the uploaded file
    }

}
