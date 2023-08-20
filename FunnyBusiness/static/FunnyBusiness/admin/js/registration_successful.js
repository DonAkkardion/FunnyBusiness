

function copyBlockChainKey() {
  var copyText = document.getElementById("blockchainPrivateKey");

  if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
    // Use the Clipboard API for modern browsers
    navigator.clipboard.writeText(copyText.value)
      .then(function() {
        alert("Copied the private key: " + copyText.value);
      })
      .catch(function(error) {
        console.error("Failed to copy private key:", error);
      });
  } else {
    // Fallback for older browsers
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

    alert("Copied the private key: " + copyText.value);
  }
}
