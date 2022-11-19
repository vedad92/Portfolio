from ast import arguments
from random import random
from helpers import random_koala_fact

if __name__ == "__main__":
    print(random_koala_fact())


def unique_koala_facts(argument):
    facts_list = []
    i = 1000
    while i > 0 and len(facts_list) < argument:
        total_list = random_koala_fact()
        if total_list not in facts_list:
            facts_list.append(total_list)
        i -= 1
        if len(facts_list) == argument:
            print(facts_list)
            break
    return facts_list


print(unique_koala_facts(5))


def num_joey_facts():
    fact_count = 0
    joey_facts = []

    while fact_count <= 1000:
        fact_count += 1
        random_fact = random_koala_fact()
        if "joey" in random_fact:
            if random_fact not in joey_facts:
                joey_facts.append(random_fact)
    return len(joey_facts)


print(num_joey_facts())


def koala_weight():
    koala_weight_fact = []

    i = 0
    while i <= 1000:
        i += 1
        random_fact = random_koala_fact()
        if "kg" in random_fact:
            if random_fact not in koala_weight_fact:
                koala_weight_fact.append(random_fact)

        extract_integer = "".join(x for x in str(koala_weight_fact) if x.isdigit())

    return int(extract_integer[4:])


print(koala_weight())
