
def parse_workflow(row):
    name, rules = row.split("{")
    rules = rules.rstrip("}").split(",")
    rules_list = [tuple(rule.split(":")) for rule in rules[:-1]]
    rules_list.append(("default", rules[-1]))
    return name, rules_list

def parse_workflows(workflows_list):
    workflows = {}
    for row in workflows_list:
        name, rules_dict = parse_workflow(row)
        workflows[name] = rules_dict
    return workflows

def parse_element(row):
    elements = row.strip("{}").split(",")
    values_dict = {}
    for element in elements:
        name, value = element.split("=")
        values_dict[name] = int(value)
    return values_dict

def less_than(a, b):
    return a < b

def geater_than(a, b):
    return a > b

def check_element(element: dict, workflows: dict, current_worflow="in"):
    rules = workflows[current_worflow]
    for rule in rules:
        condition, workflow_or_end_condition = rule
        if ">" in condition:
            compare_f, splitter = geater_than, ">"
        else:
            compare_f, splitter = less_than, "<"
        cond_elem, cond_value = condition.split(splitter) if condition != "default" else (0, 0)
        
        if condition == "default" or compare_f(element[cond_elem], int(cond_value)):
            if workflow_or_end_condition == "A":
                return sum(element.values())
            if workflow_or_end_condition == "R":
                return 0
            return check_element(element, workflows, workflow_or_end_condition)
        

def aoc(input):
    with open(input) as file:
        data = file.read()

    workflows_list, elements_list = [pattern.split() for pattern in data.split("\n\n")]
    workflows = parse_workflows(workflows_list)
    elements = [parse_element(row) for row in elements_list]

    print(sum([check_element(element, workflows) for element in elements]))


    

aoc("../input.txt")