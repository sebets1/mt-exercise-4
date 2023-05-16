#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  Seraina Betschart
# date: 12.05.2023
# Machine Translation Exercise 4: Extract perplexities


def extract_logs(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as text:
        log_list=[]
        for line in text:
            list_raw = line.split(" ")
            list_clean = []
            for ele in list_raw:
                if len(ele)>1:
                    list_clean.append(ele)

            if "ppl:" in list_clean:
                n=list_clean.index("ppl:")
                log_value=list_clean[n+1]
                log_value=log_value[:-1]
                log_list.append(float(log_value))

    print(log_list)
    print(len(log_list))


    with open(output_file, "w", encoding="utf-8") as output:
        for value in log_list:
            output.write(str(value))
            output.write("\n")

extract_logs("baseline.log", "output_baseline.txt")
extract_logs("prenorm.log", "output_prenorm.txt")
extract_logs("postnorm.log", "output_postnorm.txt")
extract_logs("baseline_own_try.log", "output_baseline_own_try.txt")

# a=(12 if 6 ==6 else None)
# print(a)
# self.layer_norm = (nn.LayerNorm(hidden_size, eps=1e-6) if kwargs.get(
#             "layer_norm", "post") == "pre" else None)