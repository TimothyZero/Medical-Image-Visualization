#  Copyright (c) 2020. The Medical Image Computing (MIC) Lab, 陶豪毅
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# -*- coding:utf-8 -*-

import os
import pickle
import sys

from medview import vtkShow
from vtkViewClass import vtkWindowView

# mode = '1'
mode = sys.argv[1]
print(mode)
if int(mode) == 1:
    loaded_data = pickle.load(open(os.path.dirname(__file__) + '/tmp.pkl', 'rb'))
    data, spacing = loaded_data['data'], loaded_data['spacing']
    vtkShow(data, spacing)
elif int(mode) == 2:
    loaded_data = pickle.load(open(os.path.dirname(__file__) + '/tmp.pkl', 'rb'))
    data, spacing = loaded_data['data'], loaded_data['spacing']
    vtkWindowView(data, spacing=spacing)
