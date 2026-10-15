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

*My guess beforehand:* it would remember, because I'd turned on memory in Settings. ✅ Correct.

1. Chat A: "Got it, Kevin: mango is your favourite fruit."
2. Chat B, asked "What's my favorite fruit?": "Mango."
3. Asked "How do you know that?":
   > Because it's saved in your memory: you've told me before that mango is your favourite fruit. That memory carries across conversations, which is how I could answer straight away without asking.
   >
   > If you'd rather I not keep that kind of detail, you can turn off "Generate memory from chats" in Settings, and I can also forget specific things if you ask.

*Observations:*
- It called me **Kevin** in chat A, though I never typed my name there. The app
  gives it details from my account and memory as well as what I type.
- It was open about *how* it knew, and told me how to switch the feature off.

### Takeaways from experiment 2
1. **The AI model has no memory of its own.** Every reply is produced only from
   the text it is given at that moment.
2. **"Memory" is an app feature built around the model.** The app saves short notes
   about me and quietly adds them to the start of new chats. The model reads them
   like any other text, so it *seems* to remember.
3. **That's the same trick as `chat.py` in project 01**, where the program resends the
   whole history each turn. Memory is a smarter version: it resends a summary.
4. **I control it.** It's in Settings, and I can ask Claude to forget specific things. memory is **on** for my account, so it remembered.

| Step | Claude's reply |
|------|----------------|
| Chat A: "My favorite fruit is mango…" | "Got it, Kevin: mango is your favourite fruit." |
| Chat B: "What's my favorite fruit?" | "Mango." |
| Chat B: "How do you know that?" | "Because it's saved in your memory… That memory carries across conversations." It also pointed to the **"Generate memory from chats"** setting to turn this off, and offered to forget specific things. |

*Observations:*
- It knew my **name** in chat A without being told. That comes from my account, which
  the app quietly includes in the conversation.
- It was open about *why* it knew: memory, not some magic recall.

### Takeaways from experiment 2
1. **The model itself is still stateless.** Behind the scenes, the app saves notes
   ("favourite fruit: mango") and *adds them to the text of each new chat*. The model
   just reads them, the same way `chat.py` in project 01 resends the history.
2. **Apps add hidden context.** My name, my memories and app instructions are all put
   in front of my message before Claude sees it. That's why it "knows" things about me.
3. **I'm in control.** I can view and edit memory, or turn it off, in Settings.
   Worth knowing before sharing anything private in a chat.

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

**Prompt 1 (fake novel):** ✅ it did **not** make anything up.
> I couldn't find any record of a 1987 novel called "The Glass Orchard" by Henry Malvern. It doesn't appear in my own knowledge, and my search turned up only unrelated books with similar titles or names, such as *The Glass Demon* by Helen Grant and *The Orchard* by Charles L. Grant. I'd rather not invent a plot for it.
>
> The book may be very obscure, out of print, or listed under a different title or author name. If you can tell me where you came across it (a publisher, ISBN, or a library listing), I can look again. If you have the book or a blurb to hand, I can summarize that. If you're after something similar in feel, I can suggest real novels with orchard or glass imagery.

*Observations:*
- It **searched the web** before answering ("my search turned up..."), so it
  checked rather than relying on memory alone. Web search must have been on.
- It said plainly that it wouldn't invent a plot, and offered honest next steps.
- The similar books it named are real ones I could look up myself, which is the
  right habit: when AI names a source, check it.

**Prompt 2 (fake Stanford study):**

*My guess beforehand:* it wouldn't hallucinate. ✅ Correct, but I couldn't verify
the extra details it gave me, so I asked Claude Code to check them.

> I couldn't find a 2019 Stanford study on left-handed pianists, so I can't give you its three main findings. I'd rather not guess at them.
>
> The closest match is a 2018 paper in PLoS ONE by Eline Smit and Makiko Sadakata, "The effect of handedness on spatial and motor representation of pitch patterns in pianists." It doesn't appear to come from Stanford. [...] Left-handed pianists tended to be quicker and more accurate when reversing their fingering in left-hand performances. This was only a trend [...]
>
> A 2019 study by Kilincer et al. on hand use in pianists is cited in the wider literature, though it concerns pianists generally rather than left-handers. [...]

It didn't accept the false premise. It offered the closest real study and
was clear it wasn't from Stanford.

**Fact-check of the extra details:**

| Claim | Verdict |
|-------|---------|
| Smit & Sadakata 2018, PLoS ONE, title as given | ✅ **Confirmed**: PLoS ONE 13(5), [open-access paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5931456/). Authors are at the University of Amsterdam, not Stanford, as Claude said. |
| Study design (practice melodies, then reversed contours and reversed keyboard) | ✅ Matches the paper's abstract |
| Findings, including "only a trend" for left-handers | ✅ Matches, including the caution |
| "2019 study by Kilincer et al." | ⚠️ **Unconfirmed.** There is a [Turkish study on pianists' hands](https://acikbilim.yok.gov.tr/handle/20.500.12812/65385), but no search showed this author and year. This is the vaguest claim in the answer, and the one to trust least. |

### Takeaways from experiment 3
1. **Claude refused both traps.** It wouldn't invent a fake book or accept a
   question that assumed a fake study existed. It said "I'd rather not guess"
   both times.
2. **It searched before answering**, which is a big reason it got these right.
3. **The risk moves to the details.** The main answers were honest, but a
   side remark ("Kilincer et al. 2019") couldn't be confirmed. Hallucinations
   today are more likely to hide in small, specific, passing details than in
   the main answer.
4. **Verify what matters.** Names, dates, numbers, quotes and citations are the
   things to check, especially before relying on them or passing them on.
   The more specific and obscure the detail, the more checking it needs.

## Experiment 4: What does it know about today?
1. In a new chat, ask: `Without searching the web, using only what you learned in training, what are the top news stories this week? Also, when does your training knowledge end?`
2. In another new chat, ask: `Search the web: what are the top news stories this week?`

*(Newer versions of the Claude app have no on/off switch for web search; Claude
decides when to search. So we tell it in words whether it may search.
If your app has a web search toggle, under the slider or "+" icon by the message
box, you can switch it off instead.)*

**Look for:** how the two answers differ, and whether the second one cites sources.
**The lesson:** a model's knowledge stops at its **training cutoff**. Tools like
web search let it fetch fresh information. That's your first look at AI using
*tools*, which becomes a big theme later.

**My results:**

**Prompt 1 (no searching allowed):** ✅ it refused to make up news.
> I can't tell you this week's top stories from training alone. My reliable knowledge runs to the **end of June 2026**, and today is 15 October 2026, so there's a gap of about three and a half months. Anything I listed as "this week's news" would be invented or out of date.

It gave an example of the latest news it *did* know, from around June 2026,
and offered to search instead.

**Prompt 2 (search allowed):** a long, organized roundup of 12–15 October 2026
(markets, conflicts, US politics, world, UK, tech) with **9 linked sources**.

*Observations:*
- **It knew today's date** even though its training ends in June. The app tells
  it the date, just as it told it my name in experiment 2.
- **Its answer was aimed at the UK** (a UK news section, British spellings like
  "favourite" and "centre"), so the app is probably passing along my rough location too.
- **The sources were a mixed bag:** mostly daily-headline roundups and smaller sites
  rather than the original reporting. Good enough for an overview; for anything
  important I'd check a major outlet or the original source.
- **Small glitches still slip in.** One item says "Hall and Michael Woodford won"
  the Nobel prize, with the first person's first name missing. Summaries of
  summaries can lose details.

### Takeaways from experiment 4
1. **AI has a knowledge cutoff.** Claude's training runs to the end of June 2026;
   without help it knows nothing after that, and it was honest about it.
2. **Tools fill the gap.** With web search it went from "I can't tell you" to a
   current, sourced roundup. AI using tools is a major theme from here on.
3. **The app adds context I don't see:** the date, my name, probably my location.
   The model works with whatever text it's given.
4. **Cited sources let you check, so check their quality.** A link isn't a
   guarantee; who wrote the source matters.

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

*My guess beforehand:* Claude wouldn't fall for them, as they're fairly easy logic riddles. ✅ Correct.

**Puzzle 1 (bat and ball):** ✅ **$0.05**. It wrote out the algebra
(x + (x + 1.00) = 1.10), checked the answer ($1.05 + $0.05 = $1.10), and explained
why the instinctive "10 cents" is wrong (the total would be $1.20).

**Puzzle 2 (mislabelled boxes):** ✅ take one fruit from the box labelled
**"Apples & Oranges"**. It worked through both cases (draw an apple / draw an
orange), then explained why picking from either of the other boxes wouldn't work.

*Observations:*
- It **showed its reasoning step by step** in the answer itself, and checked
  its own result. Working it through is what stops the "10 cents" slip.
- It explained *why* the wrong answers are wrong, not just what's right.
- **Caveat:** both are famous puzzles that appear all over the internet, so
  Claude has almost certainly seen them, with answers, in training.
  Getting them right shows it *can* reason, but it could also be remembering.
  A fair test of reasoning needs a puzzle it can't have seen before.

### Takeaways from experiment 5
1. **Working step by step makes AI more accurate**, just as it does for people.
   Claude does this on its own for tricky problems; you can also ask for it
   ("think it through step by step", "check your answer").
2. **Ask for the reasoning, not just the answer.** Seeing the steps lets you
   spot exactly where something went wrong.
3. **Famous problems are a weak test.** To judge AI reasoning, change the
   details so it can't rely on a remembered answer.

**Bonus: the impossible puzzle.** I asked a twisted version where *exactly one*
label is wrong, which can't happen (one wrong label always forces another to be wrong).
✅ **Claude spotted it immediately:**
> The puzzle as stated can't happen: it's impossible for exactly one label to be wrong. [...] With three boxes and three distinct contents, a wrong label always forces at least one other label to be wrong too. So it's either zero wrong, two wrong (a swap), or all three wrong.

It then guessed I probably meant the classic version and solved that too.

*My reaction:* pleasantly surprised. It didn't just pattern-match to the
famous puzzle; it noticed the setup was broken and explained why, listing
every possible case. That gives me more confidence in its reasoning.

*Keeping it in perspective:* one good result builds confidence but doesn't prove
it never slips. The habit is to trust its reasoning *more* when it shows its working
and the working checks out, and to keep verifying when the stakes are high.

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

**Sentence 1 (given):** ✅ exact format.
> Score: 3/10
> Good: The meaning comes through clearly, and you've got the basic shape of a story: who went, where, when, and what happened.
> Fix: Start with "He and I" instead of "me and him," since this is the subject of the sentence. Use the past tense "went" rather than "goes" to match "yesterday." "Buyed" should be "bought," "alot" is two words ("a lot"), and "stuff" is uncountable, so it never takes an -s. Corrected: "He and I went to the store yesterday and bought a lot of stuff."

**Sentence 2 (mine, same chat, no instructions repeated):**
"Me and my dog Bagel - he is a staffy - loves to playing ball in the park."
✅ same role, same format.
> Score: 5/10
> Good: Nice use of an aside to add detail about Bagel; it gives the sentence personality, and the dashes set it off correctly.
> Fix: Put yourself last and use the subject form: "My dog Bagel and I" rather than "Me and my dog Bagel." Because there are two of you, the verb should be "love," not "loves." Choose either "to play" or "playing," not a mix of both. "Staffy" is short for Staffordshire Bull Terrier, so capitalise it. Corrected: "My dog Bagel (he's a Staffy) and I love playing ball in the park."

*Observations:*
- **The format held both times**, including for a sentence I sent later without
  repeating any instructions. The role carried on because the whole chat,
  instructions included, is sent again every turn (the same idea as experiment 2).
- **"Strict but kind" came through:** it always starts with something genuinely
  positive, then lists every error with the *reason* for each, not just the fix.
- **It added a little extra:** a "Corrected:" version inside the Fix line. Helpful,
  and still within the format, but it's a reminder that AI tends to stretch rules a bit.
- **The scores are judgments, not measurements.** 3/10 and 5/10 seem fair, but the
  same sentence in a new chat might get a different number. Treat AI scores as rough guides.
- **Small style calls presented as rules:** capitalising "Staffy" is common but
  debatable for a nickname. AI sometimes states preferences as firm rules.

### Takeaways from experiment 6
1. **A role plus an exact format makes output consistent and predictable.**
   That's how to get answers in the shape you need, every time.
2. **Instructions persist through a chat** because the whole conversation is
   resent each turn. A new chat starts from scratch, which is why Projects
   (project 04) let you save instructions permanently.
3. **AI can be a useful tutor**: it explains *why*, not just *what*.
   Still, keep its scores and style rules in perspective.

---

## What I learned
_(Fill in after the experiments, in your own words. Which result surprised you most?)_

## Questions this raised
