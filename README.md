# GenAI Product Recommender & CommerceOS — AI-Led Product Discovery and Purchase

> **Branch**: `AI-Led-Product-Discovery-and-Purchase`  
> **Core Engine**: CommerceOS — Autonomous AI Commerce Agent & Google Universal Commerce Protocol (UCP v2026-04-08)  
> **Dataset**: 1,000 Product Apparel Dataset (`Dataset/CSV/Product_data.csv` & `Dataset/JSON/Product_large.json`)

---

## 🌟 Architecture & System Specification Mapping

CommerceOS on the `AI-Led-Product-Discovery-and-Purchase` branch fulfills all three System Requirement specifications in the repository:

### 1. SR-001: Advanced Intent Intelligence (`SR-001-User-Intent-Understanding.md`)
- **Natural Language Intent Extraction**: Parses shopper intents into structured commerce objects.
- **Constraint Handling**: Extracts budget limits (₹ and L/K patterns), audience/gender (`Men`, `Women`, `Kids`), brand preferences (`Lee`, `Wrangler`, `Puma`, `Flying Machine`, `Benetton`, `Scullers`, `Highlander`, `Myntra`), clothing category (`Sweatshirt`, `T-Shirt`, `Shirt`), size (`S`, `M`, `L`, `XL`, `XXL`), style (`Stripped`, `Checked`, `Printed`), and colors.
- **Confidence Scoring**: Calculates intent confidence dynamically before triggering candidate discovery.

### 2. SR-002: Agentic Product Discovery (`SR-002-Agentic-Product-Discovery.md`)
- **6D Candidate Ranking Engine**: Ranks products across 6 core dimensions:
  1. **Requirement Overlap (30%)**: Category, brand, color, style, and size match.
  2. **Budget Adherence (20%)**: Price relative to intent threshold.
  3. **Use-Case Suitability (20%)**: Occasion and preference alignment.
  4. **Stock Availability (10%)**: Multi-merchant real-time inventory verification (`NOVA`, `VeloMart`, `UrbanCart`).
  5. **Rating & Reviews (10%)**: Customer satisfaction weighting.
  6. **Delivery Speed (10%)**: Fulfillment timeframes.
- **Dataset Integration**: Operates over all 1,000 items in `Dataset/CSV/Product_data.csv`.

### 3. SR-003: Autonomous Checkout & Payment Orchestration (`SR-003-Autonomous-Checkout-Payment-Orchestration.md`)
- **Google Universal Commerce Protocol (UCP v2026-04-08)**:
  - `GET /.well-known/ucp`: Merchant capability discovery & negotiation profile.
  - `POST /ucp/v1/checkout-sessions`: Session creation, cart locking, tax/shipping computation.
  - `POST /ucp/v1/pay`: Tokenized Google Pay settlement & order confirmation generation.
- **Dual Smartphone Payment Simulator**: Live visual execution trace of buyer and merchant state synchronization.

---

## 📸 Interactive Web UI & UCP Laboratory

The single-page web application (`index.html`) includes:
- **Try It Live Chat Simulator**: AI agent intent parsing, candidate ranking, and transparent execution log.
- **Dual Mobile Checkout Simulator**: Real-time side-by-side transaction simulation.
- **Google UCP Explorer**: Live payload inspection for `/.well-known/ucp` and UCP checkout sessions.
- **Architecture Topology**: Diagram of AI Intent Engine, Candidate Ranking, and Merchant UCP endpoints.

---

## 🛠 Project Structure

```
GenAI-Product-Recommender/
├── index.html                   # Single-page Web UI application
├── catalog.json                 # 1,000 product apparel catalog from Dataset/CSV/Product_data.csv
├── convert_dataset.py           # Dataset converter script
├── build_part1_v2.py            # Builder Part 1: UI Shell & Design System
├── build_part2.py               # Builder Part 2: Curated Dataset Catalog & Merchants
├── build_part3.py               # Builder Part 3: Agent Intent Parser & 6D Ranking
├── build_part4_v2.py            # Builder Part 4: Dual Smartphone Simulator
├── build_part5_v2.py            # Builder Part 5: UCP Protocol Explorer & Navigation
├── Dataset/                     # Original CSV & JSON datasets
│   ├── CSV/Product_data.csv     # 1,000 Apparel Products (Sweatshirts, T-Shirts, Shirts)
│   └── JSON/Product_large.json
├── ucp_server/                  # Production Python FastAPI UCP Backend Server
│   ├── app/                     # FastAPI routes, schemas, models & database setup
│   ├── seed_data.py             # SQLite seeder using catalog.json
│   ├── test_ucp_api.py          # Automated Pytest / UCP integration suite
│   └── run_server.py            # Uvicorn launcher script
├── SR-001-User-Intent-Understanding.md
├── SR-002-Agentic-Product-Discovery.md
└── SR-003-Autonomous-Checkout-Payment-Orchestration.md
```

---

## 🚀 How to Run

### 1. Launch the Production Python UCP Server
```bash
cd ucp_server
pip install -r ../requirements.txt
python3 seed_data.py
python3 run_server.py
```
Verified Endpoints:
- `GET http://127.0.0.1:8000/.well-known/ucp`
- `POST http://127.0.0.1:8000/ucp/v1/checkout-sessions`
- `POST http://127.0.0.1:8000/ucp/v1/pay`

### 2. Run Automated UCP Protocol Integration Tests
```bash
cd ucp_server
python3 test_ucp_api.py
```

### 3. Open the Web Application
Simply open `index.html` in any web browser.

---

*Built for **GenAI Product Recommender — AI-Led Product Discovery and Purchase***
