# Day 01 — ReAct Loop

What I built: A bare-bones ReAct agent loop in Python
How it works: Agent reasons about what to do, picks a tool, calls it, observes result, repeats
Key lesson: An agent is just an LLM in a while loop
What confused me: API quota limits on both OpenAI and Gemini free tiers
Solution: Used a mock LLM to simulate decisions while learning the loop structure