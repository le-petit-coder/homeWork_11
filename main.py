from functions import *
from flask import Flask, render_template


def main():
    app = Flask(__name__)

    @app.route("/")
    def page_main():
        candidates = load_candidates()
        return render_template('list.html', candidates=candidates)

    @app.route("/candidates/<int:candidate_id>")
    def page_candidates(candidate_id):
        candidate = get_by_pk(candidate_id)
        if not candidate:
            return "Кандидат не найден"
        return render_template('card.html', candidate=candidate)

    @app.route("/search/<candidate_name>")
    def name_candidate(candidate_name):
        candidates = get_by_name(candidate_name)
        return render_template('search.html', candidates=candidates)

    @app.route("/skill/<skill_name>")
    def page_skills(skill_name):
        candidates = get_by_skill(skill_name)
        return render_template('skill.html', candidates=candidates)

    app.run()


if __name__ == '__main__':
    main()
