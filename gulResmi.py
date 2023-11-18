import numpy as np
import cv2
resim = cv2.imread("gul.jpeg")
alt_kirmizi = np.array([0, 0, 100], dtype="uint8")
ust_kirmizi = np.array([100, 100, 255], dtype="uint8")
kirmizi_maske = cv2.inRange(resim, alt_kirmizi, ust_kirmizi)
sonuc = resim.copy()
mavi_pikseller = sonuc[kirmizi_maske > 0]
mavi_pikseller[:, 0] = 255
sonuc[kirmizi_maske > 0] = mavi_pikseller
siyah_arka_plan = np.zeros_like(resim)
siyah_arka_plan[kirmizi_maske > 0] = mavi_pikseller
cv2.imshow("Resmin Eski Hali",resim)
cv2.imshow("Resmin Yeni Hali", siyah_arka_plan)
cv2.waitKey(0)
cv2.destroyAllWindows()
