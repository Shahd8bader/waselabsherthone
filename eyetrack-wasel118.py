import cv2
import mediapipe as mp
import pyautogui 
cam = cv2.VideoCapture(0) # Initialize the webcam, and 0 for front camera

# Create a FaceMesh (3D) for face landmark detection
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True) 

screenWidth, screenHight = pyautogui.size() # Get the screen size
while True:
    _, frame = cam.read() # Read the frame
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)# Convert the frame to RGB
    output = face_mesh.process(rgbFrame) # Process the frame
    landmark_points = output.multi_face_landmarks # Get the landmark points
    frameHight, frameWidth, _ = frame.shape
    if landmark_points: 
        landmarks = landmark_points[0].landmark # Get the landmark points
        for id, landmark in enumerate(landmarks[474:478]): # Loop through the landmark points
            x = int(landmark.x * frameWidth) # Get the x coordinate
            y = int(landmark.y * frameHight) # Get the y coordinate 
            cv2.circle(frame, (x, y), 3, (0, 255, 0)) # Draw a circle
            if id == 1:
                screen_x = screenWidth * landmark.x # Get the x coordinate on the screen
                screen_y = screenHight * landmark.y # Get the y coordinate on the screen
                pyautogui.moveTo(screen_x, screen_y) # Move the mouse pointer
        right = [landmarks[145], landmarks[159]] # Get the right eye landmark points
        for landmark in right: # Loop through the right eye landmark points
            x = int(landmark.x * frameWidth) 
            y = int(landmark.y * frameHight)
            cv2.circle(frame, (x, y), 3, (0, 255, 255)) 
        if (right[0].y - right[1].y) < 0.004: # Check if the right eye is closed
            pyautogui.click() 
            pyautogui.sleep(1)
    cv2.imshow('وصل', frame)
    cv2.waitKey(1)