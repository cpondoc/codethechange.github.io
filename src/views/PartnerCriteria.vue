<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Partner Criteria</h1>
      <p class = 'hook-sub'>
        Interested in partnering with us? Here's what we need and want
        from partners and projects.
      </p>
    </div>
    <div id="white">
      <div id="content">
        <!-- Line breaks in the markdown are treated literally -->
        <vue-markdown>

# Absolutely Necessary

These are non-negotiable. Without exception, each partner and project must clearly meet each of these criteria.

* Our partners must act ethically and legally.
* Our work on the project and with the partner must comply with any applicable regulations, including the Stanford Administrative Guide and local, state, and federal law.
    * For example, foreign partners must not be in countries where sanctions forbid our work.

# Very Important

We think very carefully before working on any project where these criteria might not be met. Exceptions are possible, but only with caution.

* Partners should be responsive to team leads and engaged in guiding our work on the project.

* Working on the project should not expose contributors to risks that are unreasonable given contributors’ positions as student volunteers.

    * For example, work that exposes contributors to potential criminal or civil liability (e.g. work with protected health information or trade secrets) should be avoided.

* Any mistakes by contributors should not endanger anyone’s safety.

    * If work is on projects critical to life or safety (e.g. work on implanted medical devices), safeguards (e.g. code reviews) should be in place to catch any errors. Contributors are students, and mistakes should be expected.

* Partners should be non-profits or otherwise have a legal structure that prioritizes the charitable mission.

    * In general, we do not work with for-profit organizations, but we are fine partnering with public benefit corporations.

    * More generally, it should be clear that contributors’ work will go entirely to support the charitable mission.

* Organizations should be in need of contributions.

    * For example, consider the following scenario. We contribute to a project, so the partner does not have to hire a developer to develop the project. Instead, the partner uses that money to give its well-paid CEO a bonus. In this case, our work essentially gave the CEO an unnecessary bonus, which is not a charitable cause.

* Projects should have an appropriate scope. The quantity and effectiveness of work varies by team, but a rough estimate is that each project will be worked-on by a team of 1-3 for 6 hours a week for 7 weeks in each of Stanford’s 3 academic quarters. We should be able to contribute an impactful part of the overall project within that time.

* Projects should require relatively little esoteric knowledge. For any needed knowledge not covered in the first couple introductory college computer science courses, assume that contributors will need to learn it on their own. This learning should be doable.

    * Note that many contributors will come in with little experience with front-end development. In particular, our introductory computer science classes do not cover web or mobile app development. Contributors can absolutely learn these skills, but it will take time that should be accounted for in project scope.

* Projects should be impactful. Our contributions should, as directly as possible, make life better for some group of people in need. Contributions are essentially donations of time and effort, so like with monetary donations, we want to make sure our donations are going to good causes.

# Preferable

These are the criteria we look for to find good projects.

* We like projects whose source code is publicly available under an open-source license (a license approved by the [Open Source Initiative](https://opensource.org/)).

* We like projects that utilize technologies that are either likely to be familiar to contributors or are likely to be useful for contributors in the near future.

    * Even though contributors are likely to be unfamiliar with web development, web development frameworks are useful to learn, so these frameworks can make a project more appealing.

* We like mature projects that have clear, concrete goals and a plentiful supply of starter tasks.

    * Starter tasks are important for the onboarding process.

    * In our experience, vague projects tend to struggle, while concrete ones tend to flourish.

* We like projects that are backed by established, stable organizations.

    * This helps us see that the project will be supported in the long term.

* We like projects that have already demonstrated some impact (e.g. number of users, trees saved, etc.)

    * This validates our belief that our work will be impactful.

# Icing on the Cake

These are great to have, but not needed for the project to be a good one.

* We love it when partners are be willing to mentor contributors, for example through code reviews.

* It’s great when the project is open to and welcoming of new contributors from the open source community.
        </vue-markdown>

      </div>
    </div>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'

export default {
  data: function () {
    return {}
  },
  computed: {
  },
  methods: {
  },
  name: 'ProjectCriteria',
  components: {
    VueMarkdown
  }
}
</script>

<style lang="scss" scoped>
@import '../theme.scss';

.container-fluid {
  padding: 0;
}

.intro {
  padding: 50px 50px 50px 250px;
  @media only screen and (max-width: 700px) {
    padding: 20px;
  }
}

#white {
    background-color: #ffffff;
    display: flex;
    justify-content: center;
}

#content {
    padding: 60px;
    max-width: 900px;
    color: #5e5e5e;
    font-family: 'Open Sans';
    font-size: 1em;
    font-style: normal;
    font-stretch: normal;
}

#hook{
  font-size: 5em;
}

.hook-sub{
  font-size: 1.2em;
  padding-top: 2.5vh;
}
</style>
