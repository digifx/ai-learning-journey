# 02 – How AI "thinks"

**Date started:** 2026-10-15
**Status:** 🚧 in progress
**Where:** the Claude app (claude.ai, desktop or mobile). No code needed.
**Time:** about 30–45 minutes

## Goal
Build an accurate gut feeling for how AI models behave: what they're good at,
where they fail, and why. These six experiments cover the ideas that explain
most of what you'll see AI do.

## The one idea behind everything
A model like Claude learned from a huge amount of text to predict **what text
should come next**. It doesn't look facts up in a database (unless it's given a
tool like web search), and it only "sees" what's in the current conversation.
Keep that in mind and most of the results below will make sense.

---

## Experiment 1: Wording changes the answer
Start a new chat and ask the same question three ways, in **three separate chats**:
1. `Why do leaves change color in autumn?`
2. `Explain why leaves change color in autumn to a 7-year-old, using one fun comparison.`
3. `In exactly one sentence, why do leaves change color in autumn?`

**Look for:** how the length, tone and detail change.
**The lesson:** AI does what you *describe*. Being specific about audience,
length and format is the most useful single skill (prompt engineering).

**My results:**

**Prompt 1 (plain question):** about 300 words, organized under bold headings
(green fades → yellows revealed → reds newly made → browns → leaf drops).
It explained the science (chlorophyll, carotenoids, anthocyanins, tannins), used
everyday comparisons (carrots, cranberries), and added extras I didn't ask for:
why weather affects how bright the colors are, and why trees drop leaves at all.
The facts check out.

*Observation:* with no instructions about audience or length, Claude chose a
thorough explainer for a curious adult. It filled in the blanks itself.

<details><summary>Full answer to prompt 1</summary>

> Leaves change color in autumn because the tree stops making chlorophyll, which unmasks pigments that were there all along and, in some species, triggers the production of new ones.
>
> **The green fades.** During spring and summer, leaves are packed with chlorophyll, the pigment that captures sunlight for photosynthesis. It's so abundant that it swamps every other color. As days shorten and nights cool in autumn, the tree begins shutting down this production. It pulls valuable nutrients, like nitrogen, back into the branches and trunk for storage over winter, and the chlorophyll breaks down.
>
> **Yellows and oranges are revealed.** Carotenoids, the same family of pigments that color carrots and corn, are present in the leaf all season. Once the chlorophyll is gone, they show through. This is why trees like birches, aspens, and hickories turn golden yellow.
>
> **Reds and purples are newly made.** Anthocyanins, the pigments behind the color of cranberries and red apples, are mostly produced in autumn, from sugars trapped in the leaf. Maples, sweetgums, and some oaks make a lot of them. Bright sunny days and cool (but not freezing) nights lead to more sugar production and trapping, which is why vivid reds tend to follow that kind of weather. A cloudy, warm autumn usually gives duller color.
>
> **Browns** come from tannins and other waste compounds left in the leaf, most noticeable in oaks.
>
> Finally, the tree seals off the leaf stem with a layer of cells (the abscission layer), and the leaf drops. Shedding leaves lets deciduous trees avoid losing water and risking frost damage when the ground is cold and the sun is weak.

</details>

**Prompt 2 (for a 7-year-old):** about 150 words, short sentences, a warm tone.
It kept the word "chlorophyll" but explained it as "green stuff", and dropped
tannins, the leaf falling off, and the weather details.
- ⚠️ **It broke a rule:** I asked for *one* fun comparison and got **two**
  (a "lunchbox factory" *and* a "green raincoat over a yellow sweater").
- ⚠️ **Simplifying cost some accuracy:** it ends with "the leaves aren't really
  changing color, they're just taking off their green coats". But one sentence
  earlier it said some leaves *make new red colors*, which is real change.
  The kid version contradicts itself slightly to sound neat.

<details><summary>Full answer to prompt 2</summary>

> Imagine a tree is like a big green lunchbox factory all summer long. Its leaves are full of a green stuff called chlorophyll, which catches sunshine and turns it into food for the tree.
>
> But the green is so bright and bossy that it hides the yellow and orange colors that were in the leaves the whole time. It's like wearing a bright green raincoat over a yellow and orange sweater.
>
> When autumn comes, the days get shorter and cooler, and the tree says, "Time to rest for winter!" It stops making the green stuff, and the green raincoat slowly fades away. Then the yellow and orange sweater underneath finally gets to show. Some leaves even make new red colors as they get ready to fall.
>
> So the leaves aren't really changing color. They're just taking off their green coats.

</details>

**Prompt 3 (one sentence):** exactly one sentence ✅, but a long one (about 45 words).
It squeezed in nearly all the key science, with technical terms in brackets.

> Leaves change color in autumn because shorter days and cooler temperatures cause trees to stop making green chlorophyll, revealing the yellow and orange pigments (carotenoids) that were there all along, while some trees also produce new red pigments (anthocyanins) from trapped sugars.

*Observation:* it followed my rule *literally* (one sentence) rather than in
spirit (short and simple). If I want short, I should say so: "under 20 words".

### Takeaways from experiment 1
1. **The same AI, the same facts, three very different answers**, all shaped by a
   few words of instruction. Audience and length matter most.
2. **With no instructions, the AI guesses.** Its default is thorough and adult-level.
3. **AI doesn't always follow instructions exactly.** It ignored "one comparison".
   Always check the output against what you asked for.
4. **Instructions get followed literally.** "One sentence" ≠ "short". Say what you actually mean.
5. **Simplifying can bend the truth.** The kid version traded a bit of accuracy for neatness.

## Experiment 2: Does it remember you?
1. In a new chat, say: `My favorite fruit is mango. Please remember that.`
2. Open a **different** new chat and ask: `What's my favorite fruit?`

**Look for:** does it know? If your memory setting is on, it might.
Ask it: `How do you know that?`
**The lesson:** the model itself remembers nothing between conversations. Each
reply is produced only from the text it's given. "Memory" is an app feature
that saves notes and adds them into new chats. (Settings → check whether memory is on.)

**My results:**

## Experiment 3: Will it make things up?
In a new chat, ask about a book that **doesn't exist**:
`Give me a short summary of the 1987 novel "The Glass Orchard" by Henry Malvern.`

Then try a sneakier version:
`What were the three main findings of the 2019 Stanford study on left-handed pianists?`

**Look for:** does it admit it doesn't know, or invent a confident answer?
**The lesson:** because AI predicts likely-sounding text, it can produce
convincing details that are false. This is called **hallucination**. Modern
models are much better at saying "I'm not sure", but never fully trust specific
facts, quotes, numbers or sources without checking.

**My results:**

## Experiment 4: What does it know about today?
1. With web search **off**, ask: `What are the top news stories this week?`
2. Turn web search **on** (the tools/search toggle near the message box) and ask again.

**Look for:** how the two answers differ, and whether the second one cites sources.
**The lesson:** a model's knowledge stops at its **training cutoff**. Tools like
web search let it fetch fresh information. That's your first look at AI using
*tools*, which becomes a big theme later.

**My results:**

## Experiment 5: Give it room to think
Ask this puzzle in a new chat:
`A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?`

Then try a harder one, with extended thinking switched on if your app offers it:
`I have 3 boxes. One has only apples, one only oranges, one both. All labels are wrong. I may take one fruit from one box. How do I relabel all boxes correctly?`

**Look for:** does it get them right (5 cents, and "pick from the box labelled *both*")?
If thinking is shown, read how it reasoned.
**The lesson:** letting a model work through a problem step by step before
answering makes it noticeably more accurate on tricky problems.

**My results:**

## Experiment 6: Roles and examples
In a new chat:
```
You are a strict but kind writing teacher. Give feedback on this sentence
in exactly this format:
Score: x/10
Good: ...
Fix: ...

Sentence: "me and him goes to the store yesterday and buyed alot of stuffs"
```
Then ask it to do the same for a sentence of your own.

**Look for:** does it follow the format exactly, every time?
**The lesson:** giving a **role** and an **example format** makes output
consistent and predictable. This is the basis of the custom instructions you'll
set up in Projects (project 04).

**My results:**

---

## What I learned
_(Fill in after the experiments, in your own words. Which result surprised you most?)_

## Questions this raised
