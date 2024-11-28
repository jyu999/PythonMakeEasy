# This is a very simple script to find same pixel in an image. Still working on. not yet tested.
# 
from PIL import Image
from typing import List
import copy

img = Image.open(f'./operation/sample1.jpg', 'r')

match_point_lst = []  ## Used to store match point list

def build_pixel_match_matrix() -> List[List[int]]:
  img_matrix = [[0 for x in range(img.width)] for y in range(img.height)] 
  for x in range(img.width):
    for y in range(img.height):
      coordinate = x, y = x, y
      pixel = img.getpixel(coordinate)
      img_matrix[x][y] = pixel
      
      # if color == whatever put in match lst
      match_point_lst.append(x + "," + y)
      # Or think 1 as the color wanted, 0 as not color wanted populate img_matrix
      # if match
      img_matrix[x][y] = 1
      match_point_lst.append[(x,y)]
      #else
      img_matrix[x][y] = 0
  return img_matrix


def check_north_neighbor(im, i: int, j: int, ret: int) -> int:
  if j > 0:
    if im[i][j] == im[i][j-1] and im[i][j] == 1 :
      ret += 1
      match_lst.remove((i, j-1))      
  else:
    return ret

def check_west_neighbor(im, i: int, j: int, ret: int) -> int:
  if i > 0 :
    if im[i][j] == im[i-1][j] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i, j-1))       
  else:
    return ret

def check_south_neighbor(im, i: int, j: int, ret: int, max_height: int) -> int:
  if j < max_height -1 :
    if im[i][j] == im[i][j+1] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i, j-1))     
  else:
    return ret

def check_east_neighbor(im, i: int, j: int, ret: int, max_width: int) -> int:
  if i < max_width -1 :
    if im[i][j] == im[i+1][j] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i, j-1)) 
  else:
    return ret
  
def check_south_east_neighbor(im, i: int, j: int, ret: int, max_width: int, max_height: int) -> int:
  if i < max_width -1 and j < max_height -1:
    if im[i][j] == im[i+1][j+1] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i+1, j+1)) 
  else:
    return ret
  
def check_north_west_neighbor(im, i: int, j: int, ret: int) -> int:
  if i > 0 and j > 0:
    if im[i][j] == im[i-1][j-1] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i-1, j-1)) 
  else:
    return ret

def check_north_east_neighbor(im, i: int, j: int, ret: int, max_width: int) -> int:
  if i < max_width -1 and j > 0:
    if im[i][j] == im[i+1][j-1] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i+1, j+1)) 
  else:
    return ret
  
def check_south_west_neighbor(im, i: int, j: int, ret: int, max_height: int) -> int:
  if i > 0  and j < max_height -1:
    if im[i][j] == im[i-1][j+1] and im[i][j] == 1:
      ret += 1
      match_lst.remove((i-1, j+1)) 
  else:
    return ret


  
img_matrix = build_pixel_match_matrix()
match_lst = copy.copy(match_point_lst)
for xy_tuple in match_point_lst:
  count = check_north_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], 0)
  count = check_south_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count, img.height)
  count = check_west_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count)
  count = check_east_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count, img.width)
  count = check_north_west_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count)
  count = check_south_east_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count, img.width, img.height)
  count = check_north_east_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count, img.width)
  count = check_south_west_neighbor(img_matrix, xy_tuple[0], xy_tuple[1], count, img.height)
  print("{xy_tuple} ,  {count}")

