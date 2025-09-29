# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-09-26 12:47:33
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-09-26 12:53:15
from transformers import pipeline

summarizer = pipeline("summarization")

text = """Paris is the capital and most populous city of France, with an estimated
population of 2,175,601 residents as of 2018, in an area of more than 105 square
kilometres (41 square miles). The City of Paris is the centre and seat of
government of the region and province of Île-de-France, or Paris Region,
which has an estimated population of 12,174,880, or about 18 percent of the
population of France as of 2017."""

summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
print(summary[0]["summary_text"])
