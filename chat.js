let isProcessing = false;

function toggleChat() {
    const chatWidget = document.getElementById('chatWidget');
    chatWidget.style.display = chatWidget.style.display === 'none' || chatWidget.style.display === '' ? 'flex' : 'none';
    
    if (chatWidget.style.display === 'flex') {
        // Welcome message
        setTimeout(() => {
            addMessage("👋 Hello! Welcome to Burger Toons. How can I help you today?", false);
        }, 500);
    }
}

function addMessage(message, isUser) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    
    // Add typing animation for bot messages
    if (!isUser) {
        messageDiv.innerHTML = '<div class="typing-indicator">...</div>';
        chatMessages.appendChild(messageDiv);
        
        setTimeout(() => {
            messageDiv.textContent = message;
        }, 1000);
    } else {
        messageDiv.textContent = message;
        chatMessages.appendChild(messageDiv);
    }

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function handleKeyPress(event) {
    if (event.key === 'Enter' && !isProcessing) {
        const input = document.getElementById('chatInput');
        const message = input.value.trim();
        
        if (message) {
            isProcessing = true;
            input.value = '';
            input.disabled = true;
            
            addMessage(message, true);
            
            try {
                const response = await fetch('http://localhost:5000/chatbot', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                addMessage(data.response, false);
            } catch (error) {
                console.error('Error:', error);
                addMessage('Sorry, I encountered an error. Please try again later.', false);
            } finally {
                isProcessing = false;
                input.disabled = false;
                input.focus();
            }
        }
    }
}

// Add suggestions buttons
function addSuggestions() {
    const suggestions = ['Menu', 'Delivery', 'Contact Us', 'About Us'];
    const suggestionsDiv = document.createElement('div');
    suggestionsDiv.className = 'chat-suggestions';
    
    suggestions.forEach(suggestion => {
        const button = document.createElement('button');
        button.textContent = suggestion;
        button.onclick = () => {
            document.getElementById('chatInput').value = suggestion;
            handleKeyPress({ key: 'Enter' });
        };
        suggestionsDiv.appendChild(button);
    });
    
    document.querySelector('.chat-input-container').appendChild(suggestionsDiv);
}

// Initialize chat when page loads
window.onload = () => {
    addSuggestions();
};