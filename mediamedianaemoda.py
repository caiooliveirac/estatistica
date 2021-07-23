arr = list(map(int,input().rstrip().split(' ')))
def media():
    media = sum(arr)/len(arr)
    return media

def mediana():
    if len(arr) % 2 == 0:
      elem1 = sorted(arr)[len(arr)//2]
      elem2 = sorted(arr)[(len(arr)//2)-1]
      return (elem1 + elem2)/2
    else:
      mediana = sorted(arr)[len(arr)//2]
      return mediana

def moda():
  return max(arr,key=arr.count)     

def stats():
    a = media()
    b= mediana()
    c = moda()
    print(round(a,2))
    print(round(b,2))
    print(c)
    
    
if __name__ == '__main__':
    stats()
