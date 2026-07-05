# Transpot AI

Edge AI Diagnostic Assistant for Mechanics — reconstructs vehicle failure progression instead of only reporting fault codes.

## What it does

Transpot AI takes vehicle telemetry (speed, brake temperature, brake pressure, RPM) and reconstructs the **story of a fault** — not just the fault code — so mechanics can see how a failure developed and what to inspect first.

## Demo

1. Select a demo vehicle or upload a telemetry CSV.
2. Click **Analyze Vehicle**.
3. View the failure progression event log, inspection recommendation, and confidence analysis.

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```
Transpot/
├── app.py              # Streamlit application
├── demo_vehicle.csv    # Sample telemetry data
├── requirements.txt
└── assets/             # Logo / static assets
```

## Status

Prototype built for SheBuilds Chennai Hack (Code & Challenge 3.0), aligned to SDG 12.
