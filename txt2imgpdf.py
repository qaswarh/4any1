from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_pdf_to_images(text_pdf):
    # Convert PDF to images (300 DPI)
    pages = convert_from_path(text_pdf, dpi=300)
    image_paths = []
    for i, page in enumerate(pages):
        image_path = f"page_{i + 1}.png"
        page.save(image_path, 'PNG')  # Save as PNG
        image_paths.append(image_path)
    return image_paths

def create_pdf_from_images(image_paths, images_pdf):
    # Create a new PDF using ReportLab
    c = canvas.Canvas(images_pdf, pagesize=letter)  # Use letter size (8.5x11 inches)

    for image_path in image_paths:
        # Calculate scaling to fit the image within the page
        image_width, image_height = 2550, 3300  # Image dimensions at 300 DPI
        page_width, page_height = letter  # Letter size in points (612x792 points at 72 DPI)

        # Scale image to fit within page dimensions
        scale_x = page_width / image_width
        scale_y = page_height / image_height
        scale = min(scale_x, scale_y)  # Use the smaller scale to fit within page

        # Compute margins to center the image
        margin_x = (page_width - (image_width * scale)) / 2
        margin_y = (page_height - (image_height * scale)) / 2

        # Draw image onto the page
        c.drawImage(image_path, margin_x, margin_y, width=image_width * scale, height=image_height * scale)
        c.showPage()  # Add a new page for each image

    c.save()

# Example usage
input_pdf = "packet_core_kt1.pdf"
output_pdf = "packet_core_kt.pdf"

# Convert PDF to images and create a new PDF from the images

images = convert_pdf_to_images(input_pdf)
create_pdf_from_images(images, output_pdf)
