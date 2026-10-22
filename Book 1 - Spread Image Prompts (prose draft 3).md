# Aria and the Very Important Hello — Spread Image Prompts
### Matches prose draft 3. 15 double-page spreads, with the text of both pages lettered into one continuous illustration.

This replaces the single-page prompts (kept as `Book 1 - Page Image Prompts (single pages, superseded).md`). The story text and the page split are unchanged. Each pair of text pages now shares one illustration that runs across both pages.

---

## Book layout (36 pages)

| Book pages | Content | Image |
|---|---|---|
| 1 | Title page | single page (right) |
| 2 | Copyright page | single page (left) |
| 3 | Dedication page | single page (right) |
| 4–5 | Spread 1 (story text pages 1–2) | spread |
| 6–7 | Spread 2 (text pages 3–4) | spread |
| 8–9 | Spread 3 (text pages 5–6) | spread |
| 10–11 | Spread 4 (text pages 7–8) | spread |
| 12–13 | Spread 5 (text pages 9–10) | spread |
| 14–15 | Spread 6 (text pages 11–12) | spread |
| 16–17 | Spread 7 (text pages 13–14) | spread |
| 18–19 | Spread 8 (text pages 15–16) | spread |
| 20–21 | Spread 9 (text pages 17–18) | spread |
| 22–23 | Spread 10 (text pages 19–20) | spread |
| 24–25 | Spread 11 (text pages 21–22) | spread |
| 26–27 | Spread 12 (text pages 23–24) | spread |
| 28–29 | Spread 13 (text pages 25–26) | spread |
| 30–31 | Spread 14 (text pages 27–28) | spread |
| 32–33 | Spread 15, the ending (text page 29) | spread |
| 34–35 | Aria's Adventure Journal (discussion prompts and challenge) | spread |
| 36 | Blank page | single page (left), plain cream, no image needed |

In a printed book, page 1 is a single right-hand page, and every even page sits on the left. Title, copyright and dedication now each have their own page. The copyright (left) faces the dedication (right), which is the usual arrangement. That lets the story start on a full spread at pages 4–5. The Adventure Journal gets its own spread after the story ends, and the blank page 36 keeps the page count even.

**Printer check:** 36 pages is a multiple of 4, so it works for every common printer, including Amazon KDP paperback, hardcover and saddle-stitched books.

---

## Mixed layout: paired single pages (decided 2026-10-21)

Spreads 2, 9 and 14 move between two different places, so each is made as **two facing single pages** instead of one continuous spread. Every other spread stays one continuous illustration.

| Spread | Left page | Right page |
|---|---|---|
| 2 | Text page 3: the porch (Single pages/Page 03 v2.png) | Text page 4: the mirror (existing page 4.png) |
| 9 | Text page 17: the pawpaw memory | Text page 18: the church-lady memory, with small Kai |
| 14 | Text page 27: the walk home | Text page 28: Kai at the classroom door |

**Rules for single pages:** square 1:1 at 4k. On a LEFT page, keep faces, hands and text at least 12% from the RIGHT edge (the fold). On a RIGHT page, keep them at least 12% from the LEFT edge. Attach the facing page as the typography and lighting reference so the pair matches. The scene descriptions in the spread prompts below still apply; split them into the two halves.

---

## How to use these

1. **One spread per image.** Each prompt makes ONE wide 2:1 image covering both pages.
2. **Attach the approved reference sheets** listed under "Attach". The sheets are the source of truth.
3. **Paste the Global Prefix first**, then the spread prompt.
4. **Generate Spread 1 and Spread 4 first.** Approve them, then attach Spread 1 as the **nursery/home reference** and Spread 4 as the **town reference** on later spreads.
5. **Attach a typography reference on every spread.** Once one spread's lettering looks right, attach it to every later prompt as the "typography reference spread".
6. **Proofread both text blocks on every spread** against this file. If a spread keeps coming out wrong, generate it with the two text areas left empty and add the text afterwards in a design tool.
7. **Butterfly rule:** the yellow butterfly appears ONLY on Spread 10 (right half) and Spread 15.
8. **Potcake rule:** small and findable on the town spreads where the prompt places him.

### Sheets
- **Done:** Mama, Aria (coral town outfit), Kai, Auntie, the carpool girl, Mr. Rolle, Miss Pearl, the potcake, the butterfly, Grandma.
- **Still needed if not yet made:** Aria's home outfit (white sleep romper). The prompt is at the end.
- **Do not use the baby on Mama's sheet**; it shows a toddler. Always attach Aria's own sheet.

---

## Global Prefix (paste at the start of every spread prompt)

> FORMAT: ONE wide double-page picture-book spread in landscape. It is a single continuous illustration that flows across both pages: one scene, one light source, one horizon. The vertical centre line is the GUTTER (the book's fold). Keep a clear band about 8% of the image width down the centre free of faces, hands, important action and all lettering. Do not draw a visible fold, border or dividing line. Never show the same character twice in one spread unless the prompt asks for vignettes. IMPORTANT TRIM: for print, about 6% of the image height will be cut off the very top and 6% off the very bottom. Treat those strips as background only: keep ALL lettering, ALL faces and the tops of heads and hair at least 12% of the image height away from the top and bottom edges. Also keep all lettering and faces at least 7% of the image width away from the left and right edges. Keep windows, doors and other strong verticals off the centre line.

**Generation settings (tested on Spread 1, 2026-10-21):** Higgsfield GPT Image 2.5, aspect ratio **16:9**, quality **high**, resolution **4k** (output is 3840 × 2160). Then trim to the 2:1 print shape with `Aria and the Very Important Hello/Spreads/crop_to_2x1.py`, which trims the top and bottom evenly to give 3840 × 1920. Do NOT use 21:9: at that width the model pushes the text to the side edges, and trimming the sides cuts it (two failed tests). Before printing, upscale each approved spread to at least 5175 × 2625 px (17.25 × 8.75 inches at 300 dpi, including bleed for an 8.5 × 8.5 inch book).
>
> STYLE: Traditional watercolour with fine, slightly broken sepia-black ink linework. Loose wet-in-wet washes in the background, more controlled painting on the characters. Visible cold-press paper texture, soft colour bleeding at the edges, warm natural light. Gently stylised proportions, expressive faces, warm and humorous. Hand-painted, never digital-looking.
>
> CHARACTERS: Match the attached character reference sheets exactly: same face shape, skin tone, eye shape, hair texture and colour, glasses, jewellery, outfit and proportions. Do not invent new features, change outfits, or age anyone up or down. Baby Aria is six months old: she sits or lies, never stands or walks, and has no teeth. Only the characters named in the prompt appear, plus unnamed background townspeople where the prompt asks for them.
>
> LETTERING: The spread has TWO text blocks: TEXT A belongs on the LEFT page (left half of the image) and TEXT B on the RIGHT page (right half). Letter each block EXACTLY as written: same words, spelling, capitals, punctuation and line breaks. Do not add, drop, reorder, paraphrase or merge any words. Never let a text block cross the gutter.
> - Typeface: one clean, warm, highly legible classic book serif, regular weight, dark sepia-black, left-aligned. The same typeface on every spread.
> - Size is FIXED and identical on every spread. It does NOT grow to fill empty space and does NOT shrink to fit. Capital letters are about 2.5% of the image height, so roughly 25 lines of text would fill the full height. Lines run about 40 to 50 characters, and each text block is no wider than about 40% of its own page, with comfortable line spacing.
> - Match the size, typeface, weight, colour and line spacing of the attached typography reference spread exactly.
> - If a text block is short and its space is large, keep the fixed size and leave the extra space empty.
> - Only a line the prompt marks as larger may be bigger, and never more than about 1.3 times the body size.
> - Keep every text block at least 4% of the image width from the outer edges and the gutter band, on a calm, pale, lightly washed area with no busy detail behind the letters.
> - TEXT A and TEXT B are the ONLY lettering in the image: no other words, signs, labels, numbers, logos, speech bubbles or captions.
>
> AVOID: 3D rendering, glossy or plastic shading, cartoon vector look, anime eyes, photorealism, heavy black outlines, extra fingers or limbs, a yellow butterfly unless the prompt asks for one.

---

## Recurring details (copy into prompts as needed)

- **Aria, home outfit:** soft white cotton sleep romper with a tiny yellow-elder flower print; two tiny pigtail puffs with small white bows; tiny gold studs.
- **Aria, town outfit:** as on her reference sheet (coral ribbed flutter-sleeve romper, coral bow on her top-knot, barefoot).
- **Mama, home look:** locs in a high bun, peach house dress, brown glasses, gold bangles, gold hoops.
- **Mama, town look:** as on her reference sheet.
- **Stroller:** a striped sea-glass-teal and white stroller with a fabric sunshade.
- **Home:** a small Bahamian wooden cottage painted pale lime green with white trim, wooden jalousie (louvre) windows, a front porch with three wooden steps, a low white picket fence and gate, a yellow elder bush and pink bougainvillea. Inside: a small nursery with a white wooden crib, a jalousie window, a play mat and a low wall mirror.
- **Town:** an ordinary, lived-in Bahamian street. Faded pastel shopfronts (peach, sky blue, lime) in painted wood and stucco, overhead power lines, a narrow pavement, a white jitney minibus with a coloured stripe. Rolle's General Store has a wooden porch. Miss Pearl's fruit stand sits under a faded umbrella. The bank is a modest pale-coral building with white columns and a wooden bench outside, under a flowering poinciana tree. No beach, no resort, and no lettering on any signs.

---

## Spread 1 — book pages 2–3

**Attach:** Mama, Aria (plus the home-outfit sheet). **Approve and use as the nursery reference.**

**TEXT A (left page):**
> Every morning, Mama leaned over the crib and said the same thing.
>
> "Good morning, sunshine."

**TEXT B (right page):**
> And every morning, Aria said hello back. Not with words. Aria was six months old.
>
> She said it with her legs.
>
> Kick. Kick. KICK-KICK-KICK.

**Prompt:**
> A small sunlit nursery in a Bahamian wooden cottage, seen as one continuous room across the spread. Early golden light falls in stripes through an open wooden jalousie window. LEFT half: Mama (home look: locs in a high bun, peach house dress, brown glasses, gold bangles) leans over the rail of a white wooden crib, laughing tenderly; her face is in the left third. RIGHT half: inside the crib, Aria (white yellow-elder sleep romper, two pigtail puffs) lies on her back, kicking both legs so fast they are a happy blur (soft repeated watercolour strokes and small splashes of motion), arms out, mouth open in delight; her face is in the right third. The crib runs across the gutter, but no face sits on it. TEXT A on the pale wall at upper left. TEXT B on the pale wall at upper right, with "Kick. Kick. KICK-KICK-KICK." slightly larger on its own line. No butterfly.

---

## Spread 2 — book pages 4–5

**Attach:** Grandma, Mama, Aria, Potcake.

**TEXT A (left page):**
> Aria had lots of hellos.
>
> When Grandma came up the front steps, she squealed so high that the potcake by the gate flattened his ears.

**TEXT B (right page):**
> And when she saw the baby in the mirror, she leaned in close and said, "BAH!"
>
> The baby in the mirror said "BAH!" right back.
>
> Aria thought that was very good manners.

**Prompt:**
> Two soft-edged watercolour vignettes on one continuous warm cream spread, joined by a gentle wash. (Here Aria may appear twice, once in each vignette.)
> LEFT VIGNETTE: the front porch of a pale lime-green wooden cottage with white trim, a yellow elder and bougainvillea. Grandma climbs the three porch steps with her handbag on her forearm, smiling broadly. Mama stands at the open screen door holding Aria (white yellow-elder sleep romper) on her hip; Aria squeals, mouth wide open, arms flung out. By the white picket gate, the sandy-ginger potcake flattens both ears and squints, comically pained by the noise.
> RIGHT VIGNETTE: indoors, Aria sits on a play mat nose-to-nose with a low wall mirror, mouth wide in a big "BAH!", and her reflection makes exactly the same face back.
> TEXT A in the open cream space above the left vignette; TEXT B above the right vignette. No butterfly.

---

## Spread 3 — book pages 6–7

**Attach:** Grandma, Mama, Aria.

**TEXT A (left page):**
> Lately, Aria had been working on a brand-new hello.
>
> A wave.
>
> Up went her arm.
> Flap went her fingers.
> SWOOP went her hand.

**TEXT B (right page):**
> It looked as if she were trying to catch a butterfly.
>
> There was no butterfly.
>
> "She's waving!" said Grandma.
>
> "She's swatting," said Mama.
>
> Aria did it again, just to be sure.

**Prompt:**
> The shady cottage porch, one continuous scene. LEFT half: open porch space with TEXT A in the calm upper area. Beneath it, three small soft-edged sketches of Aria's hand show the arm going up, the fingers flapping and the hand swooping (hands only, not extra babies). RIGHT half: Grandma and Mama sit side by side on a porch bench. Aria (white yellow-elder sleep romper, two pigtail puffs) sits on Mama's lap facing out, swiping the air mid-"wave" with fingers splayed and tongue out, as if grabbing something invisible. The air around her hand is EMPTY. Grandma points at her, thrilled and beaming. Mama presses her lips together, cheeks lifted, trying not to laugh. TEXT B in the calm area at upper right. NO butterfly anywhere.

---

## Spread 4 — book pages 8–9

**Attach:** Mama, Aria (town outfit), Potcake. **Approve and use as the town reference.**

**TEXT A (left page):**
> One Tuesday morning, Mama had errands to run, so Aria rode into town in her striped stroller.

**TEXT B (right page):**
> Behind them trotted the potcake, as if he had errands too.

**Prompt:**
> A wide, sunny view of an ordinary Bahamian town street running across the whole spread: faded pastel shopfronts (peach, sky blue, lime) with blank signs, overhead power lines, a yellow elder in bloom, bougainvillea spilling over a wall. RIGHT half: Mama (town look) walks to the right pushing the striped sea-glass-teal stroller. Aria (coral romper, coral top-knot bow) sits up eagerly with the sunshade pushed halfway up so she can see out. Mama's woven bag holds a folded list, a light-bill envelope and a letter. LEFT half, in the foreground: the sandy-ginger potcake trots after them with his curled tail high and a serious, purposeful, important expression, as if he has errands too. TEXT A in the sky at upper left; TEXT B in the sky at upper right. No butterfly.

---

## Spread 5 — book pages 10–11

**Attach:** Mama, Aria, Mr. Rolle, Miss Pearl, Potcake, plus the town reference.

**TEXT A (left page):**
> Mama greeted everyone.
>
> "Morning, Mr. Rolle!"
>
> Mr. Rolle grinned. "Mornin', mornin'! And mornin' to the little lady."

**TEXT B (right page):**
> "Good morning, Miss Pearl!"
>
> Miss Pearl looked up from her mangoes. "Look at that baby, gettin' so big!"
>
> Good morning here, good morning there,
> good mornings, mornings everywhere!

**Prompt:**
> The same town street, one continuous scene. LEFT half: the wooden porch of a small painted general store with a blank signboard. Mr. Rolle leans on his straw broom, grinning warmly and tipping his head toward the baby. Mama, pushing the teal-striped stroller, waves to him brightly. Aria (coral romper) looks up at him with wide eyes. RIGHT half: Miss Pearl sits at her wooden fruit stand piled with mangoes, sapodillas and bananas under a faded umbrella, laughing with one hand on her chest and pointing fondly toward Aria. The potcake sniffs at the base of the fruit stand. TEXT A above the store at upper left; TEXT B at upper right, with the two-line chant set slightly apart. No butterfly.

---

## Spread 6 — book pages 12–13

**Attach:** Mama, Aria, Potcake, plus the town reference.

**TEXT A (left page):**
> Good morning to the baker. Good morning to the jitney driver.
>
> Aria's head went left. Aria's head went right.

**TEXT B (right page):**
> Good morning here, good morning there,
> good mornings, mornings everywhere!
>
> Some were loud. Some were just a nod. One was two fingers lifted off a steering wheel.
>
> Aria had not known there were so many hellos in the whole world.

**Prompt:**
> A lively stretch of the same street, full of small greetings. LEFT half: a baker in a flour-dusted apron waves from a bakery doorway, and a white jitney minibus passes with its driver lifting two fingers off the steering wheel. Mama greets them both. RIGHT half: Aria (coral romper) leans out of the teal-striped stroller, mouth a perfect O, eyes enormous with wonder, her head turned with a playful motion line to show it swivelling. Around her, people of different ages, builds and skin tones nod and wave, and a man in a parked car, elbow out of the window, turns to say good morning back. The potcake sits on a step. TEXT A at upper left; TEXT B at upper right. No butterfly.

---

## Spread 7 — book pages 14–15

**Attach:** Kai, Auntie, Aria, Mama, Potcake, plus the town reference.

**TEXT A (left page):**
> Good morning here, good morning there...
>
> But outside the bank, on a bench, sat a boy who did not look like good morning at all.

**TEXT B (right page):**
> His backpack was so big it looked as if it might carry him off.
>
> The boy sat very still, holding his backpack straps with both hands.
>
> Aria looked at him.
>
> The boy looked at Aria.
>
> Then he looked at his shoes.

**Prompt:**
> LEFT half: the busy street in soft blurred motion: people walking past, a jitney going by. In the lower left foreground, Mama mid-step with the teal-striped stroller; Aria (coral romper) has turned to gaze toward the right with her serious, studying stare. RIGHT half: a modest pale-coral bank with white columns, and a wooden bench under a flowering poinciana tree. On it sits Kai, small and very still, with an enormous red backpack (green dinosaur keyring dangling), gripping both straps and looking down at his shoes. Auntie, in teal scrubs, sits beside him checking her watch. The potcake lies in the shade under the bench. Kai is the only still thing on the spread; give him plenty of empty space so he looks small. TEXT A in the sky at upper left; TEXT B in the pale sky at upper right. No butterfly.

---

## Spread 8 — book pages 16–17

**Attach:** Mama, Auntie, Kai, Aria.

**TEXT A (left page):**
> "Morning," said Mama.
>
> "Morning," said his aunt. "This is Kai. New school today."
>
> "And this is Aria," said Mama. "That's a big day, Kai."

**TEXT B (right page):**
> Kai held his straps a little tighter.
>
> "What if nobody says hi to me?" he whispered.
>
> The grown-ups looked at each other.
>
> Aria looked at Kai.

**Prompt:**
> A quieter, closer view at the bank bench. LEFT half: Mama bends slightly toward the bench with a warm, gentle smile, one hand on the teal-striped stroller; Aria (coral romper) watches Kai intently with her serious stare, eyebrows lifted. RIGHT half: Kai sits on the bench gripping his red backpack straps tighter, his new black shoes pressed together heel to heel, small and worried as he whispers. Auntie sits beside him. Mama and Auntie exchange a soft, wordless look across the space between them (their eyes meet; the gutter band itself stays clear). Muted, gentle light and a simple background. TEXT A at upper left; TEXT B at upper right. No butterfly.

---

## Spread 9 — book pages 18–19

**Attach:** Aria, Mama, Kai.

**TEXT A (left page):**
> Aria didn't know what school was.
>
> But she knew about new.
>
> New could be wonderful, like the first taste of mashed-up pawpaw.

**TEXT B (right page):**
> New could also be too much, like the lady at church who pinched her cheeks.
>
> Kai looked like the second kind of new.

**Prompt:**
> Soft, dreamy memory vignettes fading into warm cream paper. (Aria may appear in each vignette.) LEFT VIGNETTE: at home, Aria (white yellow-elder sleep romper) tastes mashed orange pawpaw from a small spoon held by Mama's hand with its gold bangles; pawpaw smeared on her cheeks, eyes squeezed shut with total delight. RIGHT VIGNETTE: a friendly church lady in a large floral Sunday hat leans in to pinch Aria's cheeks while Aria buries her face in Mama's neck with one eye peeking out. Below the right vignette, small and back in the present: Kai on the bank bench gripping his straps. TEXT A in the open cream space at upper left; TEXT B in the open space at right, between the vignette and small Kai. No butterfly.

---

## Spread 10 — book pages 20–21 (BUTTERFLY SPREAD)

**Attach:** Kai, Aria, Butterfly.

**TEXT A (left page):**
> Kai peeked at Aria again.
>
> So Aria gave him her best smile. It was very gummy and had no teeth in it at all.
>
> Kai's mouth twitched.

**TEXT B (right page):**
> Then Aria decided it was time.
>
> Up went her arm.
> Flap went her fingers.
> SWOOP went her hand.
>
> It was the best wave she had ever done.
>
> It was still mostly a swat.

**Prompt:**
> A close two-character moment. LEFT half: Kai on the bench peeks sideways toward the right, and the corner of his mouth twitches toward a smile; he is still holding his straps. RIGHT half: Aria (coral romper) in the teal-striped stroller beams her biggest gummy, toothless grin toward Kai and does her best wave: one chubby arm high, fingers splayed, hand mid-swoop, tongue out in concentration, wobbling. It looks mostly like a swat. IMPORTANT: one tiny lemon-yellow butterfly flutters just above Aria's raised hand. Nobody notices it. It is small and easy to miss. TEXT A at upper left; TEXT B at upper right, with the three refrain lines each on their own line.

---

## Spread 11 — book pages 22–23

**Attach:** Kai, Aria, Mama, Auntie, Mr. Rolle, Potcake, plus the town reference.

**TEXT A (left page):**
> Slowly, Kai let go of one backpack strap and lifted his own.
>
> He waved back.
>
> And his face did something it had not done all morning. It smiled.

**TEXT B (right page):**
> "Hi, Aria," he said.
>
> Kick. Kick. KICK-KICK-KICK.
>
> "GAH-BAH-BLAAAH-DEH!" said Aria.
>
> Kai laughed. His aunt laughed. Mama laughed.

**Prompt:**
> Joy breaks out outside the bank. LEFT half: Kai has stepped off the bench toward the stroller, one hand on a strap and the other raised in a wave, smiling his first real gap-toothed smile. Far across the street behind him, Mr. Rolle laughs too, leaning on his broom, clearly with no idea what is funny. RIGHT half: Aria (coral romper) in the teal-striped stroller kicks both legs and flaps both arms, laughing hardest of all, mouth wide open. Mama and Auntie laugh together beside her. The potcake's tail is a happy blur. Warm, bright light. TEXT A at upper left; TEXT B at upper right, with "GAH-BAH-BLAAAH-DEH!" a little larger and bouncier. No butterfly.

---

## Spread 12 — book pages 24–25

**Attach:** Kai, Auntie, Mama, Aria, plus the town reference.

**TEXT A (left page):**
> Then a horn went beep-beep.
>
> A car pulled up to the kerb. Inside were children Kai didn't know.
>
> Kai's smile went somewhere far away. He held both straps again.
>
> His feet would not go.

**TEXT B (right page):**
> Nobody told Kai to be brave. Nobody told him there was nothing to worry about.
>
> "New things can feel big," Mama said quietly.
>
> Kai's aunt put her hand on his back and left it there.

**Prompt:**
> A quieter, stiller spread: the same warm light, more muted colour. LEFT half: a silver hatchback at the kerb, back door swung open, a cheerful woman with sunglasses pushed up on her head waving from the driver's seat, children in the back seat. Kai stands frozen on the pavement facing the open door, gripping both straps, smile gone, eyes wide, feet planted. Auntie stands just behind him with her hand flat on the middle of his back. RIGHT half: Mama stands beside the teal-striped stroller looking at Kai with quiet understanding, not pushing; Aria (coral romper) watches. TEXT A at upper left above the car; TEXT B at upper right. No butterfly.

---

## Spread 13 — book pages 26–27

**Attach:** Carpool girl, Kai, Aria, Mama, Auntie.

**TEXT A (left page):**
> In the back seat, a girl moved her bag and patted the empty space beside her.
>
> Pat, pat.
>
> Kai looked at his aunt.
>
> He looked at the car.
>
> He looked back at Aria.

**TEXT B (right page):**
> Aria was still waving. By now she was waving with both arms and kicking with both feet, which is the biggest hello a person can do without standing up.
>
> "Bye, Aria," said Kai.
>
> His tummy was still flip-flopping.
>
> But he went.

**Prompt:**
> LEFT half: the silver car's open back door. Inside, the girl with two plaits and white ribbon bows (navy pinafore, white shirt with the same school crest as Kai) has moved her patched teal backpack to the floor and pats the empty seat beside her with a friendly gap-toothed grin. Kai stands at the door with one foot lifting toward the car, looking back over his shoulder toward the right, one hand raised in a small goodbye, still a little worried. Auntie is beside him. RIGHT half: Aria (coral romper) in the teal-striped stroller waves with both arms AND kicks with both feet at once, the biggest hello possible, her whole body in motion. Mama stands behind the stroller. TEXT A at upper left above the car; TEXT B at upper right, with "But he went." on its own final line. No butterfly.

---

## Spread 14 — book pages 28–29

**Attach:** Mama, Aria, Potcake, Kai, Carpool girl.

**TEXT A (left page):**
> "You know what, Miss Aria?" Mama said on the way home. "That was a very important hello."
>
> Aria didn't know what important meant. She was busy chewing her stroller strap.

**TEXT B (right page):**
> But she had heard a lot of hellos that day.
>
> Hellos here, hellos there,
> hellos, hellos everywhere.
>
> A hello with a broom. A hello off a steering wheel. A pat on an empty seat.
>
> And one that looked a lot like a swat at a butterfly.
>
> Across town, a classroom door opened.

**Prompt:**
> LEFT half: a quiet residential lane of pastel cottages with a yellow elder. The potcake trots ahead. Mama walks slowly, smiling down, pushing the teal-striped stroller with a loaf of bread poking out of her woven bag. Aria (coral romper) happily chews the stroller strap, completely unconcerned. RIGHT half, as a soft-edged vignette that melts out of the lane's sky: across town, the open door of a bright classroom with small chairs and children's paintings (no lettering). Kai stands in the doorway with the girl from the car beside him, his red backpack on, giving a small, careful wave to a child inside. He looks nervous but hopeful. TEXT A in the sky at upper left; TEXT B at upper right beside the vignette, with the two-line chant set slightly apart. No butterfly.

---

## Spread 15 — book pages 30–31, the ending (BUTTERFLY SPREAD)

**Attach:** Mama, Aria, Butterfly, plus Spread 1 as the nursery reference.

**TEXT A (left page):**
> The next morning, Mama leaned over the crib.
>
> "Good morning, sunshine."
>
> Aria looked at her. She thought about it.
>
> Up went her arm.
> Flap went her fingers.
> Swoop went her hand, wobbly and slow.

**TEXT B (right page):**
> Mama's whole face lit up. "Well," she said, "hello to you, too."
>
> Kick. Kick. KICK-KICK-KICK.
>
> Some hellos are worth saying twice.

**Prompt:**
> The same sunlit nursery as Spread 1, the next morning, deliberately echoing that first composition. LEFT half: Mama (locs in a high bun, peach house dress, brown glasses, gold bangles) leans over the crib rail, her whole face lit up with delighted surprise. RIGHT half: Aria (white yellow-elder sleep romper, two pigtail puffs) looks up at her and deliberately raises one small hand in a wobbly, slow wave, legs kicking. Golden light through the jalousie window on the right, where the small lemon-yellow butterfly sits on the windowsill with its wings open. Keep the picture simple to give the text room. TEXT A on the pale wall at upper left; TEXT B on the pale wall at upper right, with "Some hellos are worth saying twice." slightly larger on its own final line.

---

## Aria's Adventure Journal — book pages 34–35

**Attach:** Aria (town outfit), Kai, Potcake, plus the typography reference spread.

This spread is text-heavy, with headings in two sizes. Try it lettered first. If any heading or line comes out wrong, generate the art with the two pale panels left empty, then typeset the text in the same serif. On this spread, typesetting is the more reliable choice.

**TEXT A (left page):**
> Aria's Adventure Journal
>
> What Aria Discovered
>
> A hello may seem small, but it can help someone feel seen, welcomed, and included.
>
> People say hello in many ways—with words, waves, smiles, signs, gestures, and sometimes simply by making room for someone.
>
> Talk About It
>
> How do you like to say hello?
>
> Kai asked, "What if nobody says hi to me?" Who said hi to him first?
>
> How do you think Kai felt when the girl patted the seat beside her?
>
> Have you ever felt nervous somewhere new?
>
> What could you do if you noticed someone who seemed left out?
>
> Can you think of a way to say hello without using any words?

**TEXT B (right page):**
> Aria's Adventure Club Challenge
>
> Today, look for one opportunity to help someone feel welcome.
>
> It could be a wave.
> A smile.
> Making room beside you.
> Inviting someone to play.
> Or simply saying:
> "Hello."
>
> Sometimes little things are very important things.
>
> Look Again
>
> Can you find the potcake on every page in town?
>
> The book says there was no butterfly. Look again.

**Prompt:**
> A warm, journal-style spread on cream paper, like the open pages of a child's scrapbook. Two large pale panels hold the text, one on each page, with soft watercolour edges. Around the panels, small loose watercolour spot illustrations from the story: Aria (coral romper) mid-wave in her stroller in the lower left corner; Kai's red backpack with the green dinosaur keyring; a straw broom; a mango; two fingers lifted off a steering wheel; a hand patting a car seat; the potcake peeking in from the lower right corner. Keep the spot illustrations small, so the text panels stay calm and uncluttered. No butterfly.
> LETTERING: Letter TEXT A in the left panel and TEXT B in the right panel, exactly as written. "Aria's Adventure Journal" is the largest heading, in the warm hand-lettered display style from the cover. "What Aria Discovered", "Talk About It", "Aria's Adventure Club Challenge" and "Look Again" are smaller headings in the same display style, about 1.3 times the body size. Everything else is at the fixed body size in the book serif. Set each question on its own line with a little space between questions.
---

# Single pages: covers, title, copyright, dedication and blank page

For these, use the Global Prefix but **replace the FORMAT paragraph with: "ONE single square picture-book page (1:1)."** Replace the LETTERING paragraph with the lettering instructions given in each prompt.

**Fill in before generating:** the author name (I used **Barbara Franks**), the dedication wording, the publisher or imprint, and the ISBN. The series line, **An Aria's Adventure Club Book**, is plain lettering until the new watercolour logo exists.

## Front cover

**Attach:** Aria (town outfit), Kai, Mama, Potcake, plus the town reference.

> A square front cover. On a sunny Bahamian town street outside a pale-coral bank under a flowering poinciana tree, Aria (coral romper, coral top-knot bow) sits up in her teal-striped stroller in the lower left foreground and gives her big wobbly "wave": arm high, fingers splayed, tongue out, delighted. On the bench to the right, Kai, small beside his enormous red backpack with its green dinosaur keyring, holds his straps and turns toward her with the very first hint of a smile. Mama stands behind the stroller, smiling down. The potcake sits by the bench looking straight out at the reader. Warm golden morning light and a clean pale sky across the top third. No butterfly.
> COVER LETTERING: Letter "Aria and the Very Important Hello" large across the pale sky at the top in a warm, rounded, hand-lettered display style in dark sepia-brown, with "Very Important Hello" slightly larger than "Aria and the". Letter "An Aria's Adventure Club Book" in small capitals near the title, and "Barbara Franks" at the bottom in the clean book serif. Spell everything exactly as given. No other lettering.

## Book page 1: title page

**Attach:** Aria (home-outfit sheet).

> A mostly empty cream page. In the lower half, a small soft-edged vignette: Aria (white yellow-elder sleep romper, two pigtail puffs with white bows) sits on a play mat raising one small hand in her wobbly first wave, tongue poking out. Lots of open paper. No butterfly.
> LETTERING: In the upper third, letter "Aria and the Very Important Hello" in the same warm hand-lettered display style as the cover, with "Barbara Franks" beneath it in the clean book serif. No other lettering.

## Book page 2: copyright page

Generate only the small illustration in the image, then typeset the copyright text afterwards. Image tools garble small legal text and ISBNs.

> A quiet cream page. In the upper half, a small soft-edged watercolour vignette: the sandy-ginger potcake curled up asleep in a patch of morning sun, his curled tail over his nose. The lower half is completely blank cream paper, with no marks and no lettering anywhere in the image.

**Copyright text to typeset in the blank area** (small, centred, same serif):
> Aria and the Very Important Hello
> An Aria's Adventure Club Book
>
> Text copyright © 2026 Barbara Franks
> All rights reserved. No part of this book may be reproduced, stored or transmitted in any form or by any means without written permission from the author, except for brief quotations in reviews.
>
> Published by [publisher or imprint name]
> ISBN [to be added]
>
> First edition

## Book page 3: dedication page

**Attach:** Mama, Aria.

> A quiet cream page, mostly open paper. In the lower third, a small soft-edged watercolour vignette: Aria's tiny hand curled around one of Mama's fingers, with Mama's gold bangles just visible at her wrist. Close up, with no faces. No butterfly.
> LETTERING: In the upper middle of the page, letter the dedication centred, in italic book serif at the fixed body size, exactly as given: [paste the chosen dedication]. No other lettering.

**Dedication options:**
> For Aria,
> whose very first hellos
> taught me what this book is about.

> For Aria,
> and for everyone who says hello first.

## Book page 36: blank page

No image needed. Leave it as plain cream paper, the same colour as the other page backgrounds.

## Back cover

**Attach:** Aria (town outfit), Potcake, plus the town reference.

**Blurb:**
> Aria is six months old, and she already has lots of hellos: a kick for Mama, a squeal for Grandma and a "BAH!" for the baby in the mirror.
>
> Then, on a busy morning in town, she meets Kai. It is his first day at a new school, and he is worried that nobody will say hi.
>
> A warm, funny story about a very small person and a very big hello.

> A square back cover in the same style as the front. Lower left: Aria (coral romper) in her teal-striped stroller, seen from slightly behind, waving with both arms and kicking both feet toward the town street, with the potcake sitting beside the stroller looking back at the reader over his shoulder. Soft warm morning light. The upper two-thirds is a calm, pale washed sky. No butterfly.
> LETTERING: Letter the blurb exactly as given in the pale upper area, in the clean book serif, left-aligned, with a blank line between paragraphs. Below it, letter "An Aria's Adventure Club Book" in small capitals and "Ages 3–6" beneath that. In the bottom right corner, leave a plain empty cream rectangle about 2 × 1.2 inches for the barcode. No other lettering.

**Printing note:** print services such as Amazon KDP take the paperback cover as ONE wraparound image (back, spine, front) sized to their template. A 32-page book's spine is too thin for lettering. Join the front and back on the template with a plain spine in the sky colour. For an 8.5 × 8.5 inch book, each interior spread is 17 × 8.5 inches plus the printer's bleed, so check the printer's bleed and gutter guidance before the final export.

---

# Reference sheet prompts

For each one, use the Global Prefix with the FORMAT paragraph replaced by "ONE reference sheet image, landscape" and the LETTERING paragraph replaced by "No lettering anywhere." Attach the person's photo as a likeness reference only.

## Aria's home outfit

**Attach:** Aria's approved sheet.

> Character outfit sheet on plain warm off-white paper. The same baby Aria from the attached sheet, with an identical face, skin and proportions, now wearing a soft white cotton sleep romper with a tiny yellow-elder flower print, her hair in two tiny pigtail puffs with small white bows, tiny gold studs, barefoot. Front, three-quarter, side and back views sitting, plus one lying on her back. Small colour swatches.

## Aunt Gail (future books)

> Character reference sheet on plain warm off-white paper. A glamorous, fun Bahamian aunt: warm medium-light brown skin, an oval face with high cheekbones, strongly arched defined brows, almond eyes, a bright closed-lip smile and lightly suggested glossy pink lips. Long, sleek, straight black-brown hair with a deep side part, swept over one shoulder, with chunky honey-blonde face-framing highlights and one side tucked behind her ear. Large chunky textured gold hoops and a silver link watch. A leopard-print sleeveless top, dark jeans and a black crossbody bag. Full body in front, three-quarter, side and back views at the same scale. Below, six expressions: bright smile, big laugh, playful wink, surprised delight, fond look at a baby, mock-scandalised. Small colour swatches.

## Aunty Ann (future books)

> Character reference sheet on plain warm off-white paper. A cool, quietly confident Bahamian aunt: light-medium warm brown skin, a soft oval face, defined brows, gentle hooded eyes, a small knowing smile and lightly suggested berry-red lips. Hair pulled back sleek and tight from the hairline with neat laid edges into a very long, very full blown-out ponytail with a kinky-straight texture, falling over one shoulder. Large thin gold hoops and a silver chain with a heart pendant. A white top with a black bow detail and tailored trousers. Full body in front, three-quarter, side and back views at the same scale. Below, six expressions: knowing smile, soft laugh, raised eyebrow, warm affection, thoughtful, delighted surprise. Small colour swatches.
