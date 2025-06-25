# Reflections

## Problem

From image of a CAD model, generate the code associated with it.

## About the dataset

- images in 480x480
- associated code from 283b up to 8.1 kb

## Insights

### Insights 1

From the image, generate a text describing it, generate code with the given text + (recommended if possible) the image.
**Pros:**

- depending the finality of the model, it can be useful to be able to generate CAD code just from a description and not an image
- the text description can give more insights than just an image

**Cons:**

- might not be the goal of the test here
- too difficult to research on it + set-up + training in the time constraints

Insights 2
the task can be represented as a "describe the image" situation -> the model has an image as an input and should give it description, here not in plain english but in code.

**Pros:**

- simplify the process (compare to 1) with no visible trade-off
- models where able to learn English, they can learn CAD language

**Cons:**

- existing architectures might not fit code generation, since they are fine-tuned for text generation.
- I do not have time to create an architecture from scratch for this

Some resources which can be useful:

- [Flamingo](https://github.com/mlfoundations/open_flamingo): Multimodal language model that can be used for a variety of tasks.
- [BLIP-2](https://github.com/salesforce/LAVIS/tree/5ee63d688ba4cebff63acee04adaef2dee9af207): Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models.
