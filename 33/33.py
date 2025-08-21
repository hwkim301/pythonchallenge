from PIL import Image
from collections import Counter
from math import sqrt

img = Image.open("beer2.png")
print(img.mode)  # L
print(img.size)  # (138,138)

pixel_data = list(img.getdata())

pixel_counts = Counter(pixel_data)

sorted_brightness_levels = sorted(pixel_counts.keys())

cumulative_pixel_count = 0
# 3. Loop through the sorted brightness levels, not the full pixel list.
for level in sorted_brightness_levels:
    # Add the number of pixels at the current brightness level
    cumulative_pixel_count += pixel_counts[level]

    n = sqrt(cumulative_pixel_count)

    # 4. Perform the same perfect square check
    if n > 0 and n.is_integer():
        n_int = int(n)
        print(f"perfect square: {n_int}x{n_int} pixels at brightness level <= {level}")

        # 5. Only create the image data when a match is found
        # This is much more efficient than doing it in every loop.
        img_data = [p for p in pixel_data if p <= level]

        new_img = Image.new(img.mode, (n_int, n_int))
        new_img.putdata(img_data)
        new_img.save(f"img_{n_int}.png")
