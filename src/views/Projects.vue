<template>
  <div class="container-fluid">
    <div class="intro">
      <h1 id="hook">Case Studies</h1>
      <p class = 'hook-sub'>
        Since 2014, we've helped create software for 15+ nonprofits <br />
        and impact groups. Here's two of our favorites.
      </p>
    </div>
    <div class="row" id="case-studies" ref="caseStudies">
      <div v-for="project in caseStudies" :key="project.name" class="col-sm card case-card">
        <div class="case-card-text" :style="{ height: summaryHeight }">
          <h6>{{ project.name }}</h6>
          <p>{{ project.summary }}</p>
        </div>
        <img
          alt="social good image"
          :style="{'--tint': themeColors['tint-'+project.color]}"
          :src="project.background">
        <h6 class="link-case"><a @click="goToProfile(project.name)" id="link-1" :style="{ color: themeColors['bold-' + project.color]}" class="hvr-bounce-in">READ CASE</a></h6>
      </div>
    </div>
    <div class="intro" id="current-intro">
      <h1 id="hook">Current projects</h1>
      <p class ='hook-sub'>
        Here are our current projects for the 2019-20 academic year.
      </p>
    </div>
    <div class="row" id="current-projects">
      <div v-for="project in currentProjects" :key="project.name" class="project-card">
        <img
          :src="project.background">
        <div class="case-card-text">
          <h5>{{ project.name }}</h5>
          <p>{{ project.summary }}</p>
          <h6 class="link-case">
            <a @click="goToProfile(project.name)" id="link-1"
               class="hvr-bounce-in">READ MORE</a>
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import projects from '@/data/projects.json'
import themeColors from '@/data/colors.json'

export default {
  data: function () {
    const colors = ['orange', 'yellow', 'blue']
    let i = 0
    const caseStudies = []
    const currentProjects = []
    for (let project of projects) {
      if (project.featured) {
        project.color = colors[i++ % colors.length]
        caseStudies.push(project)
      }
      if (project.wip) {
        currentProjects.push(project)
      }
    }
    return {
      currentProjects: currentProjects,
      caseStudies: caseStudies,
      themeColors: themeColors,
      summaryHeight: '20px'
    }
  },
  mounted () {
    // Max the project case study summary card text's all be the same height
    // so that the images, text, and "read case" button vertically align
    this.summaryHeight = Math.max(...Array.from(this.$refs.caseStudies.children)
      .map((child) => child.firstChild.scrollHeight)) + 'px'
  },
  methods: {
    goToProfile (name) {
      this.$router.push({ path: 'profile', query: { name: name } })
    }
  },
  name: 'Projects'
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

#hook{
  font-size: 5em;
}

h5 {
  text-transform: uppercase;
  font-weight: 800;
  font-size: 1em
}

h6{
  text-transform: uppercase;
  font-weight: 800;
}

.hook-sub{
  font-size: 1.2em;
  padding-top: 2.5vh;
}
#case-studies {
  background-color: #424242;
  padding: 0 50px;
  display: flex;
  justify-content: space-evenly;
}

.row {
  margin: 0;
  padding: 0;
}

.card {
  margin: 2em;
  padding: 1em 0;
  max-width: 400px;
  img {
    --tint: black;
    width: 100%;
    margin: 0.5em auto 1em;
    background-color: #ffffff;
    float: left;
    padding: 4px;
    position: relative;
    &::before {
      content: "";
      width: 200px;
      height: 200px;
      display: block;
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      transition: all .3s linear;
      background: var(--tint);
    }
  }
}

.case-card {
  background-color: #292929;
  min-width: 200px;
  .case-card-text {
    padding: 1em;
  }
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
  width: 200px;
  margin-left: 30px;
  margin-top: 30px;
  img {
    width: 100%;
    margin-bottom: 10px;
  }
}

#current-intro {
  background-color: $secondary-light;
  color: $secondary-medium;
}

#current-projects {
  background-color: #ffffff;
  padding: 0 50px;
  display: flex;
  flex-wrap: wrap;
}

/* HOVER-CSS Bounce Out */
.hvr-bounce-in {
  display: inline-block;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0);
  -webkit-transition-duration: 0.5s;
  transition-duration: 0.5s;
}
.hvr-bounce-in:hover, .hvr-bounce-in:focus, .hvr-bounce-in:active {
  -webkit-transform: scale(1.2);
  transform: scale(1.2);
  -webkit-transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
  transition-timing-function: cubic-bezier(0.47, 2.02, 0.31, -0.36);
}
</style>
