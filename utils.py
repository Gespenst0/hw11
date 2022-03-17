import json


def load_candidates_from_json(path):
    with open(f"{path}", "r") as file:
        candidates_json = file.read()
        candidates = json.loads(candidates_json)
        return candidates


def get_all_candidates():
    candidate_list = []
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        person = {}
        person["name"] = candidate["name"]
        person["id"] = candidate["id"]
        candidate_list.append(person)
    return candidate_list


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    candidate_card = {}
    for candidate in candidates:
        if str(candidate["id"]) == str(candidate_id):
            candidate_card["name"] = candidate["name"]
            candidate_card["position"] = candidate["position"]
            candidate_card["picture"] = candidate["picture"]
            candidate_card["skills"] = candidate["skills"]
    return candidate_card


def get_candidates_by_skill(skill_name):
    list_candidates = []
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if skill_name in candidate["skills"]:
            person = {}
            person["name"] = candidate["name"]
            person["id"] = candidate["id"]
            list_candidates.append(person)
    return list_candidates


def get_candidates_by_name(candidate_name):
    list_candidates = []
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate_name in candidate["name"]:
            person = {}
            person["name"] = candidate["name"]
            person["id"] = candidate["id"]
            list_candidates.append(person)
    return list_candidates

