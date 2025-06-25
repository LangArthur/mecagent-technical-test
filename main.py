#!/usr/bin/env python

# Please have a look to REFLECTIONS.md first

from datasets import load_dataset
ds = load_dataset("CADCODER/GenCAD-Code", num_proc=16, split=["train", "test"], cache_dir="./dataset")

print(ds[0])