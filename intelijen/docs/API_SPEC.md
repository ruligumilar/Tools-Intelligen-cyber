# INTELIJEN — API SPECIFICATION

## 1. API PRINCIPLE

Backend menggunakan REST API.

Base URL development:

http://127.0.0.1:8000

Semua API harus memiliki:

- HTTP method
- endpoint
- request schema
- response schema
- validation
- error handling
- HTTP status code

Frontend tidak boleh memanggil endpoint yang belum
didefinisikan dalam dokumen ini.

---

# 2. CURRENT API

Pada Phase 1, API yang wajib tersedia hanya:

GET /api/health

Tidak boleh membuat API lain sebelum phase berikutnya
didefinisikan.

---

# 3. HEALTH CHECK

## Endpoint

GET /api/health

## Purpose

Memastikan backend INTELIJEN berjalan dengan baik.

## Request

Tidak membutuhkan request body.

## Response

HTTP 200

```json
{
  "status": "ok",
  "application": "INTELIJEN",
  "version": "0.1.0"
}