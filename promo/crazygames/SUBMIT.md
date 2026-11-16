# Submitting Blip Panic to CrazyGames

Portal: https://developer.crazygames.com (sign up / log in, then "Submit a game" / "Add new game").

## Files to upload
| What | File |
| --- | --- |
| Game (HTML5 zip) | `dist/blip-panic-crazygames.zip` (index.html at the root, CrazyGames SDK v3 built in) |
| Cover, landscape 16:9 (1920x1080) | `promo/crazygames/cover-landscape-1920x1080.png` |
| Cover, portrait 2:3 (800x1200) | `promo/crazygames/cover-portrait-800x1200.png` |
| Cover, square 1:1 (800x800) | `promo/crazygames/cover-square-800x800.png` |
| Video, landscape 1080p (19.5 s, no sound) | `promo/crazygames/trailer-landscape.mp4` |
| Video, portrait 1080x1620 (19.5 s, no sound) | `promo/crazygames/trailer-portrait.mp4` |

Rebuild the zip after any change with `python build.py`.

## Form answers
- **Title:** Blip Panic
- **Engine / technology:** HTML5 (plain JavaScript, canvas)
- **Category:** Arcade (also fits: Casual, Skill)
- **Tags:** arcade, dodge, bullet hell, mouse, skill, high score, pixel, casual, 2d, one hand
- **Orientation:** Landscape
- **Devices:** Desktop and mobile (phone + tablet)
- **SDK:** Yes, CrazyGames HTML5 SDK v3 (gameplayStart/Stop, midgame + rewarded ads, happytime, muteAudio setting)
- **Saves:** browser localStorage (best scores, gems, skins)
- **Languages:** English

### Short description
Dodge the bubbles, grab the gems! Steer a tiny blip through an arena that levels up every few seconds.

### Description
You are a tiny blip and everything else wants you gone. Steer around the arena, grab the gems and touch nothing else.

The arena levels up every few seconds and gets meaner:
- Warm-up: shiny bubbles bounce off the walls and off each other like pool balls.
- Zoomers (level 3): a ring flashes, then a fast one shoots across, usually right at you.
- Chasers (level 5): little monsters that hunt you down for a while.

Hiding in a corner? It heats up, flashes MOVE! and sends a zoomer your way.

Score 10 points per second and 50 per gem. Spend gems on blip skins (Ice, Fire, Glitch, Rainbow) and arena themes (Deep Space, Neon City), or continue a run when you get hit. How long can you last?

### Controls
- PC: the blip sits right on your mouse cursor (arrow keys / WASD and controllers also work)
- Phone / tablet: put your thumb down anywhere for a joystick
- Esc or P: pause, M: mute

## How ads work in the game (for the QA team)
- **Midgame ad:** only when the player presses PLAY AGAIN after a run of at least 10 seconds, and never right after a rewarded ad. The SDK's own 3-minute spacing applies.
- **Rewarded ad:** "FREE CONTINUE" on the game-over card, once per run, only after a run of at least 15 seconds, with a 5-second window. The reward (continue with a 2-second shield) is given only on adFinished. There's always a non-ad option: continue for 15 gems.
- Game audio mutes on adStarted and comes back on adFinished/adError. The SDK muteAudio setting is respected.
- The game shows no banners and no custom fullscreen button.
- If ads are unavailable (Basic Launch or adblock), the FREE CONTINUE button disappears and the game plays normally.
