# Rydum Backend

A FastAPI-based rhythm intelligence platform backend. Phase 1 focuses on generating MIDI drum beats.

## Project Structure

- **server/**: FastAPI Backend
- **client/**: Next.js Frontend

## Setup

1.  **Install Backend Dependencies**:
    ```bash
    cd server
    pip install -r requirements.txt
    ```

2.  **Install Frontend Dependencies**:
    ```bash
    cd client
    npm install
    ```

## Running the Project

### 1. Start Backend
```bash
cd server
python3 -m uvicorn app.main:app --reload
```
API: `http://127.0.0.1:8000`

### 2. Start Frontend
```bash
cd client
npm run dev
```
UI: `http://localhost:3000`

## Verification

To test the beat generation:

1.  Make sure the server is running.
2.  Run the verification script:
    ```bash
    cd server
    python3 verify.py
    ```
