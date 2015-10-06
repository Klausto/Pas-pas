#!/usr/bin/env python
import cv2
import os

# corresponds to the circle switch, this calculates an average of
# the three last pictures taken in the freemode.

def averager(cartoon):

  cursor = len(cartoon) - 1

  tmp = cartoon[cursor].copy()
  final = tmp.copy()
  if (cursor > 1):
    prev = cartoon[cursor - 1].copy()
    if (cursor > 2):
      pprev = cartoon[cursor - 2].copy()
      tmp = cv2.addWeighted(tmp, 0.3, pprev, 0.7, 0.0, tmp)
    tmp = cv2.addWeighted(tmp, 0.3, prev, 0.7, 0.0, tmp)

  final = cv2.addWeighted(final, 0.5, tmp, 0.5, 0.0, final)

  return final
