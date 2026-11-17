# Blip Panic

Grab the gems. Dodge everything else.

A fast arcade dodge game in one HTML file, ported from the Roblox version. Steer your blip around the arena, collect 💎 gems and survive as the levels get harder: bouncing bubbles from level 1, zoomers from level 3, chasers from level 5.

![Gameplay](promo/shot-gameplay.png)

## Play
**[Play it in your browser](https://nvsscr.github.io/blip-panic/)** (PC, phone or tablet), or open `index.html` locally.

## Controls
| Device | How |
| --- | --- |
| Mouse | The blip follows your cursor |
| Phone / tablet | Drag anywhere to steer, or switch to a fixed joystick in the menu (landscape). ⛶ = fullscreen |
| Keyboard | Arrow keys or WASD |
| Controller | Left stick, A to select, Start to pause |
| Any | Esc / P pause, M mute |

## Scoring
+10 per second, +50 per gem. Gems buy blip skins, arena themes and a continue. Progress is saved in the browser.

## Build
```
python build.py
```
Makes `dist/blip-panic-itch.zip` for itch.io and other HTML5 game sites.
