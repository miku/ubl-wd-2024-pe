# Notes

GPT4 has about 51x the size (1.76T parameters) of a (quantized) model
(llama-34B) that can run on a contemporary consumer GPU (20GB VRAM).

```
llava:34b-v1.6-q4_K_S                   787b2213f0db    20 GB   18 hours ago
```

Companies (most likely) uses
[H100](https://resources.nvidia.com/en-us-dgx-systems/ai-enterprise-dgx) HW w/
640GB total VRAM (10.2kW max).

## ELEMENTS of STYLE

```
$ curl -sL https://www.gutenberg.org/files/37134/37134-h/37134-h.htm | pup 'tr > td:nth-child(3) json{}' | jq -rc '.[] | .text' | grep -v null
Form the possessive singular of nouns by adding
In a series of three or more terms with a single conjunction, use a comma after each term except the last
Enclose parenthetic expressions between commas
Place a comma before a conjunction introducing a co-ordinate clause
Do not join independent clauses by a comma
Do not break sentences in two
A participial phrase at the beginning of a sentence must refer to the grammatical subject
Make the paragraph the unit of composition: one paragraph to each topic
As a rule, begin each paragraph with a topic sentence; end it in conformity with the beginning
Use the active voice
Put statements in positive form
Use definite, specific, concrete language
Omit needless words
Avoid a succession of loose sentences
Express co-ordinate ideas in similar form
Keep related words together
In summaries, keep to one tense
Place the emphatic words of a sentence at the end
```

Not too bad:

```
$ ollama run miku/wa-2
```

Text:

> This study identified challenges to cultural heritage adaptive reuse and solutions to overcome these challenges at multiple scales in the case study of Rijeka. The factors hampering heritage reuse were derived by content analysis of th
... e data collected through a stakeholder engagement workshop. Here, “stakeholder participation” refers to the process of involving the broad variety of actors of heritage reuse in producing the knowledge that informs the data collection.
...

Response:

> To improve clarity and adherence to "The Elements of Style," here's a revised
> version:

> This study pinpoints challenges to adaptive cultural heritage reuse, as well
> as solutions at various scales within Rijeka's case study. These hindrances
> were obtained through content analysis from data gathered in stakeholder
engagement workshops (stakeholders referring to the diverse group of actors
involved in Heritage Reuse).

> - Added "These" for clarity and cohesion with previous sentence, addressing
>   Rule 17: Use definite, specific, concrete language. Ensured a consistent
>   subject by adding "these." Improved flow as per Rules 8 & 9 (Use active
>   voice; Put
statements in positive form).
> - Defined stakeholder participation at the onset and replaced passive
>   construction with an alternative version that adheres to Rule 13: Use
>   definite, specific language.


