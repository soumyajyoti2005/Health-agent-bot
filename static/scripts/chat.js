const chatMessages = document.getElementById('chatMessages');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const typingIndicator = document.getElementById('typingIndicator');

// Add user message to chat
function addUserMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user-message';
    messageDiv.innerHTML = `
        <div class="message-avatar">👤</div>
        <div class="message-content">
            <p>${escapeHtml(message)}</p>
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Add bot message to chat
function addBotMessage(html) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    messageDiv.innerHTML = `
        <div class="message-avatar">🤖</div>
        <div class="message-content">
            ${html}
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Add error message to chat
function addErrorMessage(error) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';
    messageDiv.innerHTML = `
        <div class="message-avatar">⚠️</div>
        <div class="message-content error-message">
            <p><strong>Oops!</strong> ${escapeHtml(error)}</p>
            <p>Please try rephrasing your question or ask something else.</p>
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Show/hide typing indicator
function showTyping() {
    typingIndicator.style.display = 'flex';
    scrollToBottom();
}

function hideTyping() {
    typingIndicator.style.display = 'none';
}

// Scroll to bottom of chat
function scrollToBottom() {
    setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 100);
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Handle form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const message = userInput.value.trim();
    if (!message) return;
    
    // Add user message to chat
    addUserMessage(message);
    
    // Clear input
    userInput.value = '';
    
    // Show typing indicator
    showTyping();
    
    try {
        // Send message to backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        // Hide typing indicator
        hideTyping();
        
        if (data.success) {
            // Add bot response to chat
            addBotMessage(data.response);
        } else {
            // Show error message
            addErrorMessage(data.error || 'Something went wrong. Please try again.');
        }
        
    } catch (error) {
        hideTyping();
        addErrorMessage('Network error. Please check your connection and try again.');
        console.error('Error:', error);
    }
});

// Auto-resize textarea on input (optional enhancement)
userInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
});

// Focus input on load
window.addEventListener('load', () => {
    userInput.focus();
});