# UBL Writing Day 2024 Prompt Engineering

> Input session on 2024-02-29, Leipzig University Library, [Martin
> Czygan](mailto:martin.czygan@gmail.com), software developer, author and data
> engineer

## About Me

* Software Developer at [Leipzig University
  Library](https://ub.uni-leipzig.de), Open Data Engineer at [Internet
Archive](https://archive.org), working on [Internet Archive
Scholar](https://en.wikipedia.org/wiki/Internet_Archive_Scholar) and [Citation Graphs](https://arxiv.org/abs/2110.06595)

[![](static/ia-scholar-hp.png)](https://scholar.archive.org)

* Misc: consultant,
  [author](https://scholar.google.com/citations?user=7gueY4EAAAAJ), open source
[contributor](https://github.com/miku), community
[organizer](https://golangleipzig.space/), former Lecturer at [Lancaster
University](https://www.lancasterleipzig.de/) Leipzig
* main "serious" topic, beside
  [haikus](https://golangleipzig.space/meetup-38-llm-haiku/meetup-38-llm-haiku.pdf),
is the conversion of unstructured data (e.g. "strings", "bytes") to structured data
(e.g. "metadata"), information retrieval
* previous talks: [NN tour](https://github.com/miku/nntour) (2016), [PyTorch tour](https://github.com/miku/pytorch-tour) (2018), [ML w/ Go](https://github.com/miku/mlgo) (2018), [cgosamples](https://github.com/miku/cgosamples) (2023), [local
  models](https://github.com/miku/localmodels) (2023)

## A growing genai ecosystem

* in the last 12 months, a number of closed and open models have been released (there is a [spectrum](https://arxiv.org/pdf/2302.04844.pdf))
* large number of tools around models (often just thin wrappers)
* dozens of [writing assistants](https://github.com/steven2358/awesome-generative-ai?tab=readme-ov-file#writing-assistants), more integrated with writing tasks (ideation, readability, grammar checks, summarization, ...)
* tools to help find snippets in your own documents, locally (maybe: better search)

For programming, there are coding assistants. They can help to draft and
explore (e.g. new languages), but programming involves [more
tasks](https://pages.cs.wisc.edu/~remzi/Naur.pdf) than just writing it down.

According to a case study of 150M LOC, code quality already [dropped in
2023](https://gwern.net/doc/ai/nn/transformer/gpt/codex/2024-harding.pdf). We
**need less code not more**, and the copilots currently work in the opposite
direction.

One important step is the proliferation of open models (e.g. Meta's
[llama](https://ai.meta.com/blog/large-language-model-llama-meta-ai/)) and
tools that allow to run an LLM on your own machine (most of these notes are
informed by experiments with local models).
