# UBL Writing Day 2024 Prompt Engineering

> Input session on 2024-02-29, Leipzig University Library, [Martin
> Czygan](mailto:martin.czygan@gmail.com), software developer, author and data
> engineer

## About Me

[![](static/Sanco_8001.png)](https://en.wikipedia.org/wiki/CP/M)

* Software Developer at [Leipzig University Library](https://ub.uni-leipzig.de)
* Open Data Engineer at [Internet Archive](https://archive.org), working on [Internet Archive Scholar](https://en.wikipedia.org/wiki/Internet_Archive_Scholar)
* Misc: consultant,
  [author](https://scholar.google.com/citations?user=7gueY4EAAAAJ), open source
[contributor](https://github.com/miku), community
[organizer](https://golangleipzig.space/), former Lecturer at [Lancaster
University](https://www.lancasterleipzig.de/) Leipzig
* curious about computers since about 1985 ([pic](https://en.wikipedia.org/wiki/CP/M) related), curious about machine learning since about [2011](http://web.archive.org/web/20110816035332/ai-class.com)
* fun fact: published first short story at age 17, the anthology is preserved at this library, but thankfully not findable through the catalog

## Perspective on "AI"

* usually only "ML"
* I'm working and testing out [open](https://arxiv.org/pdf/2302.04844.pdf) models, mostly - models for which the research and development process is (at least somewhat) documented

![Running Sosaka/Alpaca-native-4bit-ggml [9c1bb480] from 2023-03-21 on a 2018 laptop w/ i7-8550u CPU and w/o GPU, recorded 2023-04-19](static/578575.gif)

> But there is frustration in the science community over OpenAI's secrecy
> around how the model was trained and what data were used, and how GPT-4
> actually works. "All of these closed-source models, they are essentially dead
> ends in science," says [Sasha Luccioni](https://www.sashaluccioni.com/), a research scientist specializing in
> climate at HuggingFace, an open-source AI cooperative. --
> [GPT-4 IS HERE: WHAT SCIENTISTS THINK](http://www.hajim.rochester.edu/che/assets/pdf/gpt-4-is-here-what-scientists-think.pdf) (03/2023)

* main "serious" topic, beside
  [haikus](https://golangleipzig.space/meetup-38-llm-haiku/meetup-38-llm-haiku.pdf),
is the conversion of unstructured data (e.g. "strings", "bytes") to structured data
(e.g. "metadata")
* previous talks: [NN tour](https://github.com/miku/nntour) (2016), [PyTorch tour](https://github.com/miku/pytorch-tour) (2018), [ML w/ Go](https://github.com/miku/mlgo) (2018), [cgosamples](https://github.com/miku/cgosamples) (2023), [local
  models](https://github.com/miku/localmodels) (2023)

## Prompt Engineering

* the wikipedia article about [Prompt
  Engineering](https://en.wikipedia.org/wiki/Prompt_engineering) is not that
old, it first appeared in
[2021-10-20](https://en.wikipedia.org/w/index.php?title=Prompt_engineering&oldid=1050870205), a Wednesday
* I first used tweet [1599971348717051904](https://twitter.com/alexandr_wang/status/1599971348717051904) as a joke on 2022-12-12 during a intro to programming CS course

> [...] I am going to assert that Riley is the first Staff Prompt Engineer hired *anywhere*. [...]

* as of 2024-02-05, IA Scholar finds
  [2066](https://scholar.archive.org/search?q=%22prompt+engineering%22), Google
Scholar [about
10100](https://scholar.google.com/scholar?q=%22prompt+engineering%22)
publications about "prompt engineering"
* let's compress some of these learnings into the next 20 minutes

## Where does PROMPT come from?

* we use the term "PROMPT" ("Eingabeaufforderung") in computing for a long time, at least since [1973](https://dspinellis.github.io/unix-v3man/v3man.pdf), but surely for quite a bit longer (in operatings systems, games; the original [ELIZA paper](https://web.stanford.edu/class/cs124/p36-weizenabaum.pdf) from 1966 does not mention "prompt")
* what a language model does is to find a probable continuation of some input, e.g. prefix or prompt
* language models go back to 1980's, and the statistical nature of text has
  been researched since at least
[1913](http://www.alpha60.de/research/markov/DavidLink_AnExampleOfStatistical_MarkovTrans_2007.pdf)
(Markov) or also
[1951](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf) (Shannon)
* in 2024 there are "marketplaces" for "prompts" -- 'care about some "Stoic Wisdom For Modern Challenges" for $3.99 or "Social Media Strategy For Companies" for $2.99?

To illustrate, let's train a model and use to generate some text in 60 seconds.


## LLM

An LLM is so large, it learns patters, so that we do not need to encode every
NLP task seperately; there is an "instruct" style training (XXX: how), so it
can use text ("prompt") to steer output towards *some* direction.

> ["Language Models are Few-Shot Learners"](https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf), 2020, [Cited by 20138](https://scholar.google.com/scholar?q=Language+Models+are+Few-Shot+Learners)

## Patterns

* persona pattern, "act as X"

