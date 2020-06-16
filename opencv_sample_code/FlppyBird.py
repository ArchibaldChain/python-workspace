import cv2
import random
import math

project_str = "I:/Programming/Cpp_workspace/CppLearningCode/CppAssignment/opencv_test/sample_code/pictures/"
bird1 = project_str + "bird1.png"
bird2 = project_str + "bird2.png"
bird3 = project_str + "bird3.png"
tub1 = project_str + "tubeup.png"
tub2 = project_str + "tubedown.png"


class FlppyBird:
    def __init__(self, frame):
        self.Tubes = []
        self.f_height = frame.shape[0]
        self.f_length = frame.shape[1]
        n = 6
        self.upperBound = int(frame.shape[0]/n)
        self.lowerBound = int(frame.shape[0]/n*(n-1))

        # Get bird pic
        b1 = cv2.imread(bird1)
        b1 = cv2.resize(b1, (2*b1.shape[0], 2*b1.shape[1]))
        b2 = cv2.imread(bird2)
        b2 = cv2.resize(b2, (2*b2.shape[0], 2*b2.shape[1]))
        b3 = cv2.imread(bird3)
        b3 = cv2.resize(b3, (2*b3.shape[0], 2*b3.shape[1]))
        self.bird = [b1, b2, b3]

        self.tube_wide = self.f_length/15  # self.tub1.shape[0]
        self.gate_size = self.f_height/4

        # Get tube pic
        newsize = (self.tube_wide, int(frame.shape[1] / 2))
        self.tub1 = cv2.resize(cv2.imread(tub1), newsize)
        self.tub2 = cv2.resize(cv2.imread(tub2), newsize)

        self.count = 0  # shows the times I call setTubes

    def setTubes(self, frame):
        self.count += 1
        if self.Tubes == []:
            g = self.generateGate()
            self.Tubes.append(g)
            return frame

        for t in self.Tubes:
            frame = self.drawTube(t, frame)
            t.moveLeft()

        # when the first one from the right enter into the frame
        if self.f_length - self.Tubes[-1].x2 > 4*self.tube_wide:
            g = self.generateGate()
            self.Tubes.append(g)

        # when the first one fromt the left completely hided.
        if self.Tubes[0].x2 <= 0:
            del(self.Tubes[0])

        return frame

    def drawBird(self, frame, center):
        bird = self.bird[self.count % 3]
        LeftUp = (center[0] - bird.shape[1], center[1] - bird.shape[0])
        imgCopy(frame, bird, LeftUp)

    def isOver(self, center_point, width, height):
        for t in self.Tubes:
            if t.isCrashed(center_point, width, height) is True:
                return True
        return False

    def drawTube(self, t, frame):
        a, b = t.getUpTube()
        cv2.rectangle(frame, a, b, (255, 255, 255), 2)
        # leftUp = (b[0] - self.tub1.shape[1], b[1] - self.tub2.shape[0])
        # imgCopy(frame, self.tub1, leftUp)

        a, b = t.getLowTube(self.f_height)
        cv2.rectangle(frame, a, b, (255, 255, 255), 2)
        # imgCopy(frame, self.tub2, a)
        return frame

    def generateGate(self):
        y = random.randint(self.upperBound, (self.lowerBound - self.gate_size))
        x = self.f_length
        return Gate(x, y, x+self.tube_wide, y + self.gate_size)

    def imgCopy(self, dsn_Image, mask, leftUp):
        for row in range(mask.shape[0]):
            for col in range(mask.shape[1]):
                isOutRange = row+leftUp[1] < 0 or\
                    row+leftUp[1] >= dsn_Image.shape[0] or\
                    col+leftUp[0] < 0 or\
                    col+leftUp[0] >= dsn_Image.shape[1]
                if sum(mask[row][col]) == 0 or isOutRange:
                    continue
                dsn_Image[row + leftUp[1], col + leftUp[0]] = mask[row, col]


class Gate:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getGateCordinate(self):
        return (self.x1, self.y1), (self.x2, self.y2)

    def getUpTube(self):
        return (self.x1, 0), (self.x2, self.y1)

    def getLowTube(self, m):
        return (self.x1, self.y2), (self.x2, m)

    def moveLeft(self):
        steplen = 5
        self.x1 -= steplen
        self.x2 -= steplen

    def isCrashed(self, center, width, height):
        if center[1]-height/2 < self.y1 or center[1] + height/2 > self.y2:
            if center[0]+width/2 < self.x2 and center[0]-width/2 > self.x1:
                return True
        return False


def imgCopy(dsn_Image, mask, leftUp):
    for row in range(mask.shape[0]):
        for col in range(mask.shape[1]):
            isOutRange = row+leftUp[1] < 0 or\
                row+leftUp[1] >= dsn_Image.shape[0] or\
                col+leftUp[0] < 0 or\
                col+leftUp[0] >= dsn_Image.shape[1]
            if sum(mask[row][col]) == 0 or isOutRange:
                continue
            dsn_Image[row + leftUp[1], col + leftUp[0]] = mask[row, col]
