## CSC320 Winter 2017 
## Assignment 1
## (c) Kyros Kutulakos
##
## DISTRIBUTION OF THIS CODE ANY FORM (ELECTRONIC OR OTHERWISE,
## AS-IS, MODIFIED OR IN PART), WITHOUT PRIOR WRITTEN AUTHORIZATION 
## BY THE INSTRUCTOR IS STRICTLY PROHIBITED. VIOLATION OF THIS 
## POLICY WILL BE CONSIDERED AN ACT OF ACADEMIC DISHONESTY
##The command to copy and paste
##./viscomp.py --matting --backA ../test_images/tiny/flowers-backA.jpg --backB ../test_images/tiny/flowers-backB.jpg --compA ../test_images/tiny/flowers-compA.jpg --compB ../test_images/tiny/flowers-compB.jpg --alphaOut alpha.tif --colOut col.tif

##
## DO NOT MODIFY THIS FILE ANYWHERE EXCEPT WHERE INDICATED
##

# import basic packages
import numpy as np
import scipy.linalg as sp
import cv2 as cv

# If you wish to import any additional modules
# or define other utility functions, 
# include them here
import os
#########################################
## PLACE YOUR CODE BETWEEN THESE LINES ##
#########################################


#########################################

#
# The Matting Class
#
# This class contains all methods required for implementing 
# triangulation matting and image compositing. Description of
# the individual methods is given below.
#
# To run triangulation matting you must create an instance
# of this class. See function run() in file run.py for an
# example of how it is called
#
class Matting:
    #
    # The class constructor
    #
    # When called, it creates a private dictionary object that acts as a container
    # for all input and all output images of the triangulation matting and compositing 
    # algorithms. These images are initialized to None and populated/accessed by 
    # calling the the readImage(), writeImage(), useTriangulationResults() methods.
    # See function run() in run.py for examples of their usage.
    #
    def __init__(self):
        self._images = { 
            'backA': None, 
            'backB': None, 
            'compA': None, 
            'compB': None, 
            'colOut': None,
            'alphaOut': None, 
            'backIn': None, 
            'colIn': None, 
            'alphaIn': None, 
            'compOut': None, 
        }

    # Return a dictionary containing the input arguments of the
    # triangulation matting algorithm, along with a brief explanation
    # and a default filename (or None)
    # This dictionary is used to create the command-line arguments
    # required by the algorithm. See the parseArguments() function
    # run.py for examples of its usage
    def mattingInput(self): 
        return {
            'backA':{'msg':'Image filename for Background A Color','default':None},
            'backB':{'msg':'Image filename for Background B Color','default':None},
            'compA':{'msg':'Image filename for Composite A Color','default':None},
            'compB':{'msg':'Image filename for Composite B Color','default':None},
        }
    # Same as above, but for the output arguments
    def mattingOutput(self): 
        return {
            'colOut':{'msg':'Image filename for Object Color','default':['color.tif']},
            'alphaOut':{'msg':'Image filename for Object Alpha','default':['alpha.tif']}
        }
    def compositingInput(self):
        return {
            'colIn':{'msg':'Image filename for Object Color','default':None},
            'alphaIn':{'msg':'Image filename for Object Alpha','default':None},
            'backIn':{'msg':'Image filename for Background Color','default':None},
        }
    def compositingOutput(self):
        return {
            'compOut':{'msg':'Image filename for Composite Color','default':['comp.tif']},
        }
    
    # Copy the output of the triangulation matting algorithm (i.e., the 
    # object Color and object Alpha images) to the images holding the input
    # to the compositing algorithm. This way we can do compositing right after
    # triangulation matting without having to save the object Color and object
    # Alpha images to disk. This routine is NOT used for partA of the assignment.
    def useTriangulationResults(self):
        if (self._images['colOut'] is not None) and (self._images['alphaOut'] is not None):
            self._images['colIn'] = self._images['colOut'].copy()
            self._images['alphaIn'] = self._images['alphaOut'].copy()

    # If you wish to create additional methods for the 
    # Matting class, include them here

    #########################################
    ## PLACE YOUR CODE BETWEEN THESE LINES ##
    #########################################

    #########################################
            
    # Use OpenCV to read an image from a file and copy its contents to the 
    # matting instance's private dictionary object. The key 
    # specifies the image variable and should be one of the
    # strings in lines 54-63. See run() in run.py for examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # leave the matting instance's dictionary entry unaffected and return
    # False, along with an error message
    def readImage(self, fileName, key):
        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        #elif (not os.path.isfile(fileName)):
        #    success, msg = False, 'Invalid filename provided for ' + key
        
        if (not key in self._images): #valid key
            success, msg = False, 'Invalid key provided: ' + key
        elif (not os.path.isfile(fileName)):
            success, msg = False, 'Invalid filename provided: ' + fileName
        else:
            picture = cv.imread(fileName) #try to load picture
            if (type(picture) == None): #failed to load image
                success, msg = False, 'Failed to load image properly'                
            else: #load worked
                self._images[key] = picture
                success, msg = True, "Successfully loaded image"                
        
        print(success, msg)
        #########################################
        return success, msg

    # Use OpenCV to write to a file an image that is contained in the 
    # instance's private dictionary. The key specifies the which image
    # should be written and should be one of the strings in lines 54-63. 
    # See run() in run.py for usage examples
    #
    # The routine should return True if it succeeded. If it did not, it should
    # return False, along with an error message
    def writeImage(self, fileName, key):
        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
        data = self._images[key]
        if(key not in self._images):
            success, msg = False, 'Invalid key provided'
        elif (type(data) == None):
            success, msg = False, 'There is no data in key: ' + key + 'to write'
        else:
            cv.imwrite(fileName, data)
            success = True, 'Successfully wrote image'

        #########################################
        return success, msg

    # Method implementing the triangulation matting algorithm. The
    # method takes its inputs/outputs from the method's private dictionary 
    # ojbect. 
    def triangulationMatting(self):
        """
        success, errorMessage = triangulationMatting(self)
        
        Perform triangulation matting. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """
        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################

        #Create matrix A, from the equation Ax = b
        temp_matrix = np.eye(3,4)
        A = np.vstack((temp_matrix, temp_matrix))

        #Create matrix x
        deltaValues = np.zeros([6,4])

        #Get image information from dictionary
        compA = self._images['compA']
        compB = self._images['compB']
        backA = self._images['backA']
        backB = self._images['backB']

        #shape of images for init of result matrices
        x,y = backA.shape[0:2]
        
        #create result matrices, alpha and co
        self._images['colOut'] = np.zeros([x,y,3]) #RBG values at each index = 3
        self._images['alphaOut'] = np.zeros([x,y]) #only x and y since just a singular value alpha

        for i in range(x): #Rows
            for j in range(y): #Columns

                #Values at the index i, j
                c1 = compA[i,j].astype(np.float16)
                c2 = compB[i,j].astype(np.float16)

                b1 = backA[i,j].astype(np.float16)
                b2 = backB[i,j].astype(np.float16)

                A[0:3, 3] = -b1
                A[3:6, 3] = -b2

                deltaValues[0:3, 0] = c1 - b1
                deltaValues[3:6, 0] = c2 - b2
                
                inverse = np.dot(np.linalg.pinv(A), deltaValues)
                
                #keep the alpha values between 1 and 0
                inverse[3,0] = np.clip(inverse[3,0], 0.0, 1.0)

                
                #add result values to self._images
                self._images['colOut'][i, j] = inverse[:3,0]
                self._images['alphaOut'][i,j] = (255 * inverse[3,0])


        success, msg = True, 'Loaded alphaOut and colOut values'

        #########################################

        return success, msg

#./viscomp.py --compositing --alphaIn alpha2.tif --colIn col2.tif --backIn ../test_images/tiny/window.jpg --compOut comp2.jpg
    def createComposite(self):
        """
        success, errorMessage = createComposite(self)
        
        Perform compositing. Returns True if successful (ie.
        all inputs and outputs are valid) and False if not. When success=False
        an explanatory error message should be returned.
        """

        success = False
        msg = 'Placeholder'

        #########################################
        ## PLACE YOUR CODE BETWEEN THESE LINES ##
        #########################################
                
        #load up alphaIn, colIn, backIn
        alpha = self._images['alphaIn'].astype(np.float32)
        colour = self._images['colIn'].astype(np.float32)
        background = self._images['backIn'].astype(np.float32)
                
        #create composite result matrix 
        x,y = alpha.shape[0:2]
        composite = np.zeros([x, y, 3])    

        #check that colour and background images are same shape
        if(colour.shape != background.shape):
            success, msg = False, 'Error: colIn must be a color image of size equal to backIn'
            
        #check alpha is same size as colour and background
        elif((alpha.shape != colour.shape) or (alpha.shape != background.shape)):
            success, msg = False, 'Error: alphaIn size doesn\'t match size of backIn or colIn' 

        #implement the matting equation
        else:
            alphaData = (1 - (alpha / 255))
            composite = np.multiply(alphaData, background) + colour
            composite = composite.astype(np.float32)
            
            self._images['compOut'] = composite
            success, msg = True, 'Created composite'
        #########################################

        return success, msg


