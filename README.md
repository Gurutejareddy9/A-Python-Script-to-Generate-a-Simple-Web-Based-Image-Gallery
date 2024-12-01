# ImageGalleryGenerator

Generate a simple web-based image gallery from a directory of images.

## Features:
- Automatically generates HTML for a basic image gallery
- Supports JPEG, PNG, GIF, and BMP image formats
- Customizable gallery title and image captions (using image file names by default)

## Requirements:
- Python 3.8+
- A directory containing your images (JPEG, PNG, GIF, BMP)

## Setup:
1. Clone the repository: `git clone https://github.com/Gurutejareddy9/ImageGalleryGenerator.git`
2. Navigate into the project directory: `cd ImageGalleryGenerator`
3. Place your images in the `images/` directory (create if it doesn't exist)

## Usage:
1. Run the script: `python gallery_generator.py`
2. Open the generated `gallery.html` in your web browser

## Customization:
- **Gallery Title:** Edit the `GALLERY_TITLE` variable in `gallery_generator.py`
- **Image Captions:** By default, uses image file names. For custom captions, create a `captions.txt` file in the `images/` directory with the format: `image_filename:Your Custom Caption`

## Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
