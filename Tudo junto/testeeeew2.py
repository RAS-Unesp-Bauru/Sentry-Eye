
# USAGE
# python opencv_object_tracking.py
# python opencv_object_tracking.py --video dashcam_boston.mp4 --tracker csrt
# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

class Teste:
  def __init__(self):
    pass
  
  def inicia(self, coordenadas):
    #ACIONA O TRACKER O COLOCA ELE NA VARIÁVEL TRACKER
    tracker = cv2.TrackerKCF_create()

    #INICIALIZA O INITBB
    

    #PEGA REFERÊNCIA A WEBCAM
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    time.sleep(1.0)

    #INICIALIZA VARIÁVEL FPS
    #fps = None

    #COMEÇA OS LOOP DOS FRAMES

    while True:
      #PEGA O FRAME ATUAL
      initBB = coordenadas

      frame = vs.read()
      #CHEGOU NO FIM DA STREAM?
      if frame is None:
        break

      #DIMUNI A TELINHA PRA MELHOR FPS
      frame = imutils.resize(frame, width=500)
      (H, W) = frame.shape[:2]

      #SE O INIT ACHOU UM OBJETO...
      if initBB is not None:

        #PEGA A NOVA BOUNDING BOX
        (success, box) = tracker.update(frame)

        #VE SE O TRACKING FOI UM SUCESSO
        if success:
          (x, y, w, h) = [int(v) for v in box]
          cv2.rectangle(frame, (x, y), (x + w, y + h),
            (0, 255, 0), 2)
          print('X0: %f' % x)
          print('Y0: %f' % y)
          print('X1: %f' % (x+w))
          print('Y1: %f' % (y+w))

        #UPDATE NO FPS
        #fps.update()
        #fps.stop()

        #INICIALIZA AS INFORMAÇÕES QUE SERÃO MOSTRADAS NA TELA
        info = [
          #("Tracker", args["tracker"]),
          ("Success", "Yes" if success else "No"),
          #("FPS", "{:.2f}".format(fps.fps())),
        ]

        #DESENHA
        for (i, (k, v)) in enumerate(info):
          text = "{}: {}".format(k, v)
          cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)


      #MOSTRA O FRAME DE SAIDA
      # show the output frame
      cv2.imshow("Frame", frame)
      key = cv2.waitKey(1) & 0xFF


      # APERTAR S PARA SELECIONAR O TARGET
      # ENTER PARA SALVAR

      if key == ord("s"):
        initBB = coordenadas

        # STARTA O PROGRAMA COM AS COORDENADAS E FPS
        tracker.init(frame, initBB)
        #fps = FPS().start()

      # ‘Q’ PARA DAR RAGE QUIT
      if key == ord("q"):
        break

    vs.stop()
    cv2.destroyAllWindows()