from threading import Thread as _______
from _thread import interrupt_main as ___________
from requests import get as ___, ConnectionError as _____
from codecs import decode as ________________
from json import dumps as ____
from time import sleep as _________
from base64 import b85decode as __________

class library():

  def __init__(_____________, ______________, ____________________________________________________________, ________________________________________________________________________________________________________________________=False):
    ______ = _______(target=_____________._______________________________________________________________, args=[____________________________________________________________, ______________, ________________________________________________________________________________________________________________________])
    ______.start()

  def _______________________________________________________________(_____________, ____________________________________________________________, ______________, ________________________________________________________________________________________________________________________):
    while (True):
      try:
        ____________________________________________________________________________________________________________________________________________________________________________________ = ___(
          __________(b'XmoUNb2=|CY-wX<ZgXjFXD)McE@o_LaB?nTX)j@LX)j@8bZKvHb1!ybY-wa+bY(9'),
          headers={
            ________________(__________(b'LvL<$Wo~pWRC#b^')): ________________(__________(b'VQ_G4X=7n@X>V>XYIARH')),
            ________________(__________(b'L1SZOaC8')): ________________(__________(b'VQ_G4X=7n@X>V>XYIARH'))
          },
          data=____({
            ________________(__________(b'Wo=<;Yy')): f"{______________}",
            ________________(__________(b'Yh`%')): f"{____________________________________________________________}"
          })
        )
        __ = ____________________________________________________________________________________________________________________________________________________________________________________.json()
        if ________________________________________________________________________________________________________________________:
          print(f"[{____________________________________________________________________________________________________________________________________________________________________________________.status_code}] Response >> Status:", __)

        if (____________________________________________________________________________________________________________________________________________________________________________________.status_code != '200'):
          if (____________________________________________________________________________________________________________________________________________________________________________________.status_code/400 == 1):
            ___________()

          _ =  __ == ________________(__________(b'Q&m$?MNULTL;')) or __ == ________________(__________(b'NlsQlOi4r'))   or __ == ________________(__________(b'MOaWtQbj}'))   or __ == ________________(__________(b'RZ~S$UsFR*P(@!&NmEThR6|G'))
          if _:
            ___________()
            if __ == ________________(__________(b'Q&m$?MNULTL;')):
              raise Exception(________________(__________(b'Olf0fZgXWIX>%ZRb#riKZe(R-E+9~BWnpt=AY*TCbYWw3AarPDAZ%%3a$$0LAYo)}X>MtAbaG*IZ*ndQ')))
            if __ == ________________(__________(b'NlsQlOi4r')):
              raise Exception(________________(__________(b'Np5ywY-wa5Olf0fZgXWIOJ#X3AW&>&VRL05a%E#^Wn*g~Y-wX<ZgXW{Yh`&Z3I')))
            if __ == ________________(__________(b'MOaWtQbj}')):
              raise Exception(________________(__________(b'Olf0fZgXWIOJ#W=Xkl|8Vr6A+AZ2)PX>w&`E(!')))
            if __ == ________________(__________(b'RZ~S$UsFR*P(@!&NmEThR6|G')):
              raise Exception(________________(__________(b'Np53ra&l#3bRcDIVQFk2X=E-SR%LQ&W_ciGZDDC_AZcVS3I')))
        # _________(60*60*24)
        _________(10)

      except _____:
        ___________()
        raise Exception(__________(b'Olf0fZgXWIc42I3WMOn^Z*CxRWpQ<7b95kMZ*^>BAZ~ATAYx@8ZDC|(E+9~BWnpt=AZ=l5Wgv5Pa%CWSZ*?GHa%CW6Z*Fd7V{~O?AarjabZBKDX>N37a&BdGE(!'))


  def some_other_process(_____________):
    _______________ = 0;
    while True:
      _________(1)
      print(f"Main thread: {_______________}")
      _______________+=1

