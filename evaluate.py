import json
import os
import time

def load_test_matrix():
    """Loads the JSON test matrix configuration."""
    matrix_path = os.path.join("config", "test_matrix.json")
    with open(matrix_path, "r") as f:
        return json.load(f)

def run_mock_agent(scenario_id):
    """
    Simulates your AI agent's execution.
    In production, this is where you call your LLM or live agent API.
    """
    print(f"   ↳ Invoking agent for scenario {scenario_id}...")
    
    # Simulating varying outcomes based on the test case ID
    if scenario_id == "TC-001":
        time.sleep(1.2)  # Simulate 1200ms latency
        return {
            "outcome": "safe_failure",
            "tool_calls_correct": True,
            "latency": 1200
        }
    elif scenario_id == "TC-002":
        time.sleep(2.8)  # Simulate 2800ms latency (Exceeds our 2500ms matrix threshold!)
        return {
            "outcome": "success",
            "tool_calls_correct": True,
            "latency": 2800
        }
    
    return {"outcome": "failed", "tool_calls_correct": False, "latency": 0}

def evaluate_agent():
    """Reads tests, runs them against the agent, and scores the metrics."""
    matrix = load_test_matrix()
    print(f"=== Starting Evaluation for Project: {matrix['project_name']} (v{matrix['matrix_version']}) ===\n")
    
    # Extract global thresholds from the matrix
    thresholds = {m['metric_name']: m['threshold'] for m in matrix['evaluation_metrics']}
    
    all_passed = True
    
    for scenario in matrix['test_scenarios']:
        print(f"Running Test [{scenario['id']}]: {scenario['description']}")
        
        # 1. Run the agent and get results (trajectory)
        result = run_mock_agent(scenario['id'])
        
        # 2. Evaluate against expectations
        test_failed_reasons = []
        
        # Check Outcome Expectation
        if result['outcome'] != scenario['expected_outcome']:
            test_failed_reasons.append(f"Expected outcome '{scenario['expected_outcome']}', got '{result['outcome']}'")
            
        # Check Latency Threshold (Max 2500ms allowed)
        if result['latency'] > thresholds['latency_per_turn']:
            test_failed_reasons.append(f"Latency {result['latency']}ms exceeded threshold of {thresholds['latency_per_turn']}ms")
            
        # 3. Print Results
        if not test_failed_reasons:
            print("✅ RESULT: PASSED\n")
        else:
            print("❌ RESULT: FAILED")
            for reason in test_failed_reasons:
                print(f"   - {reason}")
            print()
            all_passed = False
            
    print("=========================================")
    if all_passed:
        print("🎉 SUCCESS: All evaluation tests passed!")
    else:
        print("⚠️ ALERT: Evaluation failed on one or more metrics.")
    print("=========================================")

if __name__ == "__main__":
    evaluate_agent()
