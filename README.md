🚨 Blockchain-Assisted DDoS Detection System

A production-style, flow-based DDoS detection and security logging system that combines Machine Learning for attack classification and Blockchain-inspired immutable logging for auditability and trust.

📌 Overview

Distributed Denial-of-Service (DDoS) attacks remain a critical threat to network availability. This project implements a cloud-deployable DDoS detection service using statistical network flow features and a trained Machine Learning model. Detected security incidents are recorded in a tamper-evident blockchain-style ledger, ensuring integrity and auditability of security decisions.

The system is designed following industry security and ML engineering practices, focusing on correctness, transparency, and deployability rather than unsafe traffic generation.

🧠 Key Features

Flow-based Machine Learning DDoS detection

RESTful API for real-time inference

Blockchain-style immutable security event ledger

Tamper detection and ledger verification

SOC-style monitoring dashboard

Clean separation of ML, API, logging, and UI layers

Ethical and lab-safe implementation

🏗️ System Architecture
User / Analyst
      ↓
Streamlit Dashboard
      ↓
FastAPI Inference Service
      ↓
ML Model (Random Forest)
      ↓
Blockchain-Inspired Security Ledger

🤖 Machine Learning Model

Model: Random Forest Classifier

Task: Binary Classification (Benign vs DDoS)

Dataset: CIC-DDoS2019 (Flow-based CSV features)

Training Size: ~225,000 network flows

Metrics:

Accuracy: ~99.9%

Precision/Recall/F1: Near-perfect

The model learns statistical traffic patterns rather than inspecting raw packets, making it scalable and privacy-preserving.

🔗 Blockchain-Assisted Logging

Blockchain is not used for traffic processing or detection.
Instead, it provides:

Immutable security event logging

Cryptographic hash chaining

Tamper detection via ledger verification

Audit-ready incident history

Each detected DDoS event is recorded as a block containing:

Timestamp

Detection result

Confidence score

Model metadata

Hash linkage to previous events

This mirrors how real SOC audit trails are designed.

📊 Dashboard Capabilities

Manual flow feature input for integration testing

Live prediction results with confidence

Security event ledger viewer

Ledger integrity verification status

Clear separation between detection and logging

🧪 API Endpoints
Endpoint	Description
/health	Service health check
/model	Model metadata and configuration
/predict	DDoS prediction endpoint
/ledger	View security event ledger
/ledger/verify	Verify ledger integrity

Swagger documentation is available at:

/docs

⚠️ What This Project Does NOT Do

The following are intentionally excluded:

Live packet capture

Real attack generation

Firewall or traffic blocking

Continuous network monitoring

These features are outside the scope of safe academic validation and are listed as future work.

🔐 Ethical & Security Considerations

No real traffic is intercepted or generated

No attack tools are implemented

No sensitive packet data is stored

Ledger stores decisions, not raw traffic

The system adheres to ethical cybersecurity research standards.

🚀 Deployment

The system is designed to be cloud-deployable:

Backend: FastAPI (Render / Railway)

Dashboard: Streamlit Cloud

Ledger: Local / cloud file-backed storage

Deployment instructions are included for reproducibility.

📈 Future Enhancements

Live flow ingestion using CICFlowMeter

Streaming pipelines (Kafka / Redis)

Alerting integrations (Email, Webhooks)

Role-based dashboard access

Enterprise blockchain backends

🧑‍💻 Author Note

This project demonstrates industry-aligned ML security engineering, emphasizing correctness, transparency, and trust rather than unsafe or unrealistic demonstrations.

📜 License

This project is intended for educational and research purposes.