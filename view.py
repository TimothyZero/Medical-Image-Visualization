import os
import pickle
import sys

from medview import vtkShow, vtkWindowView, loadITK

data, dim, spacing, origin = loadITK(sys.argv[1])
print(sys.argv[1])
print(data.shape)
mode = 2
if int(mode) == 1:
    # loaded_data = pickle.load(open(os.path.dirname(__file__) + '/tmp.pkl', 'rb'))
    # data, spacing = loaded_data['data'], loaded_data['spacing']
    vtkShow(data, spacing=spacing)
elif int(mode) == 2:
    # loaded_data = pickle.load(open(os.path.dirname(__file__) + '/tmp.pkl', 'rb'))
    # data, spacing = loaded_data['data'], loaded_data['spacing']
    vtkWindowView(data, spacing=spacing)