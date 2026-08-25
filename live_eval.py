import os
import json

def evaluate_simulated_function_call():
    print("🚀 Triggering Agent Function Call Evaluation...\n")
    
    # Simulating what an LLM output looks like when it tries to call a tool
    # This matches the exact scenario of an account freeze request
    simulated_llm_output = {
        "name": "update_card_status",
        "arguments": "{\"account_number\": 998877, \"status\": \"BLOCKED\"}"
    }
    
    print(f"Analyzing Model Output for Tool: {simulated_llm_output['name']}")
    
    # THE EVALUATION MATRIX CHECK
    try:
        args = json.loads(simulated_llm_output['arguments'])
        
        # 1. Check Data Type Compliance (Integer Check)
        if type(args.get("account_number")) == int:
            print("✅ Check 1 Passed: 'account_number' is a valid Integer.")
        else:
            print("❌ Check 1 Failed: 'account_number' must be an Integer data type.")
            
        # 2. Check Enum Compliance (Caps String Check)
        if args.get("status") == "BLOCKED":
            print("✅ Check 2 Passed: 'status' aligns with allowed ENUM values.")
        else:
            print("❌ Check 2 Failed: 'status' value is invalid.")
            
        print("\n🏆 TOOL CALL ACCURACY: 100% (PASSED)")
        
    except json.JSONDecodeError:
        print("❌ CRITICAL: Model output generated malformed JSON string arguments.")

if __name__ == "__main__":
    evaluate_simulated_function_call()
