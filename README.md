# Agent Evaluation Tracking Framework (`agent-eval-tracker`)

This framework is built to test, score, and benchmark AI agents, specifically optimizing for **LLM Agent Function Calling (Tool Use)** accuracy, pipeline resilience, and latency validation.

## 📊 Monitored Metrics
*   **Tool Call Accuracy:** Validates schema alignment, variable data type compliance (integers vs strings), enum path choices, and checks for argument hallucinations.
*   **Task Completion Resilience:** Audits trajectory loops to catch recursive processing errors during broken tool payloads.
*   **Turn Latency Tracking:** Measures real-world execution overhead against custom thresholds (e.g., 2500ms bounds).

## 📁 System Architecture
*   `config/test_matrix.json`: Contains the test vectors, metric thresholds, and target agent identities.
*   `evaluate.py`: The local testing engine that parses validation specifications.
*   `live_eval.py`: Function calling evaluator tracking payload formatting compliance.
