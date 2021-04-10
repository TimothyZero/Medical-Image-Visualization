# -*- coding:utf-8 -*-
import SimpleITK as sitk


def loadITK(file_path):
    data = sitk.ReadImage(file_path)  # xyz order
    dim = data.GetDimension()
    spacing = tuple(reversed(data.GetSpacing()))  # xyz => zyx
    origin = tuple(reversed(data.GetOrigin()))  # xyz => zyx
    data = sitk.GetArrayFromImage(data)  # => zyx
    return data, dim, spacing, origin