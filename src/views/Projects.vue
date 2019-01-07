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
      <div v-for="project in caseStudies" :key="project.name" class="col-sm card case-card">
        <div class="case-card-text">
          <h6>{{ project.name }}</h6>
          <p>{{ project.summary }}</p>
        </div>
        <img
          alt="social good image"
          :src="project.background">
        <h6 class="link-case"><a href="#" id="link-1">READ CASE</a></h6>
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
      <div v-for="project in currentProjects" :key="project.name" class="col-sm card project-card">
        <img
          alt="Mannabase companion image"
          :src="project.background">
        <div class="case-card-text">
          <h6>{{ project.name }}</h6>
          <p>{{ project.summary }}</p>
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
    const caseStudies = []
    const currentProjects = []
    for (let project of projects) {
      if (project.featured) {
        caseStudies.push(project)
      }
      if (project.wip) {
        currentProjects.push(project)
      }
    }
    return {
      currentProjects: currentProjects,
      caseStudies: caseStudies
    }
  },
  computed: {
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
