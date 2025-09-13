console.log("Hospital Management System JS loaded.");

// Placeholder for future interactive features

document.addEventListener('DOMContentLoaded', function() {
    // Example: Add a class to the body to indicate JS is enabled
    document.body.classList.add('js-enabled');

    // Example: AI Assistant interaction
    const aiInput = document.querySelector('.ai-assistant input');
    if (aiInput) {
        aiInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                const message = e.target.value;
                if (message) {
                    const messagesContainer = document.querySelector('.ai-assistant .messages');
                    const userMessage = document.createElement('p');
                    userMessage.innerHTML = `<strong>You:</strong> ${message}`;
                    messagesContainer.appendChild(userMessage);

                    // Placeholder for AI response
                    const aiResponse = document.createElement('p');
                    aiResponse.innerHTML = `<strong>AI:</strong> I am a placeholder AI. I received your message: "${message}"`;
                    messagesContainer.appendChild(aiResponse);

                    e.target.value = '';
                    messagesContainer.scrollTop = messagesContainer.scrollHeight;
                }
            }
        });
    }
});
