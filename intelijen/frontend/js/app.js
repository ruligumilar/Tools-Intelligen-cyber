const statusPanel = document.querySelector('.status-panel');
const statusText = document.getElementById('statusText');
const checkStatusBtn = document.getElementById('checkStatusBtn');
const result = document.getElementById('result');

const setState = (state, message = '') => {
  statusPanel.dataset.state = state;

  if (state === 'idle') {
    statusText.textContent = 'Idle';
  } else if (state === 'loading') {
    statusText.textContent = 'Checking...';
  } else if (state === 'success') {
    statusText.textContent = 'Healthy';
  } else if (state === 'error') {
    statusText.textContent = 'Unavailable';
  }

  if (message) {
    result.textContent = message;
  }
};

checkStatusBtn.addEventListener('click', async () => {
  setState('loading', 'Requesting health status...');
  checkStatusBtn.disabled = true;

  try {
    const response = await fetch('/api/health');

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();
    setState('success', JSON.stringify(data, null, 2));
  } catch (error) {
    console.error(error);
    setState('error', 'Failed to connect to backend health endpoint.');
  } finally {
    checkStatusBtn.disabled = false;
  }
});
