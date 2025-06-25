#!/usr/bin/env python

# Please have a look to REFLECTIONS.md first

from datasets import load_dataset

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from metrics.valid_syntax_rate import evaluate_syntax_rate_simple
from metrics.best_iou import get_iou_best

# Generate CAD code from image description
#
# Example of expected input
# ```
# deep_seek_code_completion("A cube located in the middle of the image")
# ```
def text_to_cav(inputs):
    result = []
    for input in inputs:
        # FIXME: this should use the newly trained model
        tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-Coder-V2-Lite-Base", trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-Coder-V2-Lite-Base", trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
        preface_code = "In CAD language, please write the code for "
        inputs = tokenizer(preface_code + input, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_length=128)
        result.append(tokenizer.decode(outputs[0], skip_special_tokens=True))
    result

# return the description of the image
def describe_images(image):
    pass

def main():
    ds = load_dataset("CADCODER/GenCAD-Code", num_proc=16, split=["train", "test"], cache_dir="./dataset")
    print(ds)

    # Training
    descriptions = describe_images(ds[0]['image'])

    # Evaluation
    descriptions = describe_images(ds[1]['image'])
    cav = text_to_cav(descriptions)

    vsr = []
    iou = []
    for (i, code) in enumerate(cav):
        ground_truth = ds[1]['cadquery'][i]
        vsr.append(evaluate_syntax_rate_simple(code))
        iou.append(get_iou_best(code, ground_truth))

    print("Valid Syntax Rate:", vsr)
    print("IOU:", iou)
    return 0

if __name__=="__main__":
    main()