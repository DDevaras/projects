import cv2

img_file = 'Car image.jpg'
video = cv2.VideoCapture('Insert Name of Car video.mp4')
video = cv2.VideoCapture('Insert Name of Pedestrians video.mp4')

# Our pre-trained car and pedestrian classifiers
car_tracker_file = 'car_detector.xml'
pedestrian_tracker_file = 'haarcascade_fullbody.xml'


#Create car classifier
car_tracker = cv2.CascdeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)


#Run forver until car stops or something
while True:

    # Read the current frame, Reads a single frame from the cv2.VideoCapture video after implementing that code. Frame is the image from vdieo
    (read_successful, frame) = video.read()

    #Safe coding
    if read_successful:
        #Must convert to grayscale
        grayscaled_frame = cv2.cvt.Color(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    #Below code is an array of the different coordinates of the cars
    #detect cars AND predestrians, detects all Cars and Pedestrians regardless of scale 
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    
    # Draw rectangles around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x+1, y+2), (x+w, y+h), (255, 0, 0), 2)
        #Below code is red color 2 thickness
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #Draw rectangles around the Pedestrians
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Display the image with faces spotted
    cv2.imshow('Clever Programmer Car Detector', grayscaled_frame)

     
    #Dont autoclose (wait for key press)
    cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key==113:
        break

# Release the VideoCapture object:
video.release()




print("Code Complete")
