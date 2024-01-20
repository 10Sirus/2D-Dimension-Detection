import cv2
from google.colab.patches import cv2_imshow
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('/content/tip (1).jpg')


# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) 

# Blur the image to reduce high frequency noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edged = cv2.Canny(blurred, 30,150)

# Find contours in the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through each contour


for k in contours:

  length = cv2.arcLength(k, True)

if length> yo :
  yo= length
    


for c in contours:
    # Approximate the contour as a polygon
    approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)
    
  
    # draws boundary of contours.
    cv2.drawContours(image, [approx], 0, (0, 0, 255), 1) 
  
    # Used to flatten the array containing
    # the co-ordinates of the vertices.
    n = approx.ravel() 
    i = 0
    x=n[0]
    y=n[1]
  
    for j in n :
        if(i % 2 == 0):
          if i >=1:
         
            b= n[i]
            h= n[i+1]
            
            x1= (b+x)/2
            y1=(y+h)/2
      

            dist = math.hypot(b - x, h- y)
            x = n[i]
            y = n[i + 1]
  
            # String containing the co-ordinates.
            string= str(round(dist*p, 2))

            if len(approx) <= 10:
                # text on remaining co-ordinates.
               cv2.putText(image, string, (int(x1), int(y1)), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0)) 
        i = i + 1

    
    length = cv2.arcLength(c, True)
    
    p= 66.6/yo

    M = cv2.moments(c) 

    if M['m00'] != 0.0: 

        x = int(M['m10']/M['m00']) 

        y = int(M['m01']/M['m00']) 
    # Check the number of sides of the polygon
    if len(approx) == 3:
        # Triangle
        shape = "triangle"
    elif len(approx) == 4:
        # Rectangle or square
        # Check if the sides are approximately equal
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            shape = "square"
     

   else:
            shape = "rectangle"
    elif len(approx) == 5:
        # Pentagon
        shape = "pentagon"
    elif len(approx) == 6:
        # Hexagon
        shape = "hexagon"
    else:
        # Circle
        shape = "circle"
    # Draw the contour and label the shape on the image
    
    cv2.putText(image, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (100, 100, 0), 1)
   
    a= str(round(length*p, 2))
    cv2.putText(image, a, (x,y + 15), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (100, 100,0), 1)
  

# Show the image
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
