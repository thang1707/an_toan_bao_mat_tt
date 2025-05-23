
// Mã hóa
    function encrypt() {
      const msg = document.getElementById("message").value;

      fetch("http://localhost:5000/encrypted", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("result").innerText = JSON.stringify(data.encrypted);
      });
    }

    // Giải mã
    function decrypt() {
      const encryptedMessage = document.getElementById("encryptedMessage").value;
      const encryptedData = JSON.parse(encryptedMessage);  // Chuyển chuỗi JSON thành đối tượng

      fetch("http://localhost:5000/decrypted", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ encrypted: encryptedData })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("decryptedResult").innerText = data.decrypted;
      })
      .catch(error => {
        document.getElementById("decryptedResult").innerText = "Lỗi khi giải mã!";
      });
    }