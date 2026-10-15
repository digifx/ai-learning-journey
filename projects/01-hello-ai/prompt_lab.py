"""
Step 3: Same question, different instructions. Compare the answers side by side.

Run:  python prompt_lab.py
      python prompt_lab.py "Why is the sky blue?"

What to notice:
  - HOW you ask changes WHAT you get: length, tone, structure, accuracy.
  - Edit the EXPERIMENTS list below to try your own ideas. This is "prompt engineering".
"""

import sys

import anthropic

MODEL = "claude-opus-5-5"

question = " ".join(sys.argv[1:]) or "Why do leaves change color in autumn?"

# Each experiment: (label, system prompt, effort level)
EXPERIMENTS = [
    ("Plain", "", "low"),
    ("For a 7-year-old", "Explain things so a 7-year-old would understand. Use one fun comparison.", "low"),
    ("One sentence", "Answer in exactly one sentence.", "low"),
    ("Expert, more effort", "You are a scientist. Be precise and mention the key chemistry.", "high"),
    ("Pirate", "Answer in the voice of a pirate, but keep the facts correct.", "low"),
]

client = anthropic.Anthropic()

print(f"Question: {question}\n")

for label, system, effort in EXPERIMENTS:
    request = dict(
        model=MODEL,
        max_tokens=16000,
        output_config={"effort": effort},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": question}],
    )
    if system:
        request["system"] = system

    response = client.beta.messages.create(**request)

    answer = "".join(block.text for block in response.content if block.type == "text")
    if response.stop_reason == "refusal":
        answer = "(declined)"

    print("=" * 70)
    print(f"{label}  |  effort={effort}  |  {response.usage.output_tokens} output tokens")
    print("=" * 70)
    print(answer, "\n")
