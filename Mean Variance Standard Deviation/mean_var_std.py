import numpy as np

def calculate(list):
  if (len(list) == 9):
        
    b = np.array(list)
    
    d = np.zeros((3,3))
    i = 0
    
    for l in range(3):
      for c in range(3):
        d[l][c] = b[i]
        i += 1
     
    calculations = {
      'mean':[],
      'variance':[],
      'standard deviation':[],
      'max':[],
      'min':[],
      'sum':[]
    }
      
    calculations['mean'].append(np.mean(d, axis=0).tolist())
    calculations['mean'].append(np.mean(d, axis=1).tolist())
    calculations['mean'].append(np.mean(d).tolist())
    
    calculations['variance'].append(np.var(d, axis=0).tolist())
    calculations['variance'].append(np.var(d, axis=1).tolist())
    calculations['variance'].append(np.var(d).tolist())
    
    calculations['standard deviation'].append(np.std(d, axis=0).tolist())
    calculations['standard deviation'].append(np.std(d, axis=1).tolist())
    calculations['standard deviation'].append(np.std(d).tolist())
    
    calculations['max'].append(np.max(d, axis=0).tolist())
    calculations['max'].append(np.max(d, axis=1).tolist())
    calculations['max'].append(np.max(d).tolist())
      
    calculations['min'].append(np.min(d, axis=0).tolist())
    calculations['min'].append(np.min(d, axis=1).tolist())
    calculations['min'].append(np.min(d).tolist())
      
    calculations['sum'].append(np.sum(d, axis=0).tolist())
    calculations['sum'].append(np.sum(d, axis=1).tolist())
    calculations['sum'].append(np.sum(d).tolist())
    
    return calculations

  else:
    raise ValueError('List must contain nine numbers.')
  