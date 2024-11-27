# pyWallpaper

**pyWallpaper** is a simple Python script that generates beautiful 4K gradient wallpapers with random colors. The script allows users to choose between a **dark** or **light** theme and adds subtle noise for texture. The generated wallpapers are saved in high-quality JPEG format and can be customized by the user.

## Features
- Generates 4K resolution gradient wallpapers (3840 x 2160)
- Options for **dark** or **light** themed gradients
- Randomized gradient colors for a unique look every time
- Adds subtle noise for a textured effect
- Saves wallpapers in optimized JPEG format to reduce file size

## Requirements
The script requires the following Python libraries:

- `numpy`
- `PIL` (Pillow)

### Install Dependencies
You can install the required dependencies using `pip`:

```bash
pip install numpy pillow
```

## Usage
1. Clone or download the script.
2. Run the script in a terminal or command prompt:

```bash
python pyWallpaper.py
```

3. Choose the **theme** by modifying the `theme` variable (`"dark"` or `"light"`).
4. The script will generate a wallpaper and save it in the `image` folder.
5. The script will ask if you'd like to regenerate the wallpaper.

### Example Output
- **Dark Theme**: Generates wallpapers with darker shades and smooth transitions.
- **Light Theme**: Generates wallpapers with brighter, lighter colors.

## Customization
- **Theme Selection**: Modify the `theme` variable to `"dark"` or `"light"` in the script.
- **Gradient Noise**: Adjust the `noise` level for more or less texture.
- **Image Quality**: Modify the `quality` parameter in `save()` to control JPEG compression (default: 90).

## Output Location
The generated wallpapers are saved in the `image` directory as `4k_fast_noise_gradient_wallpaper.jpg`.

## Example Code Snippet

```python
theme = "dark"  # Change to "light" for brighter wallpapers

# Random color selection based on the theme
if theme == "dark":
    color1 = np.random.randint(0, 100, size=(1, 1, 3))
    color2 = np.random.randint(0, 100, size=(1, 1, 3))
else:
    color1 = np.random.randint(155, 256, size=(1, 1, 3))
    color2 = np.random.randint(155, 256, size=(1, 1, 3))
```

## License
This project is released under the MIT License.

---

Feel free to reach out for any issues or suggestions. Happy wallpaper generating! 🎨
