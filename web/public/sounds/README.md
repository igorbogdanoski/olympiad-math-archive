# Sound Effects for Quiz System

## Required Files

Place MP3 files in this directory:

- `click.mp3` - Short "pop" sound for answer selection (< 1 sec)
- `success.mp3` - Victory sound for quiz completion (~2 sec)
- `streak.mp3` - Fire sound for streak achievement (~1 sec)

## Recommended Sources

Free sound libraries:
- Pixabay.com/sound-effects
- Freesound.org
- Zapsplat.com

## File Requirements

- Format: MP3 (best browser compatibility)
- Size: < 50KB per file
- Duration: 0.5-2 seconds
- Volume: Normalized to -3dB

## Usage

Sounds are loaded in SoundManager and played via:
```javascript
SoundManager.play('click');
SoundManager.play('success');
SoundManager.play('streak');
```

## Testing Without Files

System will work without files (gracefully degrades). Console will show:
```
Audio autoplay blocked
```
This is expected until real MP3 files are added.
