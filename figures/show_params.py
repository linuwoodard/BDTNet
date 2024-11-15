import numpy as np
import matplotlib.pyplot as plt
import cv2

ax = 56.5
ay = 49

x0, y0 = 106, 252

np.random.seed(8)  # Set seed for reproducibility

# Function to create a vector field with arrow positions and directions
def create_vector_field(shape):
    # Define a random center of arrows within the image bounds
    num_arrows = 11*18  # Specify how many arrows you want to draw

    # Generate X coordinates
    x = []  # Creating an empty list for x-coordinates
    for i in range(11):
        # Concatenate the calculated positions
        x_segment = ax * np.arange(18) + ax / 2 * (i % 2)
        for item in x_segment:
            x.append(item)
    x = x0 + np.array(x)  # Converting list to array and adding x0
    print(x)
    # Generate Y coordinates
    y = []  # Creating an empty list for y-coordinates
    for i in range(11):
        y_segment = [ay * i] * 18  # Repeat the y-coordinate for each segment
        y.extend(y_segment)         # Use extend to add to the list
    y = y0 + np.array(y)          # Convert to numpy array and add y0
    print(y)

    dx = np.random.normal(0, 10, num_arrows)  # Change in x
    for i in range(11):
        dx[i*18] = 0
    dy = np.random.normal(0, 10, num_arrows)  # Change in y
    return x, y, dx, dy

# Load an image
def load_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    # Convert from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# Plot arrows on the image
def plot_arrows_on_image(image, x, y, dx, dy):
    plt.imshow(image)  # Plot the image

    for i in range(len(x)):
        # Calculate starting point and direction
        start = (x[i], y[i])
        end = (x[i] + dx[i], y[i] + dy[i])
        
        # Draw the arrow
        plt.arrow(start[0], start[1], dx[i], dy[i], 
                  head_width=5, head_length=7, fc='r', ec='r')
    
    plt.axis('off')  # Hide axes
    plt.savefig(r'figures\BDT_mechanical_annotated.png', dpi=300, bbox_inches='tight')
    plt.show()

# Main execution
if __name__ == '__main__':
    image_path = r'figures\BDT_mechanical.png'  # Provide the path to your image here
    image = load_image(image_path)           # Load the image
    x, y, dx, dy = create_vector_field(image.shape[:2])  # Generate arrow positions and directions
    plot_arrows_on_image(image, x, y, dx, dy)  # Plot image with arrows