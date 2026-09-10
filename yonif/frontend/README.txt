# Login YONIF TP 807/MNM

Halaman login responsif untuk PC dan HP.

## Struktur

```text
siber8_login_page/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── app.js
└── assets/
    └── yonif_logo.png
```

## Menjalankan

Paling mudah menggunakan VS Code Live Server atau server HTTP sederhana:

```bash
python -m http.server 5500
```

Kemudian buka:

```text
http://127.0.0.1:5500
```

## Integrasi FastAPI

Di `js/app.js`:

```javascript
const API_URL = "http://127.0.0.1:8001";
```

Pastikan endpoint login backend sesuai:

```text
POST /api/auth/login
```

Jika endpoint login Anda berbeda, ubah URL tersebut.

## Catatan keamanan

Token JWT disimpan di `localStorage` pada contoh ini agar mudah diuji. Untuk deployment produksi, pertimbangkan cookie `HttpOnly`, `Secure`, `SameSite`, HTTPS, dan proteksi CSRF sesuai arsitektur backend.
