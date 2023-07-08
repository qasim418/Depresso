document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the chatbox element
    var chatbox = document.getElementById('chatbox');
    
    // Retrieve the send button and input field elements
    var sendBtn = document.getElementById('sendBtn');
    var userInput = document.getElementById('userInput');
    
    // Add event listener to the send button
    sendBtn.addEventListener('click', function() {
      sendMessage();
    });
    
    // Add event listener to the input field for pressing Enter
    userInput.addEventListener('keypress', function(event) {
      if (event.which === 13) {
        sendMessage();
        event.preventDefault();
      }
    });
    
    // Function to send a message to the server
    function sendMessage() {
      var message = userInput.value.trim();
      if (message !== '') {
        // Add user's message to the chatbox
        appendMessage('user', message);
        
        // Clear the input field
        userInput.value = '';
        
        // Send the message to the server
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/chat', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
          if (xhr.status === 200) {
            // Add the bot's response to the chatbox
            appendMessage('bot', xhr.responseText);
          } else {
            // Handle error
            appendMessage('bot', 'Oops! Something went wrong.');
          }
        };
        xhr.send('message=' + encodeURIComponent(message));
      }
    }
    
    // Function to append a message to the chatbox
    function appendMessage(sender, message) {
      var messageElement = document.createElement('div');
      messageElement.classList.add('message', sender);
      messageElement.innerHTML = '<span>' + message + '</span>';
      chatbox.appendChild(messageElement);
      
      // Scroll to the bottom of the chatbox
      chatbox.scrollTop = chatbox.scrollHeight;
    }
  });
  