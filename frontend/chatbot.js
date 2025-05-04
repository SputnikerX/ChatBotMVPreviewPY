const ASSISTANT_ID = "asst_i2ivyEjwxcYQT2QFwuioPzKh";

async function sendMessage() {
  const input = document.getElementById("userInput").value;
  const responseDiv = document.getElementById("chatResponse");

  const res = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input, assistant_id: ASSISTANT_ID })
  });

  const data = await res.json();
  if (data.response) {
    responseDiv.innerText = data.response;
  } else {
    responseDiv.innerText = "Error: " + data.error;
  }
}
