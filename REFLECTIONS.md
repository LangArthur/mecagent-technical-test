# Reflections

## Problem

From image of a CAD model, generate the code associated with it.

## About the dataset

- images in 480x480
- associated code from 283b up to 8.1 kb

## Insights

creating a model from scratch would take too much time, so the idea is to get a first prototype with existing models.

### Insights 1

From the image, generate a text describing it, generate code with the given text + recommended (if possible) the image. -> multi-modal model
**Pros:**

- depending the finality of the model, it can be useful to be able to generate CAD code just from a description and not an image
- the text description can give more insights than just an image

**Cons:**

- might not be the goal of the test here
- too difficult to: research on it + set-up + training, in the time constraints

Insights 2
the task can be represented as a "describe the image" situation -> the model has an image as an input and should give it description, here not in plain english but in code.

**Pros:**

- simplify the process (compare to 1) with no visible trade-off
- models where able to learn English, they can learn CAD language

**Cons:**

- existing architectures might not fit code generation, since they are fine-tuned for text generation.

## Resources

Some resources which can be useful. The list is filled on the fly while I progress through the test:

- [Flamingo](https://github.com/mlfoundations/open_flamingo): Multimodal language model that can be used for a variety of tasks.
- [BLIP-2](https://github.com/salesforce/LAVIS/tree/5ee63d688ba4cebff63acee04adaef2dee9af207): Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models.
- [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl): opensource Multi-modal Large Language Model.
- [Flan-t5](https://huggingface.co/google/flan-t5-xxl): text generation (from the step image description -> code?).
- [DeepSeek-coder](https://github.com/deepseek-ai/DeepSeek-Coder): code generation based on a text (no official support for CAD :(. Not sure the dataset is enough )).

## Logs

- BLIP-2 dependencies are not compatible with the current environment (numpy versions). I did some tries by doing my own fork of BLIP-2, but I need to much time to find a solution. Considering switching to another model
- Testing briefly with Flamingo, but the data format seems . Considering to build a model from scratch finally.
- Try a demo of deepseek : seems convincing, investigating how to train a custom model for it.
- My GPU is not powerful enough to try the demo. I decide to write down the code of how I see the full workflow.