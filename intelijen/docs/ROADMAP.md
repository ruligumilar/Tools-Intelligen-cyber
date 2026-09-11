# INTELIJEN — DEVELOPMENT ROADMAP

## PROJECT VERSION

Current Version: 0.1.0

Target Version: 1.0.0

---

# DEVELOPMENT RULE

Project dikembangkan secara bertahap.

Setiap phase harus:

PLAN
↓
IMPLEMENT
↓
TEST
↓
DEBUG
↓
VERIFY
↓
COMMIT

Tidak boleh melanjutkan phase berikutnya jika phase
sebelumnya belum berhasil.

---

# PHASE 0 — DOCUMENTATION

Status:

COMPLETED

Files:

- MASTER_PROMPT.md
- PROJECT_SPEC.md
- ROADMAP.md

---

# PHASE 1 — FOUNDATION

Status:

NEXT

Tujuan:

Membuat struktur dasar aplikasi.

Target:

- Backend FastAPI
- Frontend HTML/CSS/JavaScript
- Health check API
- Basic project configuration
- Testing framework
- Environment configuration

Acceptance Criteria:

- Backend dapat berjalan.
- Frontend dapat dibuka.
- /api/health tersedia.
- Test berjalan.
- Tidak ada API key hardcoded.

---

# PHASE 2 — DATABASE

Status:

PLANNED

Tujuan:

Membuat sistem penyimpanan data.

Target:

- PostgreSQL
- SQLAlchemy
- Database configuration
- Models
- Migration
- Repository layer

Model awal:

- Case
- Source
- Document
- Entity
- Event
- Location
- Claim
- Relationship
- Analysis

Acceptance Criteria:

- Database dapat terkoneksi.
- Table dapat dibuat.
- Data dapat disimpan.
- Data dapat dibaca.
- Test database tersedia.

---

# PHASE 3 — SEARCH ENGINE

Status:

PLANNED

Tujuan:

Mengambil informasi dari sumber publik.

Target:

- Search provider interface
- Search API
- Search result schema
- Provider implementation
- Error handling
- Timeout handling
- Rate limit handling
- Result normalization

Output minimal:

- title
- URL
- source
- published date
- description

Acceptance Criteria:

- User dapat memasukkan query.
- Search berjalan.
- Hasil dapat ditampilkan.
- Hasil dapat disimpan.
- Error provider ditangani.

---

# PHASE 4 — SOURCE PROCESSING

Status:

PLANNED

Tujuan:

Memproses sumber yang ditemukan.

Pipeline:

SEARCH RESULT
↓
FETCH
↓
TEXT EXTRACTION
↓
CLEANING
↓
NORMALIZATION
↓
DEDUPLICATION
↓
DATABASE

Target:

- HTTP client
- Content extraction
- Text cleaning
- Duplicate detection
- Source metadata

Acceptance Criteria:

- Source dapat diproses.
- Duplicate dapat dideteksi.
- Source tetap memiliki URL.
- Error fetching ditangani.

---

# PHASE 5 — ENTITY & EVENT EXTRACTION

Status:

PLANNED

Tujuan:

Mengubah informasi menjadi data terstruktur.

Entity:

- Person
- Organization
- Location

Event:

- event name
- date
- location
- actors
- description
- sources

Claim:

- statement
- source
- date
- classification

Acceptance Criteria:

- Entity dapat diekstrak.
- Event dapat diekstrak.
- Location dapat diekstrak.
- Semua hasil dapat dikaitkan dengan source.

---

# PHASE 6 — AI ENGINE

Status:

PLANNED

Tujuan:

Menambahkan AI analysis.

AI Provider:

- Ollama
- Optional cloud provider

Fungsi:

- summarization
- entity extraction
- event extraction
- claim classification
- narrative analysis
- contradiction analysis
- assessment

Arsitektur:

AIProvider
├── OllamaProvider
└── CloudAIProvider

Acceptance Criteria:

- AI provider dapat diganti.
- Prompt terstruktur.
- Output tervalidasi.
- AI tidak mengarang source.
- AI tidak mengarang URL.
- AI tidak mengubah claim menjadi fact.

---

# PHASE 7 — VISUALIZATION

Status:

PLANNED

Tujuan:

Menyajikan hasil secara visual.

Components:

- Map
- Timeline
- Graph
- Charts

Technology:

Leaflet
Chart.js
Cytoscape.js

Output:

- event map
- actor graph
- event timeline
- source trend
- virality chart
- impact chart

Acceptance Criteria:

- Data backend dapat ditampilkan.
- Map dapat menampilkan lokasi.
- Graph dapat menampilkan hubungan.
- Chart menggunakan data aktual.

---

# PHASE 8 — INTELLIGENCE ANALYSIS

Status:

PLANNED

Tujuan:

Membuat analytical assessment.

Components:

## Virality

- mention volume
- growth
- velocity
- source diversity
- geographic spread

## Impact

- security
- social
- economic
- political
- humanitarian
- environmental
- public attention

## Contradiction

- conflicting claims
- source comparison
- evidence

## Information Gap

- known
- unknown
- conflicting
- needs verification

## Scenario

- possible development
- indicators
- supporting evidence
- confidence

Acceptance Criteria:

- Analysis memiliki dasar data.
- Score memiliki metodologi.
- Uncertainty ditampilkan.
- Assessment dapat ditelusuri ke evidence.

---

# PHASE 9 — REPORT GENERATOR

Status:

PLANNED

Output:

- HTML Report
- PDF Report

Struktur:

1. Executive Summary
2. Event Overview
3. Sources
4. Timeline
5. Actors
6. Locations
7. Relationships
8. Virality
9. Impact
10. Facts
11. Claims
12. Contradictions
13. Information Gaps
14. Possible Developments
15. Assessment
16. Recommended Actions
17. Sources

Acceptance Criteria:

- Report dapat dibuat.
- Source reference tersedia.
- Tidak ada data fiktif.
- Format dapat dibaca.

---

# PHASE 10 — SECURITY

Status:

PLANNED

Target:

- authentication
- authorization
- input validation
- rate limiting
- secure session
- secret management
- SQL injection protection
- XSS protection
- CSRF protection
- audit logging
- secure error handling

Acceptance Criteria:

- Secret tidak muncul di frontend.
- Secret tidak masuk Git.
- Input tervalidasi.
- Error tidak membocorkan informasi sensitif.

---

# PHASE 11 — TESTING & OPTIMIZATION

Status:

PLANNED

Testing:

- Unit Test
- Integration Test
- API Test
- Database Test
- Frontend Test
- End-to-End Test

Performance:

- async processing
- caching
- batching
- deduplication
- background processing

Acceptance Criteria:

- Test suite berjalan.
- Tidak ada critical error.
- Performance dapat diterima.

---

# PHASE 12 — DEPLOYMENT

Status:

PLANNED

Target:

- Linux server
- Docker
- PostgreSQL
- Nginx
- HTTPS
- Environment configuration
- Backup
- Monitoring
- Logging

Architecture:

Internet
↓
Nginx
↓
Frontend / API
↓
Application
↓
PostgreSQL
↓
AI

Acceptance Criteria:

- Application dapat dijalankan di server.
- HTTPS aktif.
- Database aman.
- Backup tersedia.
- Logging tersedia.

---

# VERSION MILESTONES

## v0.1

Foundation

## v0.2

Database

## v0.3

Search

## v0.4

Source Processing

## v0.5

Entity & Event

## v0.6

AI Engine

## v0.7

Visualization

## v0.8

Intelligence Analysis

## v0.9

Report Generator

## v0.95

Security & Testing

## v1.0

Production-ready MVP

---

# CURRENT POSITION

Current Phase:

PHASE 1 — FOUNDATION

Next Task:

Build FastAPI foundation and frontend foundation.

DO NOT implement:

- Search
- AI
- Database
- Map
- Graph
- Intelligence Analysis

until the current phase is verified.