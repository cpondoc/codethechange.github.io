<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Case Studies</h1>
      <p>
        Since 2014, we've helped create software for 30+ nonprofits <br />
        and impact groups. Here's three of our favorites.
      </p>
    </div>
    <div class="row" id="case-studies">
      <div class="col-sm card case-card">
        <div class="case-card-text">
          <h6>TEACH FOR AMERICA</h6>
          <p>How we built a scalable donor matching plaform.</p>
        </div>
        <img
          alt="social good image"
          src="http://unbounce.com/photos/landing-pages-that-could-be-marketing-more-money.png">
        <h6 class="link-case"><a href="#" id="link-1">READ CASE</a></h6>
      </div>
      <div class="col-sm card case-card">
        <div class="case-card-text">
          <h6>TEACH FOR AMERICA</h6>
          <p>How we built a scalable donor matching plaform.</p>
        </div>
        <img
          alt="blockchain for social good"
          src="https://cdn-images-1.medium.com/max/1600/1*ixmhchkbfqev5Lllrho5FQ.png">
        <h6 class="link-case"><a href="#" id="link-2">READ CASE</a></h6>
      </div>
      <div class="col-sm card case-card">
        <div class="case-card-text">
          <h6>TEACH FOR AMERICA</h6>
          <p>How we built a scalable donor matching plaform.</p>
        </div>
        <img
          alt="food for social good"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzuW4_tDp6KIFjU0m04OQN-C4L9AsSE3M1UAnVWBIFZScukb7p">
        <h6 class="link-case"><a href="#" id="link-3">READ CASE</a></h6>
      </div>
    </div>
    <div class="intro" id="current-intro">
      <h1 id="hook">Current projects</h1>
      <p>
        Since 2014, we've helped create software for 30+ nonprofits <br />
        and impact groups. Here's three of our favorites.
      </p>
    </div>
    <div class="row" id="current-projects">
      <div class="col-sm card project-card">
        <img
          alt="Mannabase companion image"
          src="https://www.bitdegree.org/tutorials/wp-content/uploads/2018/03/types-of-cryptocurrency-1.png">
        <div class="case-card-text">
          <h6>EMERGING TECH</h6>
          <p>Using blockchain for social good with Mannabase</p>
        </div>
      </div>
      <div class="col-sm card project-card">
        <img
          alt="education image"
          src="https://www.timeshighereducation.com/sites/default/files/styles/the_breaking_news_image_style/public/istock-499343530.jpg?itok=4ObUNN41">
        <div class="case-card-text">
          <h6>EDUCATION</h6>
          <p>Optimizing e-learning for a global audience with Oppia</p>
        </div>
      </div>
      <div class="col-sm card project-card">
        <img
          alt="another education image"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRccnWVVh1HATv5yUwA8ce_iiadXtZEpUcQOye07uvL3lvs0aUYhw">
        <div class="case-card-text">
          <h6>EDUCATION</h6>
          <p>Optimizing e-learning for a global audience with Oppia</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import ProjectCard from '@/components/ProjectCard.vue'
import projects from '@/data/projects.json'

export default {
  data: function () {
    const projects = []
    for (let project of projects) {

    }
  },
  computed: {
    featured: function() {
      
    }
  },
  methods: {
  },
  name: 'Projects',
  components: {
  }
}
</script>

<style lang="scss" scoped>
@import '../theme.scss';

.container-fluid {
  padding: 0;
}

.intro {
  height: 20em;
  padding: 50px 50px 50px 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#case-studies {
  background-color: #424242;
  padding: 0 50px;
}

.card {
  margin: 2em;
  padding: 1em 0;
  .case-card-text {
    margin: 0.7em;
  }
  img {
    width: 100%;
    height: auto;
    margin: 0.5em auto 1em;
  }
}

.case-card {
  background-color: #292929;
  .link-case {
    text-align: right;
    margin: 0.7em;
    #link-1 {
      color: #fff469;
    }
    #link-2 {
      color: rgb(233, 97, 233);
    }
    #link-3 {
      color: rgb(167, 255, 255);
    }
    a {
      text-decoration: none;
      &:hover {
        text-decoration: none;
        color: inherit;
      }
    }
  }
}

.project-card {
  color: #000000;
  border: none;
}

#current-intro {
  background-color: $secondary-light;
  color: $secondary-medium;
}

#current-projects {
  background-color: #ffffff;
  padding: 0 50px;
}

</style>
