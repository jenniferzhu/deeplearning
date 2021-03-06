import PIL, os, numpy as np, math, collections, cv2, threading, json, bcolz, random, scipy
import random, pandas as pd, pickle, sys, itertools, string, sys, re
import matplotlib.pyplot as plt, seaborn as sns
from abc import abstractmethod
from glob import glob, iglob
from concurrent.futures import ThreadPoolExecutor
from itertools import chain
from collections import Iterable, Counter

def in_notebook(): return 'ipykernel' in sys.modules

from tqdm import trange, tqdm, tqdm_notebook, tnrange
if in_notebook(): trange=tnrange; tqdm=tqdm_notebook