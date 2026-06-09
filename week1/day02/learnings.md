# Day 02 — Tool Design

What I built: 4 tools — search_web, read_file, write_file, run_python
Key lesson: The tool description is what the LLM reads to decide which tool to use
Bad description = wrong tool picked
Test result: Agent correctly chose search_web first, then write_file to save summary.txt