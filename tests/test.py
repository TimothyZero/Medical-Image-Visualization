# -*- coding:utf-8 -*-
from medview import loadITK, vtkShowNotebook, vtkWindowViewNotebook


if __name__ == "__main__":
    import os

    data, dim, spacing, origin = loadITK(os.path.abspath(r'../sample/lung.nii.gz'))
    print(dim)
    print(spacing)
    print(origin)

    vtkShowNotebook(data, spacing)

    vtkWindowViewNotebook(data, spacing)
