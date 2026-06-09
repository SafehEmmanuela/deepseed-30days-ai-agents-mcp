import os
import json

# ──────────────────────────────────────────
# DAY 2: Define your tools as real functions
# ──────────────────────────────────────────

def search_web(query: str) -> str:
    return (
        f"Search results for '{query}':\n"
        f"Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. "
        f"It is known for its simple, readable syntax and is widely used in web development, "
        f"data science, artificial intelligence, and automation."
    )

def read_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{path}' not found."

def write_file(path: str, content: str) -> str:
    with open(path, "w") as f:
        f.write(content)
    return f"Successfully wrote to '{path}'."

def run_python(code: str) -> str:
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return str(exec_globals.get("result", "Code ran successfully."))
    except Exception as e:
        return f"Error running code: {str(e)}"

# Map tool names to actual functions
TOOLS_MAP = {
    "search_web": search_web,
    "read_file": read_file,
    "write_file": write_file,
    "run_python": run_python,
}

# ──────────────────────────────────────────
# MOCK LLM — simulates an AI making decisions
# This is what a real LLM would decide to do
# step by step to complete the task
# ──────────────────────────────────────────

def mock_llm_decide(step: int, last_tool_result: str) -> dict:
    """
    Simulates the LLM reasoning and deciding what to do next.
    Returns either a tool call or a final answer.
    """

    if step == 1:
        # Step 1: LLM reasons it needs to search first
        print("\n [LLM REASONING]: I need to search for Python programming info first.")
        return {
            "type": "tool_call",
            "tool": "search_web",
            "args": {"query": "Python programming language"}
        }

    elif step == 2:
        # Step 2: LLM got the search results, now saves them to a file
        print("\n [LLM REASONING]: I have the search results. Now I will save a summary to summary.txt.")
        summary = (
            "Python Programming — Summary\n"
            "==============================\n"
            f"{last_tool_result}\n\n"
            "Key uses: web development, data science, AI, automation.\n"
            "Why popular: simple syntax, large community, many libraries."
        )
        return {
            "type": "tool_call",
            "tool": "write_file",
            "args": {
                "path": "summary.txt",
                "content": summary
            }
        }

    else:
        # Step 3: Task is done, give final answer
        print("\n [LLM REASONING]: I have searched and saved the file. Task is complete.")
        return {
            "type": "final_answer",
            "text": (
                "Done! I searched for information about Python programming "
                "and saved a summary to 'summary.txt'. "
                "The file contains a description of Python, its history, and key uses."
            )
        }


# ──────────────────────────────────────────
# DAY 1: The ReAct loop
# ──────────────────────────────────────────

def run_agent(task: str):
    print(f"\n TASK: {task}")
    print("=" * 50)

    last_tool_result = ""
    step = 1

    while True:
        print(f"\n Step {step} — Agent is deciding what to do...")

        # Ask the mock LLM what to do next
        decision = mock_llm_decide(step, last_tool_result)

        if decision["type"] == "tool_call":
            tool_name = decision["tool"]
            tool_args = decision["args"]

            print(f" Agent chose tool  : {tool_name}")
            print(f" Arguments         : {tool_args}")

            # Call the actual function
            tool_function = TOOLS_MAP[tool_name]
            tool_result = tool_function(**tool_args)
            last_tool_result = tool_result

            print(f" Tool result       : {tool_result}")

        elif decision["type"] == "final_answer":
            print(f"\n FINAL ANSWER:")
            print(decision["text"])
            print("\n Task complete!")
            break

        step += 1
        if step > 10:
            print("Reached max steps, stopping.")
            break


# ──────────────────────────────────────────
# Run it
# ──────────────────────────────────────────

if __name__ == "__main__":
    run_agent("Search for information about Python programming and save a short summary to a file called summary.txt")