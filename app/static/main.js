document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const tercetText = document.getElementById('tercet-text');
    const generationMethod = document.getElementById('generation-method');
    const tercetHistory = document.getElementById('tercet-history');

    generateBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    method: generationMethod.value
                })
            });

            const data = await response.json();
            
            if (data.error) {
                tercetText.textContent = `Error: ${data.error}`;
                return;
            }

            // Update current tercet display
            tercetText.textContent = data.tercet;

            // Add to history
            const historyItem = document.createElement('div');
            historyItem.className = 'history-item';
            historyItem.textContent = data.tercet;
            tercetHistory.insertBefore(historyItem, tercetHistory.firstChild);

        } catch (error) {
            tercetText.textContent = `Error: Could not connect to the server. Make sure the Flask server is running.`;
        }
    });
});
