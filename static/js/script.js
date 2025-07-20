document.addEventListener('DOMContentLoaded', function() {
    const generateForm = document.getElementById('generate-form');
    const intentSelect = document.getElementById('intent-select');
    const featuresDisplay = document.getElementById('features-display');
    const featuresDisplayBox = featuresDisplay.querySelector('.features-display-box');
    
    const eegInputBox = document.getElementById('eeg-input-box');
    const decodeButton = document.getElementById('decode-button');
    const resultsContainer = document.getElementById('results-container');

    const loader1 = document.getElementById('loader1');
    const loader2 = document.getElementById('loader2');

    generateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const selectedIntent = intentSelect.value;
        if (!selectedIntent) {
            alert("Please choose an intent from the dropdown.");
            return;
        }

        loader1.style.display = 'block';
        featuresDisplay.style.display = 'none';
        eegInputBox.value = '';
        decodeButton.disabled = true;
        resultsContainer.innerHTML = '';

        fetch('/generate_eeg', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ intent: selectedIntent }),
        })
        .then(response => response.json())
        .then(data => {
            loader1.style.display = 'none';
            if (data.success) {
                const featuresString = JSON.stringify(data.eeg_features);

                featuresDisplay.style.display = 'block';
                featuresDisplayBox.textContent = featuresString;

                eegInputBox.value = featuresString;

                decodeButton.disabled = false;
            } else {
                alert('Error generating EEG signals: ' + data.error);
            }
        })
        .catch(error => {
            loader1.style.display = 'none';
            console.error('Error:', error);
            alert('A network error occurred.');
        });
    });

    decodeButton.addEventListener('click', function() {
        const eegFeatures = eegInputBox.value;
        if (!eegFeatures) {
            alert("Please generate EEG signals first.");
            return;
        }

        loader2.style.display = 'block';
        resultsContainer.innerHTML = '';
        decodeButton.disabled = true; // Prevent multiple clicks

        fetch('/decode_process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ eeg_features: eegFeatures }),
        })
        .then(response => response.json())
        .then(data => {
            loader2.style.display = 'none';
            decodeButton.disabled = false; // Re-enable after processing
            if (data.success) {
                let resultsHTML = `
                    <div class="result-box">
                        <p><strong>Decoded Intent:</strong> ${data.decoded_intent}</p>
                    </div>
                    <div class="result-box">
                        <p><strong>Generated Sentence:</strong> ${data.generated_sentence}</p>
                    </div>
                `;
                if (data.audio_path) {
                    resultsHTML += `
                        <div class="result-box">
                            <p><strong>Audio Output 🔊:</strong></p>
                            <audio controls autoplay>
                                <source src="${data.audio_path}" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        </div>
                    `;
                }
                resultsContainer.innerHTML = resultsHTML;
            } else {
                alert('Error decoding intent: ' + data.error);
            }
        })
        .catch(error => {
            loader2.style.display = 'none';
            decodeButton.disabled = false;
            console.error('Error:', error);
            alert('A network error occurred.');
        });
    });

});
