import cv2
import json
from google.cloud import vision
from collections import OrderedDict
from google.oauth2 import service_account


class Reaction:

   def __init__(self, ramp_frames = 6):
      self.camera_port = 0
      self.ramp_frames = ramp_frames

   def _get_image(self):
      camera = None
      try:
         camera = cv2.VideoCapture(self.camera_port)
         for i in xrange(self.ramp_frames):
            camera.read()[1]
         camera_capture = camera.read()[1]
      except:
         return None
      finally:
         if camera:
            del(camera)
      return cv2.imencode('.jpg', camera_capture)[1].tostring()

   def get_mood(self):
      image = self._get_image()
      if not image:
         # camera in use or no camera
         return None
      credentials = service_account.Credentials.from_service_account_file('/home/apollo/Downloads/CP_VN-8c60f16ddaa8.json')
      client = vision.ImageAnnotatorClient(credentials=credentials)
      response = client.annotate_image({
         'image': {'content': image},
         'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],
      })
      if response:
         emotions = OrderedDict([("anger", 0), ("sorrow", 0), ("joy", 0), ("surprise", 0)])
         for face in response.face_annotations:
            emotions['joy'] = max(face.joy_likelihood, emotions['joy'])
            emotions['sorrow'] = max(face.sorrow_likelihood, emotions['sorrow'])
            emotions['anger'] = max(face.anger_likelihood, emotions['anger'])
            emotions['surprise'] = max(face.joy_likelihood, emotions['surprise'])
         top_emotion_enum = max(emotions.values())
         if top_emotion_enum <= 1:
            return None
         for emotion, val in emotions.items():
            if val == top_emotion_enum:
               return emotion
      return None


if __name__ == '__main__':
   print(Reaction().get_mood())

