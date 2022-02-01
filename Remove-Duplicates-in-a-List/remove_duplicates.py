def remove_duplicates(elements, method='sets'):
  if method == 'sets':
    return list(set(elements))
  elif method == 'loop':
    array = []
    for ii, e in enumerate(elements[1:]):
      if e not in array:
        array.append(e)
    return array
  
if __name__ == "__main__":
  
  elements = [1,2,8,5,3,5,2,5,1,6,9,8,7,3,4,7]
  print(remove_duplicates(elements, method='loop'))
