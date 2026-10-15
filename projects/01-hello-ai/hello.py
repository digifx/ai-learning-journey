"""
Step 1: Ask Claude one question and print the answer.

Run:  python hello.py
      python hello.py "Explain black holes to a 10-year-old"

What to notice:
  - An AI model is just an API: you send text, you get text back.
  - Every call is measured in "tokens" (roughly 3/4 of a word), and you pay per token.
"""

import sys

import anthropic

MODEL = "claude-opus-5-5"

# Prices in US dollars per 1 million tokens for this model (input, output).
PRICE_IN, PRICE_OUT = 4.00, 20.00

question = " ".join(sys.argv[1:]) or "In two sentences, what is a large language model?"

# The client reads your key from the ANTHROPIC_API_KEY environment variable.
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model=MODEL,
    max_tokens=16000,
    # "effort" controls how hard the model thinks before answering: low, medium, high, xhigh, max.
    output_config={"effort": "low"},
    # If Claude's safety checks decline a request, let the API retry it on a suitable model.
    betas=["server-side-fallback-2026-07-01"],
    fallbacks="default",
    messages=[{"role": "user", "content": question}],
)

if response.stop_reason == "refusal":
    print("Claude declined to answer this one.")
    sys.exit(1)

print(f"You asked: {question}\n")

# The answer comes back as a list of "content blocks". We only want the text ones.
for block in response.content:
    if block.type == "text":
        print(block.text)

usage = response.usage
cost = usage.input_tokens / 1e6 * PRICE_IN + usage.output_tokens / 1e6 * PRICE_OUT
print(f"\n--- {usage.input_tokens} tokens in, {usage.output_tokens} tokens out, about ${cost:.4f} ---")
