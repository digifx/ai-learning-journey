# 01 – Hello, AI

**Date started:** 2026-10-15
**Status:** 🚧 in progress (code ready, waiting on first run)

## Goal
Talk to an AI model (Claude) from my own code, and understand the basics that sit
underneath every AI app: requests, tokens, cost, memory and prompts.

## The three steps

| Script | What it does | Big idea it teaches |
|--------|--------------|---------------------|
| `hello.py` | Asks one question, prints the answer and what it cost | An AI model is an API: text in, text out, paid per token |
| `chat.py` | A back-and-forth chat in the terminal | The model has no memory. The app resends the whole conversation each turn |
| `prompt_lab.py` | Asks the same question 5 different ways, side by side | How you ask changes what you get (prompt engineering) |

## How to run it

1. **Get an API key** at https://console.anthropic.com (Settings → API Keys).
   Add a few dollars of credit. Each script run costs a fraction of a cent.
2. **Install the library** (once):
   ```bash
   pip install -r requirements.txt
   ```
3. **Set your key** for this terminal session. Never paste it into code or commit it:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."      # Mac / Linux
   $env:ANTHROPIC_API_KEY="sk-ant-..."        # Windows PowerShell
   ```
4. **Run the steps in order:**
   ```bash
   python hello.py
   python hello.py "Explain black holes to a 10-year-old"
   python chat.py
   python prompt_lab.py "Why is the sky blue?"
   ```

## Things to try
- In `hello.py`, change `effort` from `"low"` to `"high"`. Do the answer and token count change?
- In `chat.py`, change the `SYSTEM` prompt to something silly ("You are a grumpy cat").
  Watch the input-token count grow each turn as the history gets longer.
- In `prompt_lab.py`, add your own experiments to the `EXPERIMENTS` list.
- Ask Claude something it can't know, like today's news. What happens?

## What worked

## What didn't

## What I learned

## Ideas for next time
