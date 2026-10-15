"""
Step 2: Have a back-and-forth conversation with Claude in your terminal.

Run:  python chat.py      (type 'quit' to exit)

What to notice:
  - The model has no memory between calls. To "remember" the conversation,
    we keep a list of every message and send the WHOLE list each time.
  - That's why long chats cost more: the input grows with every turn.
  - The "system" prompt sets Claude's role and style for the whole chat.
    Try changing it and see how the personality changes.
"""

import anthropic

MODEL = "claude-opus-5-5"
SYSTEM = "You are a friendly tutor helping a beginner learn about AI. Keep answers short and concrete."

client = anthropic.Anthropic()
history = []  # every message so far, from both sides

print("Chat with Claude. Type 'quit' to exit.\n")

while True:
    user_text = input("You: ").strip()
    if user_text.lower() in {"quit", "exit"}:
        break
    if not user_text:
        continue

    history.append({"role": "user", "content": user_text})

    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM,
        output_config={"effort": "low"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=history,
    )

    if response.stop_reason == "refusal":
        print("\nClaude: (declined to answer that)\n")
        history.pop()  # drop the declined question so the chat can carry on
        continue

    # Save Claude's full reply into the history so the next call includes it.
    history.append({"role": "assistant", "content": response.content})

    reply = "".join(block.text for block in response.content if block.type == "text")
    print(f"\nClaude: {reply}")
    print(f"        [this turn sent {response.usage.input_tokens} input tokens]\n")
