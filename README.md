# UBL Writing Day 2024 Prompt Engineering

> Input session on 2024-02-29, Leipzig University Library, [Martin
> Czygan](mailto:martin.czygan@gmail.com), software developer, author and data
> engineer

## About Me

* Software Developer at [Leipzig University
  Library](https://ub.uni-leipzig.de), Open Data Engineer at [Internet
Archive](https://archive.org), working on [Internet Archive
Scholar](https://en.wikipedia.org/wiki/Internet_Archive_Scholar)

[![](static/ia-scholar-hp.png)](https://scholar.archive.org)

* Misc: consultant,
  [author](https://scholar.google.com/citations?user=7gueY4EAAAAJ), open source
[contributor](https://github.com/miku), community
[organizer](https://golangleipzig.space/), former Lecturer at [Lancaster
University](https://www.lancasterleipzig.de/) Leipzig
* curious about computers since about 1985, about machine learning since about [2011](http://web.archive.org/web/20110816035332/ai-class.com)

## What is Prompt Engineering?

> A prompt is an input, a text command or a question provided to an AI model,
> to generate **desired output** like content or answer. The process of crafting
> effective and efficient prompts is called prompt design or prompt
> engineering. -- [Azure ML docs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-retrieval-augmented-generation?view=azureml-api-2)

And why is it important?

* a new, yet to be fully understood human-computer-interaction (HCI)
* better use of the machine, better understanding of its limits

## Why does it exist?

* the wikipedia article about [Prompt
  Engineering](https://en.wikipedia.org/wiki/Prompt_engineering) is not that old, it first appeared in
[2021-10-20](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&oldid=1050870205), a Wednesday
* related tweet: [1599971348717051904](https://twitter.com/alexandr_wang/status/1599971348717051904) (I used as a joke on 2022-12-12 during an intro to programming CS class)

These language models learn are META-LEARNERS:

> language models can also be understood as meta-learners where slow
outer-loop gradient descent based learning is combined with **fast "in-context"
learning implemented within the context activations of the model** -- [Language Models are Few-Shot Learners](https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf)

This is new and only observed in larger models. We not only want a distribution over words, but words and tasks.

> Learning to perform a single task can be expressed in a
probabilistic framework as estimating a conditional distribution
`p(output|input)` . Since a general system should be able to perform many
different tasks, even for the same input, **it should condition not only on the
input but also on the task to be performed**. That is, it should model
`p(output|input, task)`. -- [Language Models are Unsupervised Multitask Learners](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

<!-- ![](static/data-to-pe.png) -->

![The LLM iceberg](static/8gfpvm.jpg)

## In-context learning

> Crucially, in-context learning happens only at inference time without any
> parameter updates to the model.

Context-window refers to the number of words (or tokens) the model is able to
take into account (gpt-2: 1024, llama2: 4096, ...)

Examples:

```
maison: house
chat: cat
dog: ...
```

How much of that in context learning is actually learning (not remembering)?
Cf. [What Can Transformers Learn In-Context? A Case Study of Simple Function
Classes](https://arxiv.org/pdf/2208.01066.pdf), or [Prompt Programming for
Large Language Models: Beyond the Few-Shot
Paradigm](https://arxiv.org/pdf/2102.07350.pdf)

> Rather than instruction, the method’s primary function is task location in
> the model's existing space of learned tasks. This is evidenced by the
> effectiveness of alternative prompts which, with no examples or instruction,
> can elicit comparable or superior perfor- mance to the few-shot format.

What affects in-learning performance? Cf. [Rethinking the Role of
Demonstrations: What Makes In-Context Learning
Work?](https://arxiv.org/pdf/2202.12837.pdf)

> Despite in-context learning consistently outperforming zero-shot inference on
> a wide range of tasks, there is little understanding of how it works and
> which aspects of the demon- strations contribute to end task performance

One finding was that
