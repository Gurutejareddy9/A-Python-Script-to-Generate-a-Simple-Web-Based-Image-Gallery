import os

# Configuration
GALLERY_TITLE = "My Image Gallery"
IMAGE_DIR = "images/"
OUTPUT_FILE = "gallery.html"

def get_images(directory):
    """Return a list of image file paths."""
    image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp")
    return [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]

def get_captions(image_files, directory):
    """Return a dictionary of image files to their captions."""
    captions = {}
    try:
        with open(os.path.join(directory, "captions.txt"), "r") as file:
            for line in file.readlines():
                filename, caption = line.strip().split(":")
                captions[filename] = caption
    except FileNotFoundError:
        pass
    for file in image_files:
        if file not in captions:
            captions[file] = file
    return captions

def generate_gallery(images, captions, title, output_file):
    """Generate the HTML gallery."""
    html = f"<html><head><title>{title}</title></head><body>"
    html += f"<h1>{title}</h1><div class='gallery'>"
    for image in images:
        html += f"<figure><img src='{IMAGE_DIR}{image}' alt='{captions[image]}'><figcaption>{captions[image]}</figcaption></figure>"
    html += "</div></body></html>"
    with open(output_file, "w") as file:
        file.write(html)

def main():
    image_files = get_images(IMAGE_DIR)
    if not image_files:
        print("No images found in the directory.")
        return
    captions = get_captions(image_files, IMAGE_DIR)
    generate_gallery(image_files, captions, GALLERY_TITLE, OUTPUT_FILE)
    print("Gallery generated successfully. Open gallery.html to view.")

if __name__ == "__main__":
    main()