/**
 * YONIF TP 807/MNM
 * Sistem Informasi Personel
 * Frontend Authentication
 */

document.addEventListener('DOMContentLoaded', () => {

    // ===============================
    // DOM ELEMENTS
    // ===============================

    const loginForm = document.getElementById('loginForm');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');

    const togglePasswordBtn =
        document.getElementById('togglePassword');

    const eyeIcon =
        document.getElementById('eyeIcon');

    const eyeOffIcon =
        document.getElementById('eyeOffIcon');

    const submitBtn =
        document.getElementById('submitBtn');

    const btnText =
        submitBtn.querySelector('.btn-text');

    const btnSpinner =
        submitBtn.querySelector('.btn-spinner');

    const formAlert =
        document.getElementById('formAlert');


    // ===============================
    // API CONFIGURATION
    // ===============================

    const API_BASE_URL = 'http://127.0.0.1:8000';


    // ===============================
    // SHOW / HIDE PASSWORD
    // ===============================

    togglePasswordBtn.addEventListener('click', () => {

        const isPassword =
            passwordInput.type === 'password';

        passwordInput.type =
            isPassword ? 'text' : 'password';

        if (isPassword) {

            eyeIcon.classList.add('hidden');
            eyeOffIcon.classList.remove('hidden');

            togglePasswordBtn.setAttribute(
                'aria-label',
                'Sembunyikan kata sandi'
            );

        } else {

            eyeIcon.classList.remove('hidden');
            eyeOffIcon.classList.add('hidden');

            togglePasswordBtn.setAttribute(
                'aria-label',
                'Tampilkan kata sandi'
            );
        }
    });


    // ===============================
    // ALERT
    // ===============================

    function showAlert(message, type = 'error') {

        formAlert.textContent = message;

        formAlert.className =
            `form-alert ${type}`;

        formAlert.classList.remove('hidden');
    }


    function hideAlert() {

        formAlert.textContent = '';

        formAlert.classList.add('hidden');
    }


    // ===============================
    // LOADING STATE
    // ===============================

    function setLoadingState(isLoading) {

        submitBtn.disabled = isLoading;

        if (isLoading) {

            btnText.classList.add('hidden');
            btnSpinner.classList.remove('hidden');

        } else {

            btnText.classList.remove('hidden');
            btnSpinner.classList.add('hidden');
        }
    }


    // ===============================
    // CLEAR ALERT
    // ===============================

    [
        usernameInput,
        passwordInput
    ].forEach(input => {

        input.addEventListener('input', () => {

            if (!formAlert.classList.contains('hidden')) {
                hideAlert();
            }

        });

    });


    // ===============================
    // LOGIN
    // ===============================

    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        hideAlert();

        const usernameVal = usernameInput.value.trim();
        const passwordVal = passwordInput.value;

        if (!usernameVal) {
            showAlert('Mohon masukkan Username Anda.');
            usernameInput.focus();
            return;
        }

        if (!passwordVal) {
            showAlert('Mohon masukkan Password Anda.');
            passwordInput.focus();
            return;
        }

        setLoadingState(true);

        try {
            const response = await fetch(
                `${API_BASE_URL}/api/auth/login?username=${encodeURIComponent(usernameVal)}&password=${encodeURIComponent(passwordVal)}`,
                {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json'
                    }
                }
            );

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Username atau password salah.');
            }

            const token = data.access_token;

            if (!token) {
                throw new Error('Token tidak diterima dari server.');
            }

            localStorage.setItem('access_token', token);

            showAlert('Login berhasil. Mengarahkan ke sistem...', 'success');

            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 800);

        } catch (error) {
            console.error('Login Error:', error);
            showAlert(error.message || 'Gagal terhubung ke server.', 'error');
        } finally {
            setLoadingState(false);
        }
    });

});