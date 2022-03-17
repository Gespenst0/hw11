from flask import Flask, render_template

import utils


app = Flask(__name__)


@app.route("/")
def title_page():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def card(candidate_id):
    candidate_data = utils.get_candidate(candidate_id)
    return render_template('card.html', candidate=candidate_data)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, len_list=len(candidates))


@app.route('/skill/<skill_name>')
def search_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, len_list=len(candidates), skill_name = skill_name)


app.run()

