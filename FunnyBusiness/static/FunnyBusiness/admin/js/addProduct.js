// const { data } = require("jquery")
const input = document.getElementById('id_img');
const confirmBtn = document.getElementById('confirm-btn');
const imageBox = document.getElementById('image-box');
const hiddenElement = document.getElementById('hidden-element');
let isCropped = false; // Track whether the image has been cropped

input.addEventListener('change', () => {
  console.log('changed');
  hiddenElement.className ="text-center mb-2 visible"
  const img_data = input.files[0];
  const url = URL.createObjectURL(img_data);
  imageBox.src = url;

  const cropper = new Cropper(imageBox, {
    aspectRatio: 9 / 9,
    viewMode: 0,
  });

  confirmBtn.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent form submission
    const croppedImageDataURL = cropper.getCroppedCanvas().toDataURL("image/png");
    imageBox.src = croppedImageDataURL;
    isCropped = true; // Set the isCropped flag to true

    // Convert data URL to Blob
    const blob = dataURLtoBlob(croppedImageDataURL);

    // Create a new File object
    
    let now = new Date();
    let formattedDate = '' + now.getFullYear() 
    + padZero(now.getMonth() + 1) 
    + padZero(now.getDate()) 
    + padZero(now.getHours()) 
    + padZero(now.getMinutes()) 
    + padZero(now.getSeconds()) 
    + padZero(now.getMilliseconds(), 3);

    function padZero(num, size=2) {
      let s = String(num);
      while (s.length < (size || 2)) {s = "0" + s;}
      return s;
    }

    const croppedImageFile = new File([blob], formattedDate+'.png', { type: 'image/png' });

    // Create a new DataTransfer object
    const dataTransfer = new DataTransfer();

    // Add the cropped image file to the data transfer object
    dataTransfer.items.add(croppedImageFile);

    // Assign the files from the data transfer object to the file input
    input.files = dataTransfer.files;
  });
});

// Helper function to convert data URL to Blob object
function dataURLtoBlob(dataURL) {
  const arr = dataURL.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], { type: mime });
}

