#!/usr/bin/env python3

import codecs
import random
import sys
import csv
from enum import Enum

DEFAULT_PROMPT = """Given the following lineage relationships:
{quiz_relations}
{quiz_question}
Select the correct answer:
{quiz_answers}
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>."""

male_names = [
    'James', 'Robert', 'John', 'Michael', 'David',
    'William', 'Richard', 'Joseph', 'Thomas', 'Christopher',
    'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark',
    'Donald', 'Steven', 'Andrew', 'Paul', 'Joshua',
    'Kenneth', 'Kevin', 'Brian', 'George', 'Timothy',
    'Ronald', 'Jason', 'Edward', 'Jeffrey', 'Ryan',
    'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan',
    'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon',
    'Benjamin', 'Samuel', 'Gregory', 'Alexander', 'Patrick',
    'Frank', 'Raymond', 'Jack', 'Dennis', 'Jerry',
    'Tyler', 'Aaron', 'Jose', 'Adam', 'Nathan',
    'Henry', 'Zachary', 'Douglas', 'Peter', 'Kyle',
    'Noah', 'Ethan', 'Jeremy', 'Walter', 'Christian',
    'Keith', 'Roger', 'Terry', 'Austin', 'Sean',
    'Gerald', 'Carl', 'Harold', 'Dylan', 'Arthur',
    'Lawrence', 'Jordan', 'Jesse', 'Bryan', 'Billy',
    'Bruce', 'Gabriel', 'Joe', 'Logan', 'Alan',
    'Juan', 'Albert', 'Willie', 'Elijah', 'Wayne',
    'Randy', 'Vincent', 'Mason', 'Roy', 'Ralph',
    'Bobby', 'Russell', 'Bradley', 'Philip', 'Eugene'
]

female_names = [
    'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth',
    'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
    'Lisa', 'Nancy', 'Betty', 'Sandra', 'Margaret',
    'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle',
    'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie',
    'Dorothy', 'Rebecca', 'Sharon', 'Laura', 'Cynthia',
    'Amy', 'Kathleen', 'Angela', 'Shirley', 'Brenda',
    'Emma', 'Anna', 'Pamela', 'Nicole', 'Samantha',
    'Katherine', 'Christine', 'Helen', 'Debra', 'Rachel',
    'Carolyn', 'Janet', 'Maria', 'Catherine', 'Heather',
    'Diane', 'Olivia', 'Julie', 'Joyce', 'Victoria',
    'Ruth', 'Virginia', 'Lauren', 'Kelly', 'Christina',
    'Joan', 'Evelyn', 'Judith', 'Andrea', 'Hannah',
    'Megan', 'Cheryl', 'Jacqueline', 'Martha', 'Madison',
    'Teresa', 'Gloria', 'Sara', 'Janice', 'Ann',
    'Kathryn', 'Abigail', 'Sophia', 'Frances', 'Jean',
    'Alice', 'Judy', 'Isabella', 'Julia', 'Grace',
    'Amber', 'Denise', 'Danielle', 'Marilyn', 'Beverly',
    'Charlotte', 'Natalie', 'Theresa', 'Diana', 'Brittany',
    'Doris', 'Kayla', 'Alexis', 'Lori', 'Marie'
]

class QuizType(Enum):
    ANCESTOR = 1
    DESCENDANT = 2
    COMMON_ANCESTOR = 3
    COMMON_DESCENDANT = 4
    OTHER = 5

answer_templates = [
    (QuizType.ANCESTOR, "{p1_name} is {p2_name}'s ancestor."),
    (QuizType.DESCENDANT, "{p1_name} is {p2_name}'s descendant."),
    (QuizType.COMMON_ANCESTOR, "{p1_name} and {p2_name} share a common ancestor."),
    (QuizType.COMMON_DESCENDANT, "{p1_name} and {p2_name} share a common descendant."),
    (QuizType.OTHER, "None of the above is correct."),
]

def generate_quiz(length, quiz_type, shuffle=False, prompt=DEFAULT_PROMPT):
    character_names = random.sample(male_names + female_names, length)

    match quiz_type:
        case QuizType.ANCESTOR:
            ancestor_relations = [(i, i + 1) for i in range(length - 1)]
        case QuizType.DESCENDANT:
            ancestor_relations = [(i + 1, i) for i in range(length - 1)]
        case QuizType.COMMON_ANCESTOR:
            common_pos = random.randint(1, length - 2)
            ancestor_relations = [(i + 1, i) if i + 1 <= common_pos else (i, i + 1) for i in range(length - 1)]
        case QuizType.COMMON_DESCENDANT:
            common_pos = random.randint(1, length - 2)
            ancestor_relations = [(i, i + 1) if i + 1 <= common_pos else (i + 1, i) for i in range(length - 1)]
        case _:
            raise ValueError("Unsupported quiz type")
    
    if shuffle:
        random.shuffle(ancestor_relations)

    quiz_relations_str = ""
    for p1, p2 in ancestor_relations:
        p1_name = character_names[p1]
        p2_name = character_names[p2]

        if random.choice([True, False]):
            quiz_relations_str += f"* {p1_name} is {p2_name}'s ancestor.\n"
        else:
            quiz_relations_str += f"* {p2_name} is {p1_name}'s descendant.\n"

    p1_name = character_names[0]
    p2_name = character_names[length-1]

    quiz_question_str = f"Determine the lineage relationship between {p1_name} and {p2_name}."
 
    answer_options = answer_templates[:-1]
    if shuffle:
        random.shuffle(answer_options)
    answer_options.append(answer_templates[-1])

    quiz_answers_str = ""
    correct_answer_num = 0
    for i, (quiz_answer_type, quiz_answer_template) in enumerate(answer_options):
        answer_num = i + 1
        quiz_answer = quiz_answer_template.format(p1_name=p1_name, p2_name=p2_name);
        quiz_answers_str += f"{answer_num}. {quiz_answer}\n"
        if quiz_answer_type == quiz_type:
            correct_answer_num = answer_num

    assert(correct_answer_num != 0)

    quiz = prompt.format(quiz_relations=quiz_relations_str.strip(), quiz_question=quiz_question_str.strip(), quiz_answers=quiz_answers_str.strip())
    return quiz, correct_answer_num

def generate_quizzes(length, num_quizzes=10, prompt=DEFAULT_PROMPT, shuffle=False, seed=None):
    if seed is not None:
        random.seed(seed)
    quiz_types = list(QuizType)
    # do not generate QuizType.OTHER quizes
    quiz_types.pop()
    for i in range(num_quizzes):
        for quiz_type in quiz_types:
            quiz, correct_answer = generate_quiz(length, quiz_type, shuffle=shuffle, prompt=prompt)
            yield (str(quiz_type).removeprefix("QuizType."), correct_answer, quiz)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help = "Number of people connected with lineage relationships in the quiz.", type=int, required=True)
    parser.add_argument("-p", "--prompt", help = "Prompt template of the quiz. The default prompt template is: " + repr(DEFAULT_PROMPT), default=DEFAULT_PROMPT)
    parser.add_argument("-s", "--shuffle", help = "Shuffle the order of lineage relations in the quiz.", action="store_true")
    parser.add_argument("-n", "--number", help = "Number of quizzes generated for each valid answer option.", default=10, type=int)
    parser.add_argument("-r", "--seed", help = "Random seed value", default=None, type=int)
    args = parser.parse_args()

    prompt = codecs.escape_decode(bytes(args.prompt, "utf-8"))[0].decode("utf-8")

    csv_writer = csv.writer(sys.stdout)
    for relation_name, correct_answer, quiz in generate_quizzes(args.length, args.number, prompt, args.shuffle, args.seed):
        csv_writer.writerow([args.length, relation_name, correct_answer, quiz])
 
