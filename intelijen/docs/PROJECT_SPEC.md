# INTELIJEN — PROJECT SPECIFICATION

## 1. PROJECT IDENTITY

Project Name:

INTELIJEN

Version:

0.1.0

Type:

OSINT & Public Information Analysis Platform

Development Status:

Foundation

---

# 2. PROJECT OBJECTIVE

INTELIJEN adalah aplikasi yang menerima input berupa kejadian,
topik, isu, atau pertanyaan dari pengguna kemudian mengumpulkan
informasi dari sumber publik dan mengubahnya menjadi informasi
terstruktur serta assessment.

Contoh input:

"Demonstrasi di Kota X"

Sistem kemudian melakukan:

USER QUERY
↓
SEARCH
↓
SOURCE COLLECTION
↓
DATA PROCESSING
↓
ENTITY EXTRACTION
↓
EVENT EXTRACTION
↓
LOCATION EXTRACTION
↓
TIMELINE
↓
ANALYSIS
↓
ASSESSMENT
↓
REPORT

---

# 3. CORE FEATURES

## 3.1 Event Search

Pengguna memasukkan:

- kejadian
- topik
- isu
- kata kunci
- lokasi

Contoh:

"Kebakaran di Kota X"

---

## 3.2 Source Collection

Sistem mengumpulkan informasi dari sumber publik.

Jenis sumber dapat mencakup:

- berita
- website publik
- dokumen publik
- sumber resmi
- sumber terbuka lainnya

Setiap source harus memiliki:

- title
- URL
- source name
- published date jika tersedia
- retrieved date
- content/reference

---

## 3.3 Information Processing

Informasi yang diperoleh diproses menjadi:

- text
- source
- date
- location
- entity
- event
- claim

---

# 4. ENTITY

Sistem dapat mengidentifikasi entitas seperti:

## Person

Tokoh publik atau individu yang relevan dengan kejadian.

## Organization

- pemerintah
- perusahaan
- organisasi
- institusi
- kelompok publik

## Location

- negara
- provinsi
- kota
- wilayah
- lokasi kejadian

---

# 5. EVENT

Event memiliki:

- event name
- description
- date
- location
- actors
- sources

---

# 6. ACTOR PROFILING

Sistem dapat membuat profil analitis terhadap aktor
yang relevan dengan suatu kejadian.

Informasi dapat mencakup:

- name
- type
- organization
- role jika tersedia
- public information
- related events
- related sources
- relationships

Profil harus berbasis informasi publik dan source evidence.

---

# 7. LOCATION ANALYSIS

Lokasi dapat ditampilkan pada map.

Data:

- latitude
- longitude
- location name
- event
- source

Map menggunakan:

Leaflet

---

# 8. TIMELINE

Sistem membuat timeline:

DATE
↓
EVENT
↓
SOURCE
↓
ACTOR
↓
DEVELOPMENT

Timeline harus dapat ditelusuri ke sumber.

---

# 9. SOURCE ANALYSIS

Sistem harus dapat menampilkan:

- jumlah sumber
- sumber berdasarkan jenis
- sumber berdasarkan waktu
- sumber berdasarkan topik
- sumber yang duplikat
- sumber yang saling bertentangan

---

# 10. INFORMATION CLASSIFICATION

Informasi dikategorikan menjadi:

FACT

CLAIM

OPINION

UNVERIFIED

CONTRADICTED

---

# 11. VIRALITY ANALYSIS

Sistem menghitung indikator perhatian publik berdasarkan
data yang tersedia.

Indikator dapat mencakup:

- mention volume
- growth
- velocity
- source diversity
- geographic spread jika tersedia

Output:

Virality Score

dan:

Virality Trend

Skor bukan indikator kebenaran.

---

# 12. IMPACT ANALYSIS

Analisis dampak dapat mencakup:

- security
- social
- economic
- political
- humanitarian
- environmental
- public attention

Output dapat berupa:

- score
- level
- explanation
- evidence

---

# 13. CONTRADICTION ANALYSIS

Sistem membandingkan informasi dari beberapa sumber.

Contoh:

SOURCE A

vs

SOURCE B

Sistem menampilkan:

- claim A
- claim B
- source A
- source B
- publication time
- differences
- confidence
- verification requirement

---

# 14. INFORMATION GAP

Sistem mengidentifikasi:

KNOWN

UNKNOWN

CONFLICTING

NEEDS VERIFICATION

Tujuannya membantu pengguna memahami informasi
yang masih kurang.

---

# 15. SCENARIO ANALYSIS

Sistem dapat menghasilkan beberapa kemungkinan
perkembangan berdasarkan evidence.

Contoh:

Scenario A
Scenario B
Scenario C

Setiap scenario harus memiliki:

- description
- indicators
- supporting evidence
- confidence

Scenario bukan kepastian.

---

# 16. RECOMMENDATION

Sistem memberikan rekomendasi analitis seperti:

1. Verify
2. Monitor
3. Collect missing information
4. Reassess

Rekomendasi harus dapat dijelaskan berdasarkan evidence.

---

# 17. DASHBOARD

Dashboard utama direncanakan memiliki:

## Header

INTELIJEN

## Search

Input:

"Masukkan kejadian atau topik..."

Button:

ANALYZE

---

## Summary

Menampilkan:

- Event
- Time
- Location
- Sources
- Actors
- Risk/Impact indicator

---

## Sources

Daftar sumber.

---

## Actors

Daftar aktor.

---

## Map

Lokasi kejadian.

---

## Timeline

Perkembangan kejadian.

---

## Relationship Graph

Hubungan antar entitas.

---

## Virality Chart

Grafik perhatian publik.

---

## Impact Chart

Grafik dampak.

---

## Assessment

Ringkasan analitis.

---

## Information Gaps

Informasi yang belum diketahui.

---

## Possible Developments

Kemungkinan perkembangan.

---

## Recommended Actions

Rekomendasi tindakan.

---

# 18. TECHNOLOGY STACK

## Backend

Python

FastAPI

SQLAlchemy

Pydantic

HTTPX

---

## Frontend

HTML

CSS

JavaScript

---

## Database

PostgreSQL

---

## AI

Ollama

Cloud AI Provider sebagai optional provider.

---

## Visualization

Leaflet

Chart.js

Cytoscape.js

---

## Testing

Pytest

---

## Version Control

Git

---

# 19. ARCHITECTURE

```text
USER
 │
 ▼
FRONTEND
 │
 ▼
FASTAPI
 │
 ├──────────────┐
 ▼              ▼
SEARCH       DATABASE
 │
 ▼
SOURCE COLLECTION
 │
 ▼
DATA PROCESSING
 │
 ├── Entity
 ├── Event
 ├── Location
 └── Claim
 │
 ▼
AI ANALYSIS
 │
 ▼
ANALYSIS ENGINE
 │
 ├── Virality
 ├── Impact
 ├── Contradiction
 ├── Information Gap
 └── Scenario
 │
 ▼
DASHBOARD
 │
 ▼
REPORT