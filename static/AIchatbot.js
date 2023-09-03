const submit = document.getElementById("submit");
const input = document.getElementById("chat-input");
const messages = document.getElementById("chat-window");

submit.addEventListener("click", async (e) => {
  const message = input.value;
  input.value = "";

  messages.innerHTML += `<br><div class="message user-message">
    <p>User: <span>${message}</span>
  </div>`;

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    });

    if (!response.ok) {
      throw new Error("Request failed.");
    }

    const responseData = await response.json();
    const chatbotResponse = responseData.response;

    messages.innerHTML += `<div class="message bot-message">
      Bot: <span>${chatbotResponse}</span>
    </div>`;
  } catch (error) {
    console.error("Error sending message to the server:", error);
  }
});

const uploadInput = document.getElementById("upload-input");
        
uploadInput.addEventListener("change", async () => {
  const file = uploadInput.files[0];
  console.log(file);
  if (file) {
      const formData = new FormData();
      formData.append("image", file);
      try {
          const response = await fetch("/pest_detection", {
              method: "POST",
              body: formData, // Do not set the "Content-Type" header
          });

          if (response.ok) {
            const responseData = await response.json();
            
            const chatbotResponse = responseData.response;
            messages.innerHTML += `<div class="message bot-message">
              Bot: <span>${chatbotResponse}</span>
              </div>`;
          } else {
              console.error("Image upload failed.");
          }
      } catch (error) {
          console.error("Error uploading image:", error);
      }
  }
     
});