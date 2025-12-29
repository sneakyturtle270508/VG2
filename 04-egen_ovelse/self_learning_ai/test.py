# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-12-05 09:08:27
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-12-05 12:11:00
import json
import os
import random

class EnglishLearningAgent:
    def __init__(self, model_file="english_model.json"):
        self.model_file = model_file
        self.data = {}  # {"input": {"output1": count1, "output2": count2, ...}}
        self.load_model()

    def train_from_json(self, json_file):
        with open(json_file, 'r', encoding="utf-8") as f:
            training_data = json.load(f)
        for entry in training_data:
            inp = entry['input']
            out = entry['output']
            if inp not in self.data:
                self.data[inp] = {}
            if out not in self.data[inp]:
                self.data[inp][out] = 0
            self.data[inp][out] += 1
        self.save_model()

    def respond(self, inp):
        if inp in self.data:
            outputs = self.data[inp]
            total = sum(outputs.values())
            probs = [count/total for count in outputs.values()]
            return random.choices(list(outputs.keys()), probs)[0]
        return "I don't know yet."

    def save_model(self):
        with open(self.model_file, 'w', encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def load_model(self):
        if os.path.exists(self.model_file):
            with open(self.model_file, 'r', encoding="utf-8") as f:
                self.data = json.load(f)


# ---------------------------
if __name__ == "__main__":
    agent = EnglishLearningAgent()

    # Example: train from JSON
    agent.train_from_json("english_training_data.json")

    # Test
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        print("Agent:", agent.respond(inp))
